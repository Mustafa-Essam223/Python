from queuee import *


class Queue2(Queue):
    ques_names = []
    ques_sz = []

    def __init__(self,name,size):
        super(Queue2,self).__init__()
        self.name=name
        self.size=size
        
        Queue2.ques_names.append(name)
        Queue2.ques_sz.append(size)
    
    def __str__(self):
        print(f"queue 2 instance: {self.name} with size {self.size} ")
    
    def insert(self,newValue):
        if len(self.que)+1 > self.size:
            raise Exception('Limited Size')
        else: 
            self.que.append(newValue)
    @staticmethod
    def track_all_queues():
        print("All created queues:\n",Queue2.ques_names)
        print("All created queues sizes:\n",Queue2.ques_sz)
        
        
    @staticmethod
    def save():
        qus_file=open("all_qus.txt",'r+')
        for i in range(len(Queue2.ques_names)):
            qus_file.writelines(f"Queue{i+1}-- name :{Queue2.ques_names[i]} size :{Queue2.ques_sz[i]}\n")
        qus_file.close()
    @staticmethod
    def load():
        qus_file=open("all_qus.txt",'r+')
        lines=qus_file.readlines()
        for line in lines:
            print(line,end="")
        qus_file.close()    







