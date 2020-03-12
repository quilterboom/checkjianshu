import requests
import re
import configparser
from info.Info import dolog
import random

def do_geturl():
    # 从配置文件中读取url
    conf = configparser.ConfigParser()
    conf.read('config.conf',encoding='utf-8')
    url = conf.get('firsturl','url')
    # 设置请求头
    head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400"}
    dolog.info('开始请求页面')
    # 设置代理
    #proxies = [{'https':'59.57.148.67:9999'},{'https':'183.154.52.2:9999'}]
    # 进行请求
    alltxt = requests.get(url,headers=head)
    # 正则匹配
    txt = re.findall(r'title(.*?)href=\"(.*?)\">\S',alltxt.text)

    for i in range(len(txt)):
        newurl = url+txt[i][1]
        dolog.info('解析链接为{}'.format(newurl))
        with open("jianshuurl.txt",mode='a',encoding='utf-8') as f:
            f.write(newurl+'\n')
    dolog.info('输入文件完毕')

if __name__ == '__main__':
    do_geturl()
    do_geturl()