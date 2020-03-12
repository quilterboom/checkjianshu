from click_zan import ClickJianShu
import time

def get_time(func):
    def wapper():
        one = time.clock()
        func()
        two = time.clock()
        end = two-one
        print("最后耗时{}".format(end))
    return wapper()

@get_time
def bg():
    ClickJianShu().begin_do()


if __name__ == '__main__':
    bg