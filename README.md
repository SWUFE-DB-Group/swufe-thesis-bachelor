# 西南财经大学本科毕业论文 LaTeX 模板

用于撰写西南财经大学本科生毕业论文（设计），包含封面、学术声明、中英文摘要、目录、正文、参考文献、附录、致谢和封底。

**[预览模板效果（PDF）](https://github.com/SWUFE-DB-Group/swufe-thesis-bachelor/blob/main/example.pdf)**

本项目基于 [SWUFE-DB-Group/SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 修改，该项目又基于[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 修改。底层使用 SJTUTeX 的 `sjtuthesis` 文档类，本项目在 `setup.tex` 中配置西南财经大学本科论文的版式与论文信息。

## 规范来源

排版依据为《西南财经大学本科生毕业论文（设计）撰写与印制规范》。

- [规范来源：西南财经大学计算机与人工智能学院](https://it.swufe.edu.cn/info/1166/22938.htm)

提交论文时，请结合学院当年的具体要求检查最终稿。

## 下载发布版本

GitHub **Releases** 中提供两种 ZIP：

| 文件名后缀 | 内容 |
| --- | --- |
| `-with-font.zip` | 模板源码、编译脚本和 `font/` 字体文件，适合希望保留示例字体的用户 |
| `-without-font.zip` | 相同的模板源码和编译脚本，省略 `font/`，自动使用系统字体或 TeX 发行版中的替代字体 |

两个 ZIP 都保留 `main.tex`、`setup.tex`、`config.json`、`refs.bib`、自定义文献样式、`contents/`、`figures/`、使用说明和许可证。`main.tex` 位于 ZIP 根目录，便于解压后本地编译或直接上传 Overleaf。ZIP 不包含 `example.pdf`、编译产物、测试及工作流文件；效果预览可查看仓库中的 [example.pdf](https://github.com/SWUFE-DB-Group/swufe-thesis-bachelor/blob/main/example.pdf)。

## 编译环境与版本要求

本项目已适配 **SJTUTeX 2.3.1（2026-02-26）**，最低要求为该版本，使用 **XeLaTeX** 编译。推荐使用 **TeX Live 2026**；使用其他发行版时，请确认已安装 `sjtutex` 2.3.1 或更新版本，以及 `jsonparse` 等依赖宏包。当前验证环境为 TeX Live 2026 / SJTUTeX 2.3.1；更新版本仍需确认兼容性。

[SJTUTeX 已被 CTAN 收录，并由 TeX Live、MiKTeX 分发](https://ctan.org/pkg/sjtutex)。本项目直接使用发行版中的文档类，不再附带旧版 `texmf/`，无需配置 `TEXINPUTS`。自定义的 `swufe-gbt7714-numerical.bst` 位于项目根目录，BibTeX 可直接查找，无需配置 `BSTINPUTS`。

使用 TeX Live 官方安装器安装的环境，可运行：

```bash
tlmgr update --self
tlmgr install sjtutex jsonparse
tlmgr update sjtutex jsonparse
```

若 TeX Live 由操作系统包管理器安装，请通过对应包管理器更新；MiKTeX 用户可通过 MiKTeX Console 安装和更新宏包。

编译日志开头应显示 `Document Class: sjtuthesis 2026/02/26 v2.3.1 ...` 或更新版本。从旧版项目迁移时，请删除旧的 `texmf/` 和依赖搜索路径设置，避免旧版文档类覆盖发行版版本。模板已迁移到新版的 `abstract` 环境（如 `[lang=zh,notintoc]`）与 `\tableofcontents[notintoc]` 接口；本科论文信息仍使用单套配置字段。

## 模板使用

如果你不熟悉 LaTeX 的编译流程，建议使用下列编译脚本或编辑器配方。本地编译前，请满足上述版本要求，并安装 **BibTeX**、**latexmk** 及模板依赖的宏包。

编译时，`latexmk` 会读取项目根目录的 `.latexmkrc`，使用发行版中的文档类，按需运行 BibTeX，并重复编译以更新目录、引用和页码。请在项目根目录运行命令。

### VS Code 用户

安装 **LaTeX Workshop** 扩展，选择 **Recipe: latexmk (xelatex)** 进行编译，并在 VS Code 设置中将 `latex-workshop.latex.recipe.default` 改为 `lastUsed`，以便后续继续使用该配方：

```json
{
  "latex-workshop.latex.recipe.default": "lastUsed"
}
```

### Linux 与 macOS 用户

推荐使用模板提供的 `Makefile`：

```bash
make all          # 编译生成 main.pdf（也可直接运行 make）
make clean        # 删除编译产生的中间文件，保留 main.pdf
make cleanall     # 删除 main.pdf 和所有中间文件
make wordcount    # 论文字数统计
make pvc          # 监听文件变化并自动编译
```

### Windows 用户

模板提供了 `Compile.bat`，可以双击直接编译，也可以在 PowerShell 或命令提示符中运行：

```powershell
.\Compile.bat thesis       # 编译生成 main.pdf
.\Compile.bat clean        # 删除编译产生的中间文件，保留 main.pdf
.\Compile.bat cleanall     # 删除 main.pdf 和所有中间文件
.\Compile.bat wordcount    # 论文字数统计
```

### 直接使用 latexmk

熟悉命令行的用户也可以执行：

```bash
latexmk -xelatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

### Overleaf 等在线平台

在线编译无需在本机安装 TeX。以 Overleaf 为例：

1. 将项目源文件打包为 ZIP，保留 `main.tex`、`setup.tex`、`config.json`、`refs.bib`、`swufe-gbt7714-numerical.bst`，以及完整的 `contents/`、`figures/` 目录；`font/` 为可选目录，保留它可使用示例中的原字体。
2. 在 Overleaf 中选择 **New Project → Upload Project**，上传 ZIP。确认 `main.tex` 位于项目根目录。
3. 在项目设置中，将 **Main document** 设为 `main.tex`，**Compiler** 设为 **XeLaTeX**，**TeX Live version** 设为 **2026**。该流程直接使用平台提供的 SJTUTeX，无需上传 `texmf/`，也无需创建或重命名 `latexmkrc`；仓库的 `.latexmkrc` 用于本地脚本编译。
4. 修改 `config.json` 和 `contents/` 中的论文内容，点击 **Recompile**，编译完成后下载 PDF。若提示 `SJTUTeX 2.3.1 or newer is required`，请检查 TeX Live 版本，并清除项目中残留的旧文档类。

其他在线平台同样需要满足 SJTUTeX 版本要求，上传项目并选择 XeLaTeX。`font/` 可省略；若提供字体文件，需保留原文件名。

参考 Overleaf 官方文档：[上传项目](https://www.overleaf.com/learn/latex/Kb/Uploading_a_project)、[TeX Live 2026 公告](https://www.overleaf.com/blog/tex-live-2026-is-now-available)、[编译器与 TeX Live 版本](https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler)。

### 字体

模板优先使用 `font/` 中的字体；文件缺失时查找同名系统字体，仍不可用时采用 TeX 发行版中的替代字体。即使整个 `font/` 目录不存在，也能在满足上述依赖要求的环境中编译。

| 项目字体文件 | 用途 | 回退顺序 |
| --- | --- | --- |
| `STZHONGS.TTF` | 封面主标题及一级标题等的华文中宋 | 系统 `STZhongsong` → Fandol 宋体 |
| `STFANGSO.TTF` | 封面信息栏与日期的华文仿宋 | 系统 `STFangsong` → Fandol 仿宋 |
| `Times New Roman*.ttf` | 西文与数字的常规、粗体、斜体、粗斜体 | 系统 Times New Roman → TeX Gyre TermesX |

Times New Roman 的四个文件作为一组加载，缺少任意一个时整组回退。华文中宋与华文仿宋的粗体使用合成加粗，Fandol 宋体使用自带粗体。若提供字体文件，文件名须与配置一致，尤其注意 Linux 下的大小写。

回退到替代字体时，编译日志会给出提示。替代字体与规范指定的原字体存在字形差异：Fandol 宋体并非华文中宋，Fandol 仿宋并非华文仿宋，TeX Gyre TermesX 并非 Times New Roman。需要保持指定字体及示例效果时，请保留项目字体或在系统中安装相应字体。

正文宋体与标题黑体由发行版中的 SJTUTeX 字体方案提供：Windows 默认使用中易宋体、黑体，macOS 默认使用系统中文字体，其他系统默认使用 Fandol 宋体、黑体。

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
├── example.pdf              # 可直接预览的模板示例
├── main.tex                 # 主文档与章节顺序
├── setup.tex                # 元数据读取、字体与版式配置
├── config.json              # 论文信息、盲审开关与引用样式
├── refs.bib                 # 默认的参考文献数据库
├── contents/                # 封面、摘要、正文及其他章节
├── figures/                 # 实际使用的校名、校徽、声明页、封底等素材
├── font/                    # 可选的华文中宋、华文仿宋与 Times New Roman 字体文件
├── swufe-gbt7714-numerical.bst # 中文优先的 GB/T 7714 BibTeX 样式
├── .latexmkrc               # 本地 XeLaTeX / BibTeX 编译配置
├── .gitignore               # 编译产物与编辑器临时文件忽略规则
├── tests/                   # 版本迁移、编译和打包检查
├── scripts/                 # 发布 ZIP 打包脚本
├── .github/workflows/        # tag 触发的 Release 工作流
├── Makefile                 # make 编译入口
├── Compile.bat              # Windows 编译入口
└── LICENSE
```

学术声明与封底分别通过 `contents/学术声明.tex`、`contents/封底.tex` 嵌入 `figures/copyright.pdf` 和 `figures/last.pdf`。这些 PDF 是编译输入，应与源代码一起保留。`example.pdf` 是纳入版本管理的效果示例，修改模板排版后应重新编译并用 `main.pdf` 更新。生成的 `main.pdf` 和编译中间文件由 `.gitignore` 忽略。

## 发布版本

`.github/workflows/release.yml` 在推送任意 tag 时触发，创建对应的 GitHub Release，并上传两个 ZIP。例如：

```bash
git tag v1.0.0
git push origin v1.0.0
```

该示例生成 `SWUFE-Thesis-Bachelor-v1.0.0-with-font.zip` 和 `SWUFE-Thesis-Bachelor-v1.0.0-without-font.zip`。工作流使用内置的 `GITHUB_TOKEN` 和 `contents: write` 权限，无需额外配置令牌；同一 tag 的工作流重跑时，会更新已有 Release 中同名的 ZIP 附件。工作流打包 tag 对应的已跟踪模板文件，不在发布时重新编译论文。

也可在项目根目录本地生成 ZIP：

```bash
python3 scripts/package_release.py v1.0.0
```

文件默认输出到 `build/release/`；可通过 `--output-dir` 指定其他目录。打包要求六个随项目提供的字体文件完整，以确保 `with-font` 包含完整字体组。

## 开发检查

修改模板后可运行：

```bash
python3 -m unittest discover -s tests -v
```

检查需要 Python 3、XeLaTeX、BibTeX、latexmk 和 Poppler（`pdfinfo`、`pdftotext`、`pdftohtml`、`pdffonts`）。编译检查在临时目录中运行，不读取项目的 `.latexmkrc`，验证发行版文档类、JSON 与默认配置、盲审元数据、两种文献来源、字体回退、字体字号、页边距及脚注间距。打包检查另外需要 Git，可单独运行 `python3 -m unittest discover -s tests -p test_release.py -v`，无需安装 TeX。

## 许可与致谢

项目许可证见 [LICENSE](LICENSE)。感谢 [SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 及其所基于的[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 的作者，以及 [gbt7714-bibtex-style](https://github.com/zepinglee/gbt7714-bibtex-style) 的维护者。SJTUTeX 由 TeX 发行版提供；本项目修改后的 BibTeX 样式保留其原有的 LaTeX Project Public License 声明。
