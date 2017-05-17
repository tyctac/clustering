#encoding=utf-8
from core.rock_clustering.heap_oper import my_heap
from core.rock_clustering.rock_type import rock_type
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
        self.rt = rt  ## rt 中存放的应该是rk_heap._data中对应的索引id, 堆需要重新设计,....,这样才能在线性甚至是对数时间进行删除和更新操作
        ## 当前rt 可以用来判断是否存在和是否需要更新,如果rt[id]==None,则不存在
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

    def update(self, id, gkey):
        '''
        :param id:
        :param gkey:
        :return:
        '''
        if self.rt[id] == None:
            return False ##
        self.delete(id)
        rkty = rock_type(id,gkey)
        self.insert(rkty)


    def insert(self,rkty):
        '''

        :param rkty:
        :return:
        '''
        if self.rt[rkty.id] != None:
            return False ## already exist
        self.rt[rkty.id] == rkty
        self.rkheap.push(rkty)
        self.count += 1

    def insert_new_obj(self,id,gkey):
        rkty = rock_type(id,gkey)
        self.insert(rkty)

    def extract_max(self):
        '''
        get max gkey rkty
        :return:
        '''
        if self.count == 0:
            return -1 ## 堆已空,返回-1
        rk = self.rkheap.pop()
        self.rt[rk.id] = None
        self.count -= 1
        return rk

    def getMax(self):
        '''
        peek max gkey rkty
        :return:
        '''
        if self.count == 0:
            return -1 ## heap already empty
        return self.rkheap.peek_top()





if __name__ == '__main__':
    print 'hello'