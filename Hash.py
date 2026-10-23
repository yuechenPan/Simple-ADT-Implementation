class Deleted_Me:
    def __init__(self):
        self.name = "DM"

DM = Deleted_Me()

def hash_1(k,i,m):
    return (k + i - 1) % m

class Open_Address:

    def __init__(self):
        self.m = 1 #table size
        self.array = [None]
        self.n = 0 #elements in table currently

    def insert(self,k):
        #check load factor and implement table grow
        alpha = self.n / self.m
        if alpha >= 0.5:
            self.m = self.m * 2
            self.rehash()

        #Actually start insertion
        for i in range(self.m):
            target = self.array[hash_1(k,i,self.m)]
            if target is None or target is DM:
                self.array[hash_1(k,i,self.m)] = k
                self.n += 1
                return


    def search(self,k): #Return the index of the desired key
        for i in range(self.m):
            target = self.array[hash_1(k,i,self.m)]
            if target is DM:
                continue
            elif target == k:
                return hash_1(k,i,self.m)
            else:
                return None
        return None


    def delete(self,k):
        #Start Deletion
        for i in range(self.m - 1):
            target = self.array[hash_1(k,i,self.m)]
            if target is DM:
                continue

            elif target == k:
                self.array[hash_1(k,i,self.m)] = DM
                print("Deleted {0} successfully!".format(k))
                n -= 1

                #Shrink check
                alpha = self.n / self.m
                if alpha <= 0.25:
                    self.m = self.m / 2
                    self.rehash()
                return
            
            print("Fail to find {0}".format(k))
            return None



    def rehash(self):
        old_array = self.array
        self.array = [None] * self.m
        self.n = 0

        for item in old_array:
            if item is None or item is DM:
                continue

            for i in range(self.m):
                index = hash_1(item, i, self.m)

                if self.array[index] is None:
                    self.array[index] = item
                    self.n += 1
                    break

    def print_hash(self):
        index = 0
        for item in self.array:
            if item is None:
                print("{0} | None ".format(index))
            elif item is DM:
                print("{0} | Deleted ".format(index))
            else:
                print("{0} | {1} ".format(index,item))
            index += 1


test1 = [3,1,4,1,5,9,2,6]
a = Open_Address()
for item in test1:
    a.insert(item)
a.print_hash()