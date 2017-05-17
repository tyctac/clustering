#encoding=utf-8
class LINK:
    def __init__(self,linkNum,setN,sets,Length,k):
        self.linkNum = linkNum
        ## self.linkNum may have problems
        self.len = Length + Length -k ## k is the number of cluster
        self.setN = []
        self.sets = []
        for i in range(len):
            setN.append(1)
            sets.append(i)
        self.len = Length
        self.now = self.len