class Queue:
    que = []
    def __init__(self):
        self.que=[]

    def __str__(self):
        print('queue instance---')
    def insert(self,newValue):
        self.que.append(newValue)
    def front(self):
        if len(self.que)!=0:
            return self.que[0]
        else:
            raise Exception("Queue is empty")
    def popp(self):
        if len(self.que)==0:
            raise Exception('Queue is empty')
        else:
            self.que.pop(0)
    def length(self):
        return len(self.que)
    def isempty(self):
        return len(self.que)==0


