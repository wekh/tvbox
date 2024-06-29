import requests

# 获取直播源链接
urls = [
    "https://fanmingming.com/txt?url=https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/wekh/tvbox/main/itv.txt"
]
response = requests.get(url)
playlist = response.text

# 将直播源链接保存到iptv.txt文件中
with open("iptv.txt", "w") as file:
    file.write(playlist)
