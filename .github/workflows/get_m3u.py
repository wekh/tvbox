import requests

# 定义两个 URL
urls = [
    "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/wekh/tvbox/main/itv.txt"
]

# 打开文件以写入模式
with open("iptv.m3u", "w") as file:
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            playlist = response.text

            # 检查最后一行是否为空行
            if not playlist.endswith('\n'):
                playlist += '\n'

            # 写入 URL 内容
            file.write(playlist)

            print(f"内容已成功从 {url} 保存到 iptv.m3u 文件中")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {url} - {e}")

print("所有内容已处理完毕")
