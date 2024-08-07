import re
import base64
import requests
import json

headers = {'User-Agent': 'okhttp/3.15'}

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

        # 排除注释内容
        content_lines = content.split('\n')
        cleaned_content = [line for line in content_lines if not line.strip().startswith("//")]

        # 合并处理后的内容
        cleaned_content_text = '\n'.join(cleaned_content)

        # 解析内容
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

        # 添加新数据到 "sites" 的开头
        if "sites" in data:
            new_site = {
                "key": "mfys",
                "name": "🍁免费┃不卡",
                "type": 1,
                "api": "https://ys.wekh.eu.org/api.php/provide/vod/",
                "searchable": 1,
                "quickSearch": 1,
                "filterable": 1
            },
            data["sites"].insert(0, new_site)
        else:
            print('"sites" 键不在数据中')

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
