#encoding=utf-8
from core.rock_clustering.heap_oper import my_heap
class rock_queue:
    '''
    堆的实现，包括global_heap 和local_heap,
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
        根据rock_type的id对堆中相应元素进行删除
        :param id:
        :return:
        '''
        if self.rt[id] != None:
            return False ## 堆中没有该对象
        flag = self.rkheap.delete_by_attr(id,'id')
        if flag:
            self.count = self.count -1
            self.rt[id] = None
        return flag

    def insert(self,rkty):
        '''

        :param rkty:
        :return:
        '''
        if self.rt[rkty.id] != None:
            return False



    def update(self,id,gkey):
        '''

        :param id:
        :param gkey:
        :return:
        '''
        pass
