import requests

# 定义两个 URL
urls = [
    "https://fanmingming.com/txt?url=https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/wekh/tvbox/main/itv.txt"
]

# 打开文件以写入模式
with open("iptv.txt", "w") as file:
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            playlist = response.text

            # 写入 URL 内容
            file.write(playlist + "\n\n")  # 加两个换行符作为分隔符

            print(f"内容已成功从 {url} 保存到 iptv.txt 文件中")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {url} - {e}")

print("所有内容已处理完毕")
