import xml.etree.ElementTree as ET
import json
from xml.dom import minidom


# 格式化OPML内容的函数
def format_opml(opml_element):
    # 使用 minidom 来格式化生成的 XML
    xml_str = ET.tostring(opml_element, encoding='utf-8', xml_declaration=True).decode('utf-8')
    # 使用 minidom 来格式化字符串（加上换行和缩进）
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")
    return pretty_xml_str


def json_to_opml(json_data, title_str):
    opml = ET.Element('opml', version='2.0')
    head = ET.SubElement(opml, 'head')
    title = ET.SubElement(head, 'title')
    title.text = title_str
    body = ET.SubElement(opml, 'body')
    build_outline(body, json_data)
    return opml


def build_outline(parent, data):
    # 如果当前节点有子节点
    if 'children' in data:
        # 遍历每一个子节点
        for item in data['children']:
            outline = ET.SubElement(parent, 'outline', text=item['name'])  # 创建当前节点
            # 如果当前子节点有子节点，则递归调用
            if 'children' in item:
                build_outline(outline, item)  # 递归处理子节点


# 从文件中读取JSON数据
def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
        return None
    except json.JSONDecodeError:
        print(f"文件 {filename} 不是有效的JSON。")
        return None


# 读取mindmap.json文件中的数据
json_filename = 'mindmap.json'
data = read_json_file(json_filename)

# print(data)

# 如果数据读取成功，则生成OPML文件
if data is not None:
    opml_data = json_to_opml(data, '思维导图信息')
    # 使用格式化函数格式化 OPML 文件
    formatted_opml = format_opml(opml_data)

    # 将格式化后的 OPML 内容写入文件
    with open('output.opml', 'w', encoding='utf-8') as f:
        f.write(formatted_opml)
else:
    print("无法生成OPML文件，因为JSON数据无效或文件不存在。")
