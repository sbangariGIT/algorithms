class InsertionSort():

    def __init__(self, arr) -> None:
        self.elements = arr
        
    def insertionSort(self, arr):
        result = [0] * len(arr) 
        for i in range(len(arr)):
            j = i - 1
            while j >= 0 and result[j] > arr[i]:
                result[j+1] = result[j]
                j -= 1
            result[j+1] = arr[i]
        return result

    def get_sorted(self):
        self.elements = self.insertionSort(self.elements)
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
            print('Performing Insertion Sort\n')
            s = InsertionSort(elem)
            elem = s.get_sorted()
            print(f'Your Output is {elem}\n')
        except Exception:
            print('Invalid input')
            continue