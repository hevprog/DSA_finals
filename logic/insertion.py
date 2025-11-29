#insertion sort 

class insertion:
    sorted = False
    def __init__(self, a):
        self.arr = a
    
    def sort(self):
        self.sorted = True
        n = 10

        for i in range(len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j];
                j-=1
            self.arr[j + 1] = key;
    
    def restart(self, a):
        self.arr = a
    
    def getArray(self):
        return self.arr if sorted else None

if __name__ == "__main__":
    unsortedArray = [63, 22, 12, 23, 45, 34, 11, 23, 78, 99]
    insertion = insertion(unsortedArray)
    insertion.sort()
    print(insertion.getArray())