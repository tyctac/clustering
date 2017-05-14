#encoding=utf-8
from utils import levenshtein_distance,config
class Domain_sim():
    def __init__(self,s1,s2):
        self.domain1 = s1
        self.domain2 = s2

    def name_similarity(self):
        return levenshtein_distance.get_ld(self.domain1,self.domain2)

    def reg_person_similarity(self):
        '''
        注册人信息的相似度，如何计算
        :return:
        '''
        if self.domain1.reg_name == self.domain2.reg_name:
            return 1 * config.get_reg_person_weight()

    def reg_date_similarity(self):
        '''
        时间相似性指标：
        这里使用两者之间的间距，
        使用两年的时间归一化
                先弄清楚格式再写代码
        :return:
        '''
        pass

