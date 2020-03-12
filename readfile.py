# import os
# a = os.path.dirname(__file__)
# c=os.path.join(a,'jianshuurl.txt')
# print(c)
# os.remove(c)

# a = os.path.exists(os.path.join(os.path.dirname(__file__),'jianshuurl.txt'))
# print(a)
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#
# print(os.path.join(os.path.dirname(__file__),'info'))

# import time
#
# def get_time(func):
#     def wapper():
#         one = time.clock()
#         func()
#         two = time.clock()
#         end = two-one
#         print("最后耗时{}".format(end))
#     return wapper()
#
# @get_time
# def test1():
#     for i in range(100):
#         print(1)
#
# if __name__ == '__main__':
#     test = get_time(test1)
#     test()
#
# import time
# import os
# time_name = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
# picname = '{}.png'.format(time_name)
# picallname = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'info'),'scpic'), picname)
# print(picallname)

# import requests
#
# #获取当前访问使用的IP地址网站
# url="http://www.ipip.net/"
#
# #设置代理，从西刺免费代理网站上找出一个可用的代理IP
# head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400"}
# proxies={'http':'27.152.8.66:9999'} #此处也可以通过列表形式，设置多个代理IP，后面通过random.choice()随机选取一个进行使用
#
# #使用代理IP进行访问
# res=requests.get(url,headers=head,proxies=proxies,timeout=10)
# status=res.status_code # 状态码
# print(status)
# content=res.text
# print(content)
