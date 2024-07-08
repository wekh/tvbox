import re
import base64
import requests
import json

headers = {'User-Agent': 'okhttp/3.15'}

url = 'http://www.饭太硬.com/tv/'
try:
    # 发送HTTP GET请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果响应状态码不是200，引发异常

    # 使用正则表达式查找匹配项
    match = re.search(r'[A-Za-z0]{8}\*\*(.*)', response.text)
    
    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        # 提取并解码base64编码的内容
        result = match.group(1)
        content = base64.b64decode(result).decode('utf-8')

        # 打印解析后的内容（调试用）
        print("解析后的内容：")
        print(content)

        # 排除注释内容
        content_lines = content.split('\n')
        cleaned_content = [line for line in content_lines if not line.strip().startswith("//")]

        # 合并处理后的内容
        cleaned_content_text = '\n'.join(cleaned_content)

        # 解析JSON内容
        data = json.loads(cleaned_content_text)

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
except json.JSONDecodeError as je:
    print("JSON解析失败:", je)
except base64.binascii.Error as be:
    print("Base64解码失败:", be)
except Exception as ex:
    print("发生错误:", ex)
