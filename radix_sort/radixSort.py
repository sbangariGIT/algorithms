from unittest import result


class RadixSort():

    def __init__(self, arr, d) -> None:
        self.elements = arr
        self.digiLen = d

    def get_digit(self, number, n):
        return number // 10**n % 10

    def combine(self, L, R, d):
        A = []
        i = 0
        j = 0
        k  = 0
        while i < len(L) + len(R):
            if(j < len(L) and k < len(R)):
                if(self.get_digit(L[j],d)  <= self.get_digit(R[k],d)):
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
        
    def mergeSort(self, arr, i):
        if(len(arr) < 2):
            return arr
        else:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            L = self.mergeSort(L, i)
            R = self.mergeSort(R, i)
            return self.combine(L, R, i)
        
        
    def radixSort(self, arr):
        result = arr
        for i in range(self.digiLen):
            result = self.mergeSort(result, i)
        return result

    def get_sorted(self):
        self.elements = self.radixSort(self.elements)
        return  self.elements


if __name__ == "__main__":
    while True:
        try:
            elem = []
            l = input('What is the length of your digits? (If you want to quit enter q) \n')
            if l == 'q':
                break
            digi_len = int(l)
            total = int(input('What is the lenght of your array?'))
            i = 0
            while i < total:
                x = input(f'enter element {i+1} \n')
                if len(x) != digi_len:
                    print(f'This input is not of the correct length. Please input number of length {digi_len}')
                    i -= 1
                    continue
                elem.append(int(x))
                i += 1
            print(f'Your input array is {elem}\n')
            print('Performing Radix Sort\n')
            s = RadixSort(elem, digi_len)
            elem = s.get_sorted()
            print(f'Your Output is {elem}\n')
        except Exception:
            print('Invalid input')
            continue