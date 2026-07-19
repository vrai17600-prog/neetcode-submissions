class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size  += 1
        


    def popback(self) -> int:
        last = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1
        return last
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        
        self.array = new_arr


    def getSize(self) -> int:
        # int_size = 0
        # for num in self.array:
        #     if num == None:
        #         break
        #     int_size += 1
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
