#counting sort 


class counting:
    sorted = False
    def __init__(self,a):
        self.arr = a
        self.counts = []
    def get_array(self):
        return self.arr if sorted else None
    def get_count(self):
        return self.counts if sorted else None
    def restart(self,a):
        self.arr = a
    def sort(self):
        self.sorted = True
        sorted_arr = [0]*(max(self.arr)+1)

        while(len(self.arr)>0):
            num = self.arr.pop()
            sorted_arr[num] = sorted_arr[num] + 1
        self.counts = sorted_arr[:]
        for i in range(len(sorted_arr)):
            while sorted_arr[i] > 0:
                self.arr.append(i)
                sorted_arr[i] = sorted_arr[i]-1

if __name__ == "__main__":
    unsort = [1,1,3,4,5,5,4,1]
    countS = counting(unsort)
    countS.sort()
    print(countS.get_array())
                