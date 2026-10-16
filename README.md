# 西南财经大学本科毕业论文 LaTeX 模板

用于撰写西南财经大学本科生毕业论文（设计），包含封面、学术声明、中英文摘要、目录、正文、参考文献、附录、致谢和封底。

本项目基于 [SWUFE-DB-Group/SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 修改，该项目又基于[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 修改。底层使用 SJTUTeX 的 `sjtuthesis` 文档类，本项目在 `setup.tex` 中配置西南财经大学本科论文的版式与论文信息。

## 规范来源

排版依据为《西南财经大学本科生毕业论文（设计）撰写与印制规范》。

- [规范来源：西南财经大学计算机与人工智能学院](https://it.swufe.edu.cn/info/1166/22938.htm)

提交论文时，请结合学院当年的具体要求检查最终稿。

## 编译

需要安装包含 **XeLaTeX**、**BibTeX** 和 **latexmk** 的 TeX 发行版，以及 `ctex`、`fontspec`、`xeCJK`、`jsonparse`、`newtx`、`tikz`、`pgfplots` 等依赖。使用较新的完整 TeX Live 可减少缺少宏包的问题。

在项目根目录执行：

```bash
latexmk -xelatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

生成文件为 `main.pdf`。`latexmk` 会读取 `.latexmkrc`，自动设置本地文档类和参考文献样式的搜索路径，按需运行 BibTeX，并重复编译以更新目录、引用和页码；无需使用 Biber。

Linux / macOS 也可以使用：

```bash
make             # 编译
make pvc         # 监听文件变化并自动编译
make clean       # 清理中间文件，保留 main.pdf
make cleanall    # 同时删除 main.pdf
```

Windows 可在命令提示符中运行 `Compile.bat`，或直接使用上面的 `latexmk` 命令。批处理脚本也支持 `Compile.bat clean` 和 `Compile.bat cleanall`。

### Overleaf 等在线平台

在线编译无需在本机安装 TeX。以 Overleaf 为例：

1. 将项目源文件打包为 ZIP，保留 `main.tex`、`setup.tex`、`config.json`、`refs.bib`、`.latexmkrc`，以及完整的 `contents/`、`figures/`、`font/`、`texmf/` 目录。
2. 在 Overleaf 中选择 **New Project → Upload Project**，上传 ZIP。确认 `main.tex` 位于项目根目录。
3. 在在线项目根目录，将 `.latexmkrc` 重命名为 **`latexmkrc`**（去掉开头的点），保留其内容，使平台能够加载本地 `texmf/` 中的文档类、配置和 BibTeX 样式。
4. 在项目设置中，将 **Main document** 设为 `main.tex`，**Compiler** 设为 **XeLaTeX**，并选择平台提供的较新 TeX Live 版本。
5. 修改 `config.json` 和 `contents/` 中的论文内容，点击 **Recompile**，编译完成后下载 PDF。

其他支持 XeLaTeX 的在线 LaTeX 平台可采用相同流程：上传完整项目、指定 `main.tex` 为主文档、选择 XeLaTeX，并确保平台读取项目中的 latexmk 配置。字体文件通过相对路径加载，需一并上传并保留原文件名。

参考 Overleaf 官方文档：[上传项目](https://www.overleaf.com/learn/latex/Kb/Uploading_a_project)、[latexmkrc 配置](https://docs.overleaf.com/managing-projects-and-files/the-latexmkrc-file)、[编译器与 TeX Live 版本](https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler)。

### 字体

仓库的 `font/` 目录已包含以下字体，由模板直接通过文件路径加载，无需另行安装：

| 字体文件 | 用途 |
| --- | --- |
| `STZHONGS.TTF` | 华文中宋，用于封面主标题及章节等标题 |
| `STFANGSO.TTF` | 华文仿宋，用于封面信息栏与日期 |
| `Times New Roman*.ttf` | Times New Roman 的常规、粗体、斜体及粗斜体，用于西文与数字 |

华文中宋标题和华文仿宋日期的粗体使用合成加粗。文件名须与配置一致，尤其注意 Linux 下的大小写。

`texmf/` 内保留文档类按操作系统和字体选项加载的配置文件。

### 字号与间距

正文、摘要、参考文献和致谢采用小四号（12bp），一级标题为二号（22bp），二级标题为小三号（15bp），三级标题为小四号（12bp）。图表标题与内容为五号（10.5bp），脚注为小五号（9bp）。中英文关键词整行加粗。

模板使用 CTeX 的单倍基线（字号的 1.2 倍），正文和标题再乘 1.5；正文实际基线间距为 21.6bp。标题段前、段后的“行”以正文基线为单位：一级标题为 3 行、2 行，二、三级标题均为 1 行、1 行。图表使用单倍行距，题注上下间距各为五号单倍基线的 0.5 行。此处明确的是 LaTeX 的行距计算方式，并非声称与 Word 的字体度量逐像素一致。

## 填写论文信息

优先修改根目录的 `config.json`。论文信息统一放在 `info` 中，标题、姓名、学院、专业、导师和关键词均直接填写字符串，无需区分中英文。配置中已提供的字段会覆盖 `setup.tex` 的默认值；空字符串可用于清空可选字段。JSON 字符串中的 LaTeX 反斜杠需要写成 `\\`。

| 字段 | 用途 |
| --- | --- |
| `review` | 是否启用盲审模式，取 `true` 或 `false` |
| `citation_superscript` | 文献引用是否使用上标；默认 `false`（非上标），设为 `true` 启用上标 |
| `bibliography.source` | 参考文献来源，默认 `"bib"`；设为 `"tex"` 使用手工参考文献 |
| `bibliography.bib_file` | BibTeX 数据库路径，默认 `"refs.bib"` |
| `bibliography.tex_file` | 手工参考文献路径，默认 `"contents/参考文献.tex"` |
| `info.title` | 完整论文标题，用于页眉和 PDF 元数据 |
| `info.display_title` | 封面题目的第一行；省略或留空则使用完整标题 |
| `info.title_second` | 封面题目的第二行；省略或留空则只显示一行 |
| `info.author` | 作者姓名 |
| `info.student_id` | 学号，建议保留为字符串 |
| `info.department` | 学院名称 |
| `info.major` | 专业名称 |
| `info.grade` | 年级，如 `2022级` |
| `info.supervisor` | 导师姓名及职称 |
| `info.final_date` | 封面日期，如 `2026年5月` |
| `info.keywords` | 关键词，用英文逗号分隔 |

例如，封面题目需要分成两行时，可设置：

```json
{
  "info": {
    "title": "面向金融数据的风险识别方法研究",
    "display_title": "面向金融数据的",
    "title_second": "风险识别方法研究"
  }
}
```

将上述三个字段填写到 `config.json` 的 `info` 中，其他字段按需保留。封面每行的下划线宽度为 9cm，长标题可通过 `display_title` 和 `title_second` 合理拆分。只填写 `title` 时，封面使用完整标题，不保留示例标题的分行。

不使用 JSON 时，可直接修改 `setup.tex` 第 2 节的 `\swufesetup` 默认设置。该设置同样只有一套 `title`、`author`、`department`、`major`、`supervisor`、`keywords` 等字段；学号使用 `id`，封面分行与日期使用 `display-title`、`title-second` 和 `final-date`。

中文摘要的关键词由 `info.keywords` 自动生成；英文摘要的正文及英文关键词直接在 `contents/abstract.tex` 中维护。

将 `review` 设为 `true` 时，封面隐藏姓名、学号和导师信息，并跳过致谢页。正文、插图等自行填写的个人信息仍需检查。

## 撰写正文与参考文献

在 `contents/` 中修改各章内容；增加或删除章节时，同步调整 `main.tex` 中的 `\input{...}`。`contents/格式与规范指南.tex` 提供表格、插图、公式、脚注、算法和代码的示例。

图表格式由 `setup.tex` 统一设置：

- 图题、表题均为五号黑体加粗，居中，前后各空半行。
- 表格的 `\caption` 写在表格内容之前，插图的 `\caption` 写在图片之后。
- 图表内容为五号字体、单倍行距，无需在每个浮动体中重复设置。

外部图片中已经绘制的文字需要在制图软件中设置字号；LaTeX 的字体设置只作用于其排版的文字。

### 参考文献来源

默认从 `refs.bib` 读取文献，由 BibTeX 按 **GB/T 7714-2015 顺序编码制**生成参考文献表。配置如下：

```json
"bibliography": {
  "source": "bib",
  "bib_file": "refs.bib",
  "tex_file": "contents/参考文献.tex"
}
```

将 `source` 改为 `"tex"`，即可使用 `contents/参考文献.tex` 中的 `thebibliography` 和 `\bibitem` 手工维护参考文献，格式与顺序需自行维护。选择 `"bib"` 但指定的 `.bib` 文件不存在时，模板会提示警告并自动读取 `tex_file`。两种来源使用相同的 `\cite{文献键}` 命令。

`.bib` 模式自动保证**中文在前、外文在后，各组内部按正文首次引用的顺序排列**，全部条目从 `[1]` 连续编号。即使先引用英文文献，文末仍先列中文文献；数据库中的录入顺序不会影响这一规则。默认只列出被引用的条目，需要列出未引用文献时可使用 `\nocite{文献键}` 或 `\nocite{*}`。

可参考 `refs.bib` 中的条目添加文献，例如：

```bibtex
@book{西瓜书,
  author    = {周志华},
  title     = {机器学习},
  address   = {北京},
  publisher = {清华大学出版社},
  year      = {2016},
  language  = {chinese}
}
```

`language` 可设为 `chinese` 或 `english`；省略时，样式会根据作者、标题等内容自动识别。多人作者用 `and` 分隔。语言字段用于文献排序与著录格式，不需要为同一条文献填写中英文两套信息。

本项目的 `swufe-gbt7714-numerical.bst` 基于 [gbt7714-bibtex-style](https://github.com/zepinglee/gbt7714-bibtex-style) 的 GB/T 7714-2015 样式修改，仅增加中文优先排序，保留国标著录格式。

### 正文引用

正文引用默认使用非上标的方括号数字。若需上标引用，在 `config.json` 中将 `citation_superscript` 设为 `true`；该字段省略或设为 `false` 时均使用非上标。引用命令保持一致，例如：

```latex
分类与回归等机器学习方法为模型构建提供了基础\cite{西瓜书}。
相关概念和训练方法可参考教材\cite{西瓜书,深度学习图书}。
残差网络、注意力机制与自适应优化可联合引用\cite{ResNet,Transformer,Adam}。
网络结构设计可参考残差连接与批归一化方法\cite{ResNet,BatchNormalization}。
```

花括号中的文献键须与 `.bib` 中的条目键或 `\bibitem{文献键}` 一致，多篇文献用逗号分隔。模板会自动按文献编号排序，两个编号用逗号分隔（如 `[1,2]`），三个及以上连续编号合并为横线连接的范围（如 `[3–5]`），不连续编号仍用逗号分隔（如 `[4,6]`）。这些规则同时适用于非上标和上标引用。具体编号由当前参考文献来源决定，正文无需手工维护。绪论提供了单篇及多篇中文文献的引用示例，系统设计章节提供了英文文献及连续编号合并的示例。

脚注使用 `\footnote{说明文字}` 插入。`setup.tex` 中的 `fnmark-style=plain` 将正文标记设为普通阿拉伯数字上标，`footmisc` 的 `perpage` 选项使每页从 1 开始编号。同一章的不同页面及下一章均提供了脚注示例；使用 `latexmk` 编译可自动完成逐页编号所需的多遍处理。

## 项目结构

```text
.
├── main.tex                 # 主文档与章节顺序
├── setup.tex                # 元数据读取、字体与版式配置
├── config.json              # 论文信息、盲审开关与引用样式
├── refs.bib                 # 默认的参考文献数据库
├── contents/                # 封面、摘要、正文及其他章节
├── figures/                 # 实际使用的校名、校徽、声明页、封底等素材
├── font/                    # 华文中宋、华文仿宋与 Times New Roman 字体文件
├── texmf/                   # 本地论文文档类、配置与 GB/T 7714 BibTeX 样式
├── .latexmkrc               # 编译引擎与本地依赖搜索路径
├── .gitignore               # 编译产物与编辑器临时文件忽略规则
├── Makefile                 # make 编译入口
├── Compile.bat              # Windows 编译入口
└── LICENSE
```

学术声明与封底分别通过 `contents/学术声明.tex`、`contents/封底.tex` 嵌入 `figures/copyright.pdf` 和 `figures/last.pdf`。这些 PDF 是编译输入，应与源代码一起保留。生成的 `main.pdf` 和编译中间文件由 `.gitignore` 忽略。

## 许可与致谢

项目许可证见 [LICENSE](LICENSE)。感谢 [SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 及其所基于的[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 的作者，以及 [gbt7714-bibtex-style](https://github.com/zepinglee/gbt7714-bibtex-style) 的维护者。本地 SJTUTeX 文件和修改后的 BibTeX 样式保留其原有的 LaTeX Project Public License 声明。
