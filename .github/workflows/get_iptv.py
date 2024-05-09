import requests

# 获取直播源链接
url = "https://fanmingming.com/txt?url=https://live.fanmingming.com/tv/m3u/ipv6.m3u"
response = requests.get(url)
playlist = response.text

# 将直播源链接保存到iptv.txt文件中
with open("iptv.txt", "w") as file:
    file.write(playlist)
