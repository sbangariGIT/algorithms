class MergeSort():

    def __init__(self, arr) -> None:
        self.elements = arr


    def combine(self, L, R):
        A = []
        i = 0
        j = 0
        k  = 0
        while i < len(L) + len(R):
            if(j < len(L) and k < len(R)):
                if(L[j] <= R[k]):
                    A.append(L[j])
                    j += 1
                else:
                    A.append(R[k])
                    k += 1
            elif(j < len(L)):
                A.append(L[j])
                j += 1
            else:
                #When R still has elements
                A.append(R[k])
                k += 1
            i += 1
        return A
        
    def mergeSort(self, arr):
        if(len(arr) < 2):
            return arr
        else:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            L = self.mergeSort(L)
            R = self.mergeSort(R)
            return self.combine(L, R)

    def get_sorted(self):
        self.elements = self.mergeSort(self.elements)
        return  self.elements



if __name__ == "__main__":
    while True:
        try:
            elem = []
            l = input('What is the length of your Array? (If you want to quit enter q) \n')
            if l == 'q':
                break
            total = int(l)
            for i in range(total):
                elem.append(int(input(f'enter element {i+1} \n')))
            print(f'Your input is {elem}\n')
            print('Performing merge Sort\n')
            s = MergeSort(elem)
            elem = s.get_sorted()
            print(f'Your Output is {elem}\n')
        except Exception:
            print('Invalid input')
            continue