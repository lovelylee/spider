import sys
import requests
import json

# 1. 接收命令行传入翻译内容
# print(sys.argv)
word = sys.argv[1]
# 2. 准备请求URL
url = 'http://fy.iciba.com/ajax.php?a=fy'
# 3. 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
# 4. 准备POST请求的数据
data = {
    'f': 'auto',
    't': 'auto',
    'w': word
}

# 5. 发送POST, 获取响应数据
response = requests.post(url, data=data, headers=headers)
# print(response.content.decode())
# json_data = response.content.decode()
# 6. 获取并打印翻译结果
# json => python
# rs = json.loads(json_data)
rs = response.json()

mean = rs['content'].get('word_mean')
if mean:
    print(mean[0])
else:
    print(rs['content']['out'])


"""
{"status":0,"content":{"ph_en":"hə'ləʊ","ph_am":"həˈloʊ","ph_en_mp3":"","ph_am_mp3":"http:\/\/res.iciba.com\/resource\/amp3\/1\/0\/5d\/41\/5d41402ab*屏蔽的关键字*b2a76b9719d911017c592.mp3","ph_tts_mp3":"http:\/\/res-tts.iciba.com\/5\/d\/4\/5d41402ab*屏蔽的关键字*b2a76b9719d911017c592.mp3","word_mean":["int. 哈喽，喂;你好，您好;表示问候;打招呼;","n. “喂”的招呼声或问候声;","vi. 喊“喂”;"]}}

{"status":1,"content":{"from":"zh-CN","to":"en-US","out":"hello","vendor":"ciba","err_no":0}}

"""
