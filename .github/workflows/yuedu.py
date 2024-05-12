import requests

# 获取数据
url = "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/XIU2/Yuedu/master/shuyuan"
response = requests.get(url)
data = response.text

# 将数据保存到yuedu.txt文件中
with open("yuedu.txt", "w") as file:
    file.write(data)
