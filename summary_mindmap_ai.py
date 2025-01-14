from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_community.llms.tongyi import Tongyi
from langchain_core.output_parsers import StrOutputParser
from docx import Document
import re

# 初始化 Tongyi LLM
tongyi_qwenplus_llm = Tongyi(model="qwen-plus", api_key="api-key")

# 定义 Prompt 模板
prompt_template = '''请根据下面的文本，完成两项任务：  
1、根据文本生成概括内容，输出示例：  

### 标题  
**[自动生成文本标题]**  

### 关键字  
- [关键字1]  
- [关键字2]  
- [关键字3]  
- ...  

### 摘要
(要求：判断所给文本的字数，如果文本字数在2000之内，则生成50-100字的摘要；大于2000字，生成200-300字的摘要。)  
[根据文本内容生成50-100字的摘要，简要概括核心内容和结论。例如：  
“本文探讨了AI与中国人力资源管理的融合，分析了政策支持、技术创新及企业实践。研究表明，AI技术在招聘、绩效评估等领域取得显著进展，但同时面临隐私与伦理挑战。”]  

### 1. 引言  
- 提供清晰的开篇陈述，概括文本的主要主题或核心思想。  
- 结合文本的目的、范围或重点，提供必要背景信息。  
- **示例**：“本文分析了AI与中国人力资源领域的融合，重点关注政策支持、技术创新以及企业需求的变化。”  

### 2. 关键点  
#### 2.1 背景信息  
- 简要描述推动研究或讨论的背景、动因（例如政策变化、社会趋势或技术进步）。  
  - **示例**：“中国政府通过‘新一代人工智能发展规划’等政策推动AI发展，旨在促进数字化和智能化人力资源管理。”  

#### 2.2 核心部分  
- 按照主题类别或章节组织主要观点，保持逻辑性并突出关键细节：  
  - **主题划分**：  
    - *行业生态*：说明基础层（如基础设施、软件和应用层）的角色及作用。  
    - *技术应用*：涵盖招聘、员工关系、绩效管理等具体案例。  
  - **支持证据**：通过数据、示例或案例研究增加深度和权威性。  
    - **示例**：某技术的实施使企业招聘效率提升30%。  

#### 2.3 分析与见解（可选）  
- 提取文本中的深层次分析或前瞻性见解：  
  - **示例**：“AI驱动的绩效评估显著减少了人为偏见，有助于提升员工满意度和决策透明度。”  

### 3. 结论  
- 总结作者的主要结论和探讨的影响：  
  - **示例**：“本文通过呼吁企业采用全面的AI策略，强调技术应用与以人为本的组织文化之间的平衡。”  
- 包括任何实际建议或可操作性方案（如适用）。  

### 4. 相关性与趋势（可选）  
- 强调文本与更广泛趋势或当前发展之间的联系：  
  - **示例**：“本文反映了全球向AI驱动组织管理转型的趋势，并揭示了其在应对经济不确定性中的潜在价值。”  

### 强有力总结的特点(参考就好了，不需要呈现出来)  
1. **简洁但详实**：突出核心要点，同时提供足够背景和支持细节。  
2. **逻辑结构清晰**：各部分层次分明，便于理解。  
3. **客观性**：避免个人观点或偏见，注重中立性。  
4. **全面性**：涵盖所有重要内容，避免遗漏关键信息。  

---  

2、根据你输出的总结，生成一段 JSON 格式的思维导图结构模板，只保留 JSON，其他什么都不需要，不需要任何解释与前后提示语，请把各个分支写的详细一些，而且要写关键词和摘要，统一是"name""children"的形式，请参考下面的案例，不要使用别的单词。还有，第一个"name"是无效成分，请你保留为"无效"，你总结的内容应该放在第一个"children"后面。JSON 应该包含以下结构：  

### **JSON模板输出格式** 
{{
  "name": "无效",
  "children": [
    {{
      "name": "主题",
      "children": [
        {{
          "name": "标题与关键字",
          "children": [
            {{
              "name": "标题",
              "children": [
                {{
                  "name": "示例标题",
                  "children": []
                }}
              ]
            }},
            {{
              "name": "关键字",
              "children": [
                {{
                  "name": "关键字1",
                  "children": []
                }},
                {{
                  "name": "关键字2",
                  "children": []
                }},
                {{
                  "name": "关键字3",
                  "children": []
                }}
              ]
            }}
          ]
        }},
        {{
          "name": "引言",
          "children": [
            {{
              "name": "核心主题",
              "children": [
                {{
                  "name": "核心观点",
                  "children": []
                }}
              ]
            }},
            {{
              "name": "背景信息",
              "children": [
                {{
                  "name": "背景要点1",
                  "children": []
                }},
                {{
                  "name": "背景要点2",
                  "children": []
                }}
              ]
            }}
          ]
        }},
        {{
          "name": "关键点",
          "children": [
            {{
              "name": "背景与背景信息",
              "children": [
                {{
                  "name": "动因1",
                  "children": []
                }},
                {{
                  "name": "动因2",
                  "children": []
                }}
              ]
            }},
            {{
              "name": "核心部分",
              "children": [
                {{
                  "name": "部分1",
                  "children": [
                    {{
                      "name": "详细信息1",
                      "children": []
                    }},
                    {{
                      "name": "详细信息2",
                      "children": []
                    }}
                  ]
                }},
                {{
                  "name": "部分2",
                  "children": [
                    {{
                      "name": "子部分1",
                      "children": []
                    }},
                    {{
                      "name": "子部分2",
                      "children": []
                    }}
                  ]
                }}
              ]
            }},
            {{
              "name": "分析与见解",
              "children": [
                {{
                  "name": "见解1",
                  "children": []
                }},
                {{
                  "name": "见解2",
                  "children": []
                }}
              ]
            }}
          ]
        }},
        {{
          "name": "结论与建议",
          "children": [
            {{
              "name": "主要结论",
              "children": []
            }},
            {{
              "name": "建议",
              "children": [
                {{
                  "name": "建议1",
                  "children": []
                }},
                {{
                  "name": "建议2",
                  "children": []
                }}
              ]
            }}
          ]
        }},
        {{
          "name": "相关性与趋势",
          "children": [
            {{
              "name": "趋势1",
              "children": []
            }},
            {{
              "name": "趋势2",
              "children": []
            }}
          ]
        }}
      ]
    }}
  ]
}}

文本:{text} \n python代码:'''

