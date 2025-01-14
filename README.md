# README

## 项目名称
文本总结与思维导图生成工具

## 项目描述
本项目提供了一套完整的工具链，用于：
1. 从 Word 文档中提取文本并生成概要内容和思维导图的 JSON 结构。
2. 将生成的 JSON 文件转换为 OPML 文件，用于可视化思维导图。

该工具基于 LangChain 框架、Tongyi LLM 模型以及标准 Python 库进行实现。用户可以通过提供文档快速生成多层次结构化总结，并通过 OPML 格式将数据导入支持的应用（如 MindManager、XMind 等）。


## 功能
### 1. 文本总结与 JSON 思维导图生成
`summary_mindmap_ai.py` 文件负责以下主要功能：
- **文本提取**：从指定的 Word 文档中读取段落内容。
- **语言模型交互**：通过 `LangChain` 框架与 `Tongyi` 模型协作，利用自定义的 Prompt 模板生成结构化文本总结。
- **结果处理**：将生成的内容以 Markdown 格式保存总结，并以 JSON 格式输出思维导图数据，供进一步使用。
- 从指定 Word 文档（.docx 格式）中读取文本内容。
- 利用 Prompt 模板与大语言模型生成文本的结构化总结和 JSON 思维导图。
- 结果以 Markdown 和 JSON 文件保存。

### 2. JSON 转 OPML
- `json_to_opml.py` 文件用于处理 JSON 数据并生成标准 OPML 文件。
- **主要逻辑**：
  - 读取生成的 JSON 文件并解析其多层嵌套结构。
  - 使用递归函数 `build_outline` 将 JSON 中的各级节点映射到 OPML 的 outline 节点。
  - 生成的 OPML 文件具有多层级结构，便于导入主流思维导图软件（如 XMind 和 MindManager）进行可视化。
  - 提供格式化输出功能，使生成的 OPML 文件易于阅读和调试。
- 支持多层级嵌套结构，方便在主流思维导图软件中使用。

## 使用方法

### 环境准备
1. 确保安装了以下依赖：
    - Python >= 3.8
    - 依赖库：
      ```bash
      pip install langchain-core langchain-community docx xml json
      ```
2. 配置 Tongyi LLM：
    - 在 `summary_mindmap_ai.py` 中替换为您自己的 API Key：
      ```python
      api_key="your_tongyi_api_key_here"
      ```

### 文件结构
```
├── summary_mindmap_ai.py    # 文本处理与 JSON 生成脚本
├── json_to_opml.py          # JSON 转 OPML 脚本
├── text_example2.docx       # 示例输入文档
├── summary.md               # 自动生成的文本总结
├── mindmap.json             # 自动生成的 JSON 思维导图
├── output.opml              # 自动生成的 OPML 文件
├── requirements.txt         # 项目依赖
└── README.md                # 项目说明
```

### 使用步骤
1. **运行文本处理脚本**
   运行 `summary_mindmap_ai.py` 提取 Word 文档中的文本并生成总结和 JSON 思维导图：
   ```bash
   python summary_mindmap_ai.py
   ```
   输出文件：
   - `summary.md`：生成的文本总结。
   - `mindmap.json`：生成的 JSON 思维导图。

2. **转换 JSON 为 OPML**
   运行 `json_to_opml.py` 将 JSON 文件转换为 OPML 文件：
   ```bash
   python json_to_opml.py
   ```
   输出文件：
   - `output.opml`：生成的 OPML 文件。

3. **导入到思维导图软件**
   使用支持 OPML 格式的软件（如 XMind、MindManager）导入 `output.opml` 文件，查看生成的思维导图。


## 示例
### 输入
提供的 `text_example2.docx` 文件。

### 输出
- 文本总结（保存在 `summary.md` 文件中）。
- 思维导图 JSON 文件（保存在 `mindmap.json` 文件中）。
- 可视化思维导图（通过 OPML 文件 `output.opml` 导入工具查看）。


## 注意事项
1. 确保输入文档为 `.docx` 格式，其他格式可能导致解析失败。
2. 在 `summary_mindmap_ai.py` 中，替换 `api_key` 为您自己的 Tongyi API 密钥。
3. 输出的 JSON 文件应保存在当前目录下，否则转换脚本可能无法找到输入文件。


## 贡献
欢迎提交 Issues 和 Pull Requests 来改进本项目！


## 许可证
本项目基于 MIT License 开源，请自由使用与分发。

