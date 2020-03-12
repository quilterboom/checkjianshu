from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from geturl import do_geturl
import os
from info.Info import dolog


class ClickJianShu:
    def __init__(self):
        self.webdr = webdriver.Chrome()
        self.webdr.maximize_window()
        self.wait = WebDriverWait(self.webdr, 10)

    def click_icon(self,url):
        time_name = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        picname = '{}.png'.format(time_name)
        picallname = os.path.join('./info/scpic', picname)
        zanxpath =  '//div[@class="_1pUUKr"]/div[@class="_2VdqdF" and @aria-label="给文章点赞"]'
        self.webdr.get(url)
        pic1 = self.webdr.save_screenshot(picallname)
        dolog.info('截图路径{},截图状态{}'.format(picallname,pic1))
        try:
            zanicon = self.wait.until(ec.presence_of_element_located((By.XPATH, zanxpath)))
            zanicon.click()
        except Exception as e:
            dolog.error('可能已点击过赞,错误信息为{}'.format(e))

    def do_click(self):
        with open('jianshuurl.txt', mode='r', encoding='utf-8') as f:
            a = f.readlines()
        for i in range(len(a)):
            dolog.info('执行链接为{}'.format(a[i]))
            url = a[i]
            self.click_icon(url)
        dolog.info('执行完毕')
        dolog.info('关闭浏览器')
        self.webdr.quit()
        dolog.info('执行删除文件操作')
        os.remove(os.path.join(os.path.dirname(__file__), 'jianshuurl.txt'))
        dolog.info('删除完毕')


    def begin_do(self):
        self.webdr.get('https://www.jianshu.com')
        dolog.info('打开简书页面')
        try:
            loadicon = "//a[contains(text(),'登录')]"
            self.wait.until(ec.presence_of_element_located((By.XPATH,loadicon))).click()
        except Exception as e:
            dolog.error('找不到登录icon，错误信息为{}'.format(e))
        try:
            weixinicon = '//i[@class="iconfont ic-wechat"]'
            self.wait.until(ec.presence_of_element_located((By.XPATH,weixinicon))).click()
        except Exception as e:
            dolog.error('找不到微信icon，错误信息为{}'.format(e))
        # 等到手机扫码
        #isture = 1
        isture = input('扫码后关闭当前页面，确认是否准备就绪 1是ok，其他未准备关闭页面')
        #print(isture)
        #time.sleep(5)
        if isture == '1':
            window = self.webdr.window_handles
            self.webdr.switch_to.window(window[-1])
            self.webdr.close()
            window = self.webdr.window_handles
            self.webdr.switch_to.window(window[-1])
            for i in range(3):
                self.webdr.refresh()
            time.sleep(1)
            if os.path.exists(os.path.join(os.path.dirname(__file__),'jianshuurl.txt')):
                #如果存在执行do_click
                dolog.info('执行do_click')
                self.do_click()
            else:
                # 加载文件,多次请求
                dolog.info('不存在文件，进行多次请求')
                for i in range(3):
                    dolog.info(f'循环第{i}次')
                    time.sleep(400)
                    dolog.info('结束等待')
                    do_geturl()
                dolog.info('开始执行do_click')
                self.do_click()
        else:
            print('关闭浏览器')
            self.webdr.quit()