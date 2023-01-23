class QueueError(IndexError): 
    pass

class Queue:
    def __init__(self):
        self.queue=[]

    def put_val(self, val):
        self.queue.insert(0,val)

    def get_val(self):
        if len(self.queue) > 0:
            val = self.queue[-1]
            del self.queue[-1]
            return val
        else:
            raise IndexError
    
class SuperQueue(Queue):
    def __init__(self) :
        Queue.__init__(self)
    
    def isempty(self):
        if len(self.queue) > 0:
            return False
        else:
            True
        
que = SuperQueue()
que.put_val(1)
que.put_val("dog")
que.put_val(False)
for i in range(4):
    if not que.isempty():
        print(que.get_val())
    else:
        print("Queue empty")