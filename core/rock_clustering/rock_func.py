#encoding=utf-8
from core.rock_clustering import heap_oper,rock_queue,rock_type,LINK

class rock_func:
    @staticmethod
    def compute_linknum(u,len,k):
        '''
        根据邻居矩阵u计算共同连接数对象LINK
        :param u: 邻居矩阵
        :param len:
        :param k:
        :return:
        '''
