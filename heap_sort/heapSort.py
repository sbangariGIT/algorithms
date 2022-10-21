# class Node():
#     def __init__(self, val) -> None:
#         self.val = val
#         self.left = None
#         self.rigth = None

#     def add_right(self, right):
#         self.rigth = right
    
#     def add_left(self, left):
#         self.left = left

#     def get_right(self):
#         return self.rigth
    
#     def get_left(self):
#         return self.left
    
#     def set_val(self, val):
#         self.val = val
    
#     def get_val(self):
#         return self.val
class HeapSort():

    def __init__(self, arr) -> None:
        self.elements = arr
    
    def heapify(self, arr, i):
        right = True
        if(2*i >= len(arr)):
            return
        if((2*i) + 1  >= len(arr)):
            right = False
        if right:
            # print(len(arr))
            # print((2*i) + 1)
            m = max(arr[i], arr[2*i], arr[(2*i) + 1])
        else:
            m = max(arr[i], arr[2*i])
        if m == arr[i]:
            return
        if m == arr[2*i]:
            arr[2*i] = arr[i]
            arr[i] = m
            self.heapify(arr, 2*i)
            return
        arr[(2*i) + 1] = arr[i]
        arr[i] = m
        self.heapify(arr, (2*i) + 1)

    def extract_max(self, heap):
        x = heap[0]
        heap[0] = heap[len(heap) - 1]
        return x
        

    def HeapSort(self, arr):
        #Make the array a heap
        #Left child is (2i) and right child is (2i)  + 1
        heap = arr
        for i in range(len(heap) - 1, -1, -1):
            self.heapify(heap, i)
        #List is heapified
        result = [0] * len(heap)
        x = len(heap)
        for i in range(x - 1, -1, -1):
            result[i] = self.extract_max(heap)
            heap = heap[:-1]
            self.heapify(heap, 0)
        return result

    def get_sorted(self):
        self.elements = self.HeapSort(self.elements)
        return  self.elements

if __name__ == "__main__":
    while True:
        # try:
            elem = []
            l = input('What is the length of your Array? (If you want to quit enter q) \n')
            if l == 'q':
                break
            total = int(l)
            for i in range(total):
                elem.append(int(input(f'enter element {i+1} \n')))
            print(f'Your input is {elem}\n')
            print('Performing Heap Sort\n')
            s = HeapSort(elem)
            elem = s.get_sorted()
            print(f'Your Output is {elem}\n')
        # except Exception:
        #     print('Invalid input')
        #     continue