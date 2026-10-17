"""Compile isolated copies with distribution SJTUTeX and no latexmkrc.

Run: python3 -m unittest discover -s tests -v
Requires XeLaTeX, BibTeX, latexmk and Poppler; no Python dependencies.
"""

import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ("xelatex", "bibtex", "latexmk", "pdfinfo", "pdftotext", "pdftohtml", "pdffonts")


@unittest.skipUnless(all(shutil.which(t) for t in TOOLS), "TeX/Poppler required")
class TemplateTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="swufe-bachelor-test-")
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        for name in ("main.tex", "setup.tex", "config.json", "refs.bib",
                     "swufe-gbt7714-numerical.bst"):
            shutil.copy2(ROOT / name, self.project / name)
        shutil.copytree(ROOT / "contents", self.project / "contents")
        for name in ("font", "figures"):
            (self.project / name).symlink_to(ROOT / name, target_is_directory=True)
        self.config = json.loads((self.project / "config.json").read_text())
        self.config["info"].update(
            title="迁移 Test Title", display_title="", title_second="",
            author="迁移作者", supervisor="迁移导师", student_id="2099123456",
            department="迁移学院", keywords="迁移关键词,排序校验",
        )

    def build(self, config=True, succeeds=True):
        if config:
            (self.project / "config.json").write_text(
                json.dumps(self.config, ensure_ascii=False)
            )
        else:
            (self.project / "config.json").unlink()
        result = subprocess.run(
            ["latexmk", "-norc", "-xelatex", "-quiet", "-halt-on-error",
             "-interaction=nonstopmode", "main.tex"],
            cwd=self.project, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, timeout=120,
        )
        log = (self.project / "main.log").read_text(errors="replace")
        if not succeeds:
            self.assertNotEqual(result.returncode, 0)
            return log
        self.assertEqual(result.returncode, 0, log[-6000:])
        version = re.search(r"Document Class: sjtuthesis \S+ v?(\d+\.\d+\.\d+)", log)
        self.assertIsNotNone(version)
        self.assertGreaterEqual(tuple(map(int, version[1].split("."))), (2, 3, 1))
        for warning in ("undefined citations", "undefined references", "Rerun to get",
                        "Label(s) may have changed", "unknown key", "Unknown key",
                        "Missing character", "Package fancyhdr Warning"):
            self.assertNotIn(warning, log)
        pdf = str(self.project / "main.pdf")
        self.info = subprocess.check_output(["pdfinfo", pdf], text=True)
        self.text = subprocess.check_output(["pdftotext", "-layout", pdf, "-"], text=True)
        self.compact = re.sub(r"\s", "", self.text)
        self.pages = self.text.split("\f")
        return log

    def assert_bib_order(self):
        bbl = (self.project / "main.bbl").read_text()
        self.assertEqual(re.findall(r"\\bibitem\[.*?\]\{(.*?)\}", bbl, re.DOTALL), [
            "西瓜书", "深度学习图书", "Transformer", "ResNet", "Adam", "BatchNormalization",
        ])

    def test_json_final_without_search_paths(self):
        self.build()
        for value in ("迁移TestTitle", "迁移作者", "迁移导师", "2099123456",
                      "迁移学院", "迁移关键词；排序校验", "Keywords:", "ABSTRACT"):
            self.assertIn(value, self.compact)
        self.assertIn("迁移 Test Title", self.info)  # JSON spaces survive rescanning.
        self.assertRegex(self.info, r"Author: +迁移作者")
        self.assertIn("Subject:         西南财经大学本科毕业论文（设计）", self.info)
        self.assertIn("迁移TestTitle", re.sub(r"\s", "", self.pages[0]))
        toc = (self.project / "main.toc").read_text()
        self.assertNotIn("ABSTRACT", toc)
        self.assertNotIn("摘要", re.sub(r"\s", "", toc))
        self.assert_bib_order()
        self.assertIn("[3–5]", self.compact)
        self.assertIn("[4,6]", self.compact)

    def test_json_review_hides_identity_and_pdf_author(self):
        self.config["review"] = True
        self.build()
        for value in ("迁移作者", "迁移导师", "2099123456", "时光荏苒"):
            self.assertNotIn(value, self.compact + self.info)
        self.assertIsNone(re.search(r"^Author:[^\S\r\n]*\S", self.info, re.MULTILINE))
        self.assertIn("迁移TestTitle", self.compact)

    def test_setup_defaults_without_json(self):
        self.build(config=False)
        for value in ("张三", "李四教授", "42100001", "2026年5月", "关键词："):
            self.assertIn(value, self.compact)
        self.assert_bib_order()

    def force_no_system_fonts(self):
        # Exercise distribution fallbacks even on hosts with installed Microsoft fonts.
        path = self.project / "main.tex"
        path.write_text(path.read_text().replace(
            r"\input{setup}",
            r"\RenewDocumentCommand{\IfFontExistsTF}{m m m}{#3}" "\n" r"\input{setup}",
        ))

    def embedded_fonts(self):
        return subprocess.check_output(
            ["pdffonts", str(self.project / "main.pdf")], text=True
        )

    def test_no_font_directory(self):
        (self.project / "font").unlink()  # Remove this copy's symlink, not repo fonts.
        self.build()
        self.assertIn("迁移TestTitle", self.compact)
        self.assert_bib_order()

    def test_empty_font_directory_and_no_system_fonts(self):
        (self.project / "font").unlink()
        (self.project / "font").mkdir()
        self.force_no_system_fonts()
        log = self.build()
        for message in ("using TeX Gyre TermesX", "using FandolSong", "using FandolFang"):
            self.assertIn(message, log)
        fonts = self.embedded_fonts()
        for family in ("TeXGyreTermesX-Regular", "TeXGyreTermesX-Bold",
                       "TeXGyreTermesX-Italic", "FandolSong-Bold", "FandolFang"):
            self.assertIn(family, fonts)
        for family in ("TimesNewRoman", "STZhongsong", "STFangsong"):
            self.assertNotIn(family, fonts)
        self.assert_bib_order()

    def test_partial_times_family_falls_back_together(self):
        (self.project / "font").unlink()
        (self.project / "font").mkdir()
        for path in (ROOT / "font").iterdir():
            if path.name != "Times New Roman Bold.ttf":
                (self.project / "font" / path.name).symlink_to(path)
        self.force_no_system_fonts()
        self.build()
        fonts = self.embedded_fonts()
        self.assertIn("TeXGyreTermesX-Regular", fonts)
        self.assertIn("TeXGyreTermesX-Bold", fonts)
        self.assertIn("STZhongsong", fonts)
        self.assertNotIn("TimesNewRoman", fonts)

    def test_manual_bibliography_and_superscript(self):
        self.config["bibliography"]["source"] = "tex"
        self.config["citation_superscript"] = True
        self.build()
        self.assertIn("[7–9]", self.compact)
        self.assertIn("[7,10]", self.compact)
        self.assertFalse((self.project / "main.blg").exists())

    def test_missing_bib_falls_back_to_tex(self):
        self.config["bibliography"]["bib_file"] = "missing.bib"
        log = self.build()
        self.assertIn("not found; using", log)
        self.assertIn("[7–9]", self.compact)

    def test_rejects_old_document_class(self):
        (self.project / "sjtuthesis.cls").write_text(
            r"\ProvidesClass{sjtuthesis}[2024/06/29 v2.1.3 test stub]" "\n"
            r"\LoadClass{article}" "\n"
        )
        self.assertIn("SJTUTeX 2.3.1 or newer is required", self.build(succeeds=False))

    def test_rendered_fonts_layout_and_footnotes(self):
        (self.project / "main.tex").write_text(r"""
\documentclass[type=bachelor,openany,oneside,cjk-font=fandol,baselineskip=false,linespread=1]{sjtuthesis}
\input{setup}
\makeatletter
\newcommand{\layoutprobe}{%
\typeout{SWUFE-BASELINE=\the\baselineskip}%
\typeout{SWUFE-INDENT=\the\parindent}%
\typeout{SWUFE-LEFT=\the\dimexpr1in+\oddsidemargin\relax}%
\typeout{SWUFE-RIGHT=\the\dimexpr\paperwidth-1in-\oddsidemargin-\textwidth\relax}%
}
\makeatother
\begin{document}
\layoutprobe
\chapter{一级标题测量}
\section{二级标题测量}
\subsection{三级标题测量}
正文测量\footnote{脚注首行测量。\par 脚注续段测量。}
\begin{table}[h]
\caption{表题测量}
\centering\begin{tabular}{cc}表格内容 & 测量内容\\\end{tabular}
\end{table}
\clearpage
正文测量\footnote{另一页脚注测量。}
\end{document}
""")
        log = self.build()
        for key, bp in (("BASELINE", 21.6), ("INDENT", 24),
                        ("LEFT", 3 / 2.54 * 72), ("RIGHT", 3 / 2.54 * 72)):
            value = re.search(r"SWUFE-" + key + r"=([\d.]+)pt", log)
            self.assertIsNotNone(value)
            self.assertAlmostEqual(float(value[1]) * 72 / 72.27, bp, places=3)
        xml = self.project / "fonts.xml"
        subprocess.run(["pdftohtml", "-xml", "-i", "-hidden", "-zoom", "2",
                        str(self.project / "main.pdf"), str(xml)], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        root = ET.parse(xml).getroot()
        fonts = {f.attrib["id"]: f.attrib for f in root.iter("fontspec")}
        for label, family, size in (("一级标题测量", "STZhongsong", "44"),
                                    ("二级标题测量", "FandolHei", "30"),
                                    ("三级标题测量", "FandolHei", "24"),
                                    ("正文测量", "FandolSong", "24"),
                                    ("表题测量", "FandolHei", "21"),
                                    ("表格内容", "FandolSong", "21"),
                                    ("脚注首行测量", "FandolSong", "18")):
            nodes = [n for n in root.iter("text") if label in "".join(n.itertext())]
            node = max(nodes, key=lambda n: int(fonts[n.attrib["font"]]["size"]))
            font = fonts[node.attrib["font"]]
            self.assertIn(family, font["family"])
            self.assertEqual(size, font["size"])
        for page in root.findall("page"):
            notes = [n for n in page.findall("text") if "脚注" in "".join(n.itertext())]
            first = next(n for n in notes if "首行" in "".join(n.itertext()) or
                         "另一页" in "".join(n.itertext()))
            marker = next(n for n in page.findall("text") if
                          "".join(n.itertext()).strip() == "1" and
                          abs(int(n.attrib["top"]) - int(first.attrib["top"])) < 15)
            gap = int(first.attrib["left"]) - int(marker.attrib["left"]) - int(marker.attrib["width"])
            self.assertLessEqual(gap, 6)  # At 2x zoom, 0.25em is 4.5 units.


if __name__ == "__main__":
    unittest.main()
