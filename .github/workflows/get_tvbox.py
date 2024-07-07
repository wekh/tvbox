import re
import base64
import requests
import json

headers = {'User-Agent': 'okhttp/3.15'}

def fix_json(json_str):
    # 使用正则表达式查找未用双引号括起来的属性名，并自动添加双引号
    fixed_json_str = re.sub(r'(?<=\{|,)\s*([a-zA-Z_][a-zA-Z0-9_-]*)\s*:', r'"\1":', json_str)
    return fixed_json_str

def remove_comments(json_str):
    # 使用正则表达式移除单行注释
    return re.sub(r'//.*', '', json_str)

def clean_json(json_str):
    # 移除注释
    json_str = remove_comments(json_str)
    # 修复未用双引号括起来的属性名
    json_str = fix_json(json_str)
    return json_str

url = 'http://www.饭太硬.com/tv/'
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 抛出异常，处理错误的响应状态

    # 使用正则表达式查找匹配项
    match = re.search(r'[A-Za-z0]{8}\*\*(.*)', response.text)
    
    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        result = match.group(1)
        content = base64.b64decode(result).decode('utf-8')

        # 调试输出解析后的内容
        print("解析后的内容：")
        print(content)

        # 清理JSON字符串
        cleaned_content_text = clean_json(content)

        try:
            # 尝试解析内容
            data = json.loads(cleaned_content_text)
        except json.JSONDecodeError as e:
            print("JSON解析失败，尝试自动修复...")
            # 尝试自动修复JSON字符串
            fixed_content_text = fix_json(cleaned_content_text)
            try:
                data = json.loads(fixed_content_text)
                print("自动修复成功!")
            except json.JSONDecodeError as ex:
                print("自动修复失败:", ex)
                raise ex

        # 修改内容
        data["lives"] = [
            {
                "name": "IPV6",
                "type": 0,
                "url": "https://tv.wekh.top/iptv.txt",
                "playerType": 1,
                "ua": "okhttp/3.15"
            }
        ]

        # 将修改后的内容转换为 JSON 字符串，并指定 ensure_ascii=False 以确保汉字和表情符号正常显示
        modified_content = json.dumps(data, indent=2, ensure_ascii=False)

        # 将修改后的 JSON 字符串写入 tvbox.txt 文件中
        with open('tvbox.txt', 'w', newline='', encoding='utf-8') as f:
            f.write(modified_content)

        print("修改后的内容已写入到 tvbox.txt 文件中。")

except requests.RequestException as e:
    print("请求失败:", e)
except Exception as ex:
    print("发生错误:", ex)
