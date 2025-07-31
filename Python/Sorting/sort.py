class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr

class InsertionSort():
    def __init__(self,arr):
        self.arr=arr
    def sort(self):
        key=1
        n=len(self.arr)
        for i in range(n):
            for j in range(n):
                if(key<n and self.arr[j]>self.arr[key]):
                    self.arr[key],self.arr[j]=self.arr[j],self.arr[key]
                key+=1
        return self.arr

def main():
    n = int(input("Enter array size: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    bubble_sorted_arr = BubbleSort(arr).sort()
    insertion_sort=InsertionSort(arr).sort()
    print("Sorted array:", insertion_sort)


if __name__ == "__main__":
    main()
