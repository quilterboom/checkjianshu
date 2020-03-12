import logging
import time
import os

class loginfo:
    def __init__(self):
        time_name = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        filename = '{}.log'.format(time_name)
        fileallname = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),'info'),filename)
        self.log = logging.getLogger('jianshulog')
        self.log.setLevel(logging.DEBUG)
        file_hand = logging.FileHandler(fileallname,encoding='utf-8')
        file_hand.setLevel(logging.DEBUG)
        simple = logging.Formatter('%(asctime)s-[%(levelname)s]-[%(message)s]')
        file_hand.setFormatter(simple)
        self.log.addHandler(file_hand)

    def logg(self):
        return self.log

dolog = loginfo().logg()

if __name__ == '__main__':
    dolog.info('asda')
    dolog.debug('das')