# 初始化 Prompt
prompt = PromptTemplate(input_variables=["text"], template=prompt_template)

# 创建链式调用
llm = tongyi_qwenplus_llm
chain = prompt | llm | StrOutputParser()

# 读取文档并提取文本内容
filename = 'text_example2.docx'
doc = Document(filename)

input_text = ''
for para in doc.paragraphs:
    input_text += para.text

# 调用链式处理
code = chain.invoke({"text": input_text})

# 正则表达式匹配输出的内容
pattern1 = re.compile(r'### 标题\s*\n([\s\S]*?)\n---', re.DOTALL)
pattern2 = re.compile(r'```json\s*\n(.*\S*)\s*```', re.DOTALL)

# 获取匹配内容
pattern1_content = None
pattern2_content = None

match1 = pattern1.search(code)
if match1:
    pattern1_content = match1.group(1).strip()

match2 = pattern2.search(code)
if match2:
    pattern2_content = match2.group(1).strip()

# 输出匹配内容
if pattern1_content:
    print("pattern1 内容:")
    print(pattern1_content)

if pattern2_content:
    print("\npattern2 内容:")
    print(pattern2_content)

# 保存到文件
filename1 = "summary.md"
if pattern1_content:
    with open(filename1, "w", encoding='utf-8') as f:
        f.write(pattern1_content)
    print(f"已保存到文件: {filename1}")

filename2 = "mindmap.json"
if pattern2_content:
    with open(filename2, "w", encoding='utf-8') as f:
        f.write(pattern2_content)
    print(f"已保存到文件: {filename2}")

