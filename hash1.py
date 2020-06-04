class HashOpenAddr:
    def __init__(self, size = 10):
        self.size = size
        self.keys = [None]* self.size
        self.values = [None]* self.size

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = f(key)
        start = i
        while ( H[i] is occupied )
    def set(self, key , value = None):

    def hash_function(self,key):
        return key % self.size

    def remove(self,key):

    def search(self,key):

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key,value)

H = HashOpenAddr()
while True:
    cmd  = input().split()
