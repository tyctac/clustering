# encoding=utf8
from core.rock_clustering.heap_oper import my_heap
class rock_type:
    def __init__(self,id,gkey):
        self.id = id
        self.gkey = gkey

    def compare_func(self,):
        '''
        先不管比较函数，实现堆的时候再说
        :return:
        '''
        pass

class rock_queue:
    '''
    堆的实现，包括global_heap 和local_heap
    '''
    def __init__(self,rt,id,count=0,rk_heap=my_heap(key=lambda x:-x.gkey)): ## todo
        # 有默认值的参数要放在最后面
        '''
        构造函数
        :param ptree:核心数据结构，是一个平衡二叉堆
        :param rt:  用来标记以值为id的rock_type对象是否在堆中
        :param id:  TODO
        :param count: TODO
        '''
        self.rkheap = rk_heap
        self.rt = rt
        self.id = id
        self.count = count

    def capacity(self):
        return len(self.rt)

    def delete(self,id):
        '''

        :param id:
        :return:
        '''