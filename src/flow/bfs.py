

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.queue[0]
            if len(self.queue) == 1:
                self.queue = []
            else:
                self.queue = self.queue[1:]    
        except:
            pass

        return val

    def isEmpty(self):
        result = False
        if len(self.queue) == 0:
            result = True
        return result
    
def BFS(graph,start,end,q):
    '''Breadth-First-Search'''
    temp_path = [start]

    q.enqueue(temp_path)

    while not q.isEmpty():
        tmp_path = q.dequeue()
        
        last_node = tmp_path[len(tmp_path)-1]
        
        print tmp_path
        if last_node == end:
            print "VALID_PATH : ",tmp_path
            
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                #new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)

