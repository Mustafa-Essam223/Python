from queuee import *
from queuee2 import *
q=Queue()
# q.__str__()
q.insert(5)
q.insert(15)
q.insert(25)
q.insert(35)

while not q.isempty():
    print(f"front = {q.front()}")
    q.popp()


q1=Queue2('first',3)
q2=Queue2('second',3)
q1.__str__()
q1.insert(3)
q1.insert(6)
q1.insert(9)
# q1.insert(12)

print("--",q1.length())
print("--",q1.isempty())

print("==========================")
Queue2.track_all_queues()
print("==========================")
Queue2.save()
print("==========================")
Queue2.load()
