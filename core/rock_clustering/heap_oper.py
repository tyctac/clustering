#encoding=utf8
from core.rock_clustering import main_class
import heapq
import random
class my_heap:
    def __init__(self,initial=None,key = lambda x:x): ## 可以通过key来实现比较函数吗？？？
        # self.k = 20 # the size of this heap , i think it is useless in our problem
        self.key = key
        self._data = []

    def push(self,item):
        '''
        自定义 push
        :param elem:
        :return:
        '''
        ## old
        # if len(self.data) < self.k:
        #     heapq.heappush(self.data.elem)
        # else:
        heapq.heappush(self._data,(self.key(item),item)) ##
        ## --->> 关键特性
        ## 这么做能成功的原因是不是因为： tuple 默认是比较第零个元素 呢？？，就相当于是key，
        ## 这样就可以实现自定义的比较函数了吧，方法，
        ##　将比较函数值放在tuple的第一个元素，比较对象在tuple 的第二个对象， 原来如此啊

    def pop(self):
        '''
        pop define by myself
        :return:
        '''
        if(len(self._data) > 1):
            return heapq.heappop(self._data)[1]
        else:
            return None

## test
def main():
    testlist = []
    num = 100
    myhp = my_heap(key = lambda item: -item.gkey)
    for i in range(100):
        id = random.randint(0,100)
        gkey = random.randint(0,100)
        myhp.push(main_class.rock_type(id,gkey))
    for i in range(20):
        j = myhp.pop()
        if(j != None):
            print str(j.gkey) + '\t' + str(j.id)

if __name__ == '__main__':
    main()
    print 'ok!! '


