# 西南财经大学本科毕业论文 LaTeX 模板

用于撰写西南财经大学本科生毕业论文（设计），包含封面、学术声明、中英文摘要、目录、正文、参考文献、附录、致谢和封底。

本项目基于 [SWUFE-DB-Group/SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 修改，该项目又基于[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 修改。底层使用 SJTUTeX 的 `sjtuthesis` 文档类，本项目在 `setup.tex` 中配置西南财经大学本科论文的版式与论文信息。

## 规范来源

排版依据为《西南财经大学本科生毕业论文（设计）撰写与印制规范》。

- [规范来源：西南财经大学计算机与人工智能学院](https://it.swufe.edu.cn/info/1166/22938.htm)

提交论文时，请结合学院当年的具体要求检查最终稿。

## 编译

需要安装包含 **XeLaTeX** 和 **latexmk** 的 TeX 发行版，以及 `ctex`、`fontspec`、`xeCJK`、`jsonparse`、`newtx`、`tikz`、`pgfplots` 等依赖。使用较新的完整 TeX Live 可减少缺少宏包的问题。

在项目根目录执行：

```bash
latexmk -xelatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

生成文件为 `main.pdf`。`latexmk` 会读取 `.latexmkrc`，自动设置本地 `texmf/` 的搜索路径，并按需重复编译以更新目录、引用和页码。

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

1. 将项目源文件打包为 ZIP，保留 `main.tex`、`setup.tex`、`config.json`、`.latexmkrc`，以及完整的 `contents/`、`figures/`、`font/`、`texmf/` 目录。
2. 在 Overleaf 中选择 **New Project → Upload Project**，上传 ZIP。确认 `main.tex` 位于项目根目录。
3. 在在线项目根目录，将 `.latexmkrc` 重命名为 **`latexmkrc`**（去掉开头的点），保留其内容，使平台能够加载本地 `texmf/` 中的文档类和配置。
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

## 填写论文信息

优先修改根目录的 `config.json`。其中的非空字段会覆盖 `setup.tex` 的默认值；JSON 字符串中的 LaTeX 反斜杠需要写成 `\\`。

| 字段 | 用途 |
| --- | --- |
| `review` | 是否启用盲审模式，取 `true` 或 `false` |
| `citation_superscript` | 文献引用是否使用上标；默认 `false`（非上标），设为 `true` 启用上标 |
| `info.title.zh` / `info.title.en` | 中英文完整论文标题 |
| `info.title.display_zh` | 封面题目的第一行；留空则使用完整中文标题 |
| `info.title.display_zh_line2` | 封面题目的第二行；留空则只显示一行 |
| `info.author.zh` / `info.author.en` | 中英文作者姓名 |
| `info.student_id` | 学号，建议保留为字符串 |
| `info.department.zh` / `info.department.en` | 学院名称 |
| `info.major.zh` / `info.major.en` | 专业名称 |
| `info.grade` | 年级，如 `2022级` |
| `info.supervisor.zh` / `info.supervisor.en` | 导师姓名及职称 |
| `info.final_date` | 封面日期，如 `2026年5月` |
| `info.keywords.zh` / `info.keywords.en` | 中英文关键词 |

例如，封面题目需要分成两行时，可设置：

```json
"title": {
  "zh": "面向金融数据的风险识别方法研究",
  "en": "Risk Identification Methods for Financial Data",
  "display_zh": "面向金融数据的",
  "display_zh_line2": "风险识别方法研究"
}
```

这是 `info.title` 对象的示例，替换 `config.json` 中对应的对象即可。封面每行的下划线宽度为 9cm，长标题应通过这两个字段合理拆分。

将 `review` 设为 `true` 时，封面隐藏姓名、学号和导师信息，并跳过致谢页。正文、插图等自行填写的个人信息仍需检查。

## 撰写正文与参考文献

在 `contents/` 中修改各章内容；增加或删除章节时，同步调整 `main.tex` 中的 `\input{...}`。`contents/格式与规范指南.tex` 提供表格、插图、公式、脚注、算法和代码的示例。

图表格式由 `setup.tex` 统一设置：

- 图题、表题均为五号黑体加粗，居中，前后各空半行。
- 表格的 `\caption` 写在表格内容之前，插图的 `\caption` 写在图片之后。
- 图表内容为五号字体、单倍行距，无需在每个浮动体中重复设置。

外部图片中已经绘制的文字需要在制图软件中设置字号；LaTeX 的字体设置只作用于其排版的文字。

参考文献在 `contents/参考文献.tex` 中使用 `thebibliography` 和 `\bibitem` 手工维护，通过 `\cite{文献键}` 引用。当前模板不使用 `.bib` 数据库，也不需要额外运行 BibTeX 或 Biber。

正文引用默认使用非上标的方括号数字。若需上标引用，在 `config.json` 中将 `citation_superscript` 设为 `true`；该字段省略或设为 `false` 时均使用非上标。引用命令保持一致，例如：

```latex
分类与回归等机器学习方法为模型构建提供了基础\cite{西瓜书}。
相关概念和训练方法可参考教材\cite{西瓜书,深度学习图书}。
网络结构设计可参考残差连接与批归一化方法\cite{ResNet,BatchNormalization}。
残差网络、注意力机制与自适应优化可联合引用\cite{ResNet,Transformer,Adam}。
```

花括号中的文献键须与 `\bibitem{文献键}` 一致，多篇文献用逗号分隔。模板会自动按文献编号排序，两个编号用逗号分隔（如 `[1,2]`），三个及以上连续编号合并为横线连接的范围（如 `[7–9]`），不连续编号仍用逗号分隔（如 `[7,10]`）。这些规则同时适用于非上标和上标引用。绪论提供了单篇及多篇中文文献的引用示例，系统设计章节提供了英文文献及连续编号合并的示例。

脚注使用 `\footnote{说明文字}` 插入。`setup.tex` 中的 `fnmark-style=plain` 将正文标记设为普通阿拉伯数字上标，`footmisc` 的 `perpage` 选项使每页从 1 开始编号。同一章的不同页面及下一章均提供了脚注示例；使用 `latexmk` 编译可自动完成逐页编号所需的多遍处理。

## 项目结构

```text
.
├── main.tex                 # 主文档与章节顺序
├── setup.tex                # 元数据读取、字体与版式配置
├── config.json              # 论文信息、盲审开关与引用样式
├── contents/                # 封面、摘要、正文及其他章节
├── figures/                 # 实际使用的校名、校徽、声明页、封底等素材
├── font/                    # 华文中宋、华文仿宋与 Times New Roman 字体文件
├── texmf/                   # 本地 SJTUTeX 论文文档类及其配置
├── .latexmkrc               # 编译引擎与本地依赖搜索路径
├── .gitignore               # 编译产物与编辑器临时文件忽略规则
├── Makefile                 # make 编译入口
├── Compile.bat              # Windows 编译入口
└── LICENSE
```

学术声明与封底分别通过 `contents/学术声明.tex`、`contents/封底.tex` 嵌入 `figures/copyright.pdf` 和 `figures/last.pdf`。这些 PDF 是编译输入，应与源代码一起保留。生成的 `main.pdf` 和编译中间文件由 `.gitignore` 忽略。

## 许可与致谢

项目许可证见 [LICENSE](LICENSE)。感谢 [SWUFE-Thesis](https://github.com/SWUFE-DB-Group/SWUFE-Thesis) 及其所基于的[上海交通大学论文模板 SJTUThesis](https://github.com/sjtug/SJTUThesis) 的作者。本地 SJTUTeX 文件保留其原有的 LaTeX Project Public License 声明。
