class HashOpenAddr:
    def __init__(self,size, k):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
        

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]


    def find_slot(self,key):
        i = self.hash_function(key)
        start = i
        while ( self.keys[i] != None ) and (self.keys[i] != key):
            i = ( i + 1 ) % self.size
            if (i == start ): return
        return i

    def set(self,key, value=None):
        i = self.find_slot(key)
        if i == None: return None
        if self.keys[i] == None:
            self.keys[i] = key
            self.values[i] = value
            return key
        else:
            self.values[i] = value
            return key 
    def hash_function(self,key):
        return key % self.size

    def remove(self,key):
        i = self.find_slot(key)
        if self.keys[i] == None:
            return 

        j = i
        while True:
            self.keys[i] = None
            self.values[i] = None
            while True:
                j = (j+1) % self.size
                if self.keys[j] == None:
                    return key
                k = self.hash_function(self.keys[j])

                if not( i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j] 
            self.values[i] = self.values[j]
            i = j
        return key

    def search(self,key):
        i = self.find_slot(key)
        if self.keys[i] != None:
            return key
        else:
            return

    def __getitem__(self,key):
        return self.search(key)

    def __setitem__(self,key,value):
        self.set(key, value)

    def find_pair(self,k):
        sum = 0
        target = int(k)
        for i in self:
            if i == None:
                continue
            first = int(i)
            for j in self:
                if j == None:
                    continue
                second = int(j)
                if ( first == (target - second) and first != second):
                    self.remove(first)
                    self.remove(target)
                    sum += 1
        return sum

k = input()
n = input()
n = n.split(' ')
for i in range(len(n)):
    if(n[i] is ''):
        n.pop(i)
        
size = int(1.5 * len(n))
H = HashOpenAddr(size,k)
for i in n:

    a = int(i,base=10)
    val = a
    H.set(val)
sum = H.find_pair(k)
print(sum)
