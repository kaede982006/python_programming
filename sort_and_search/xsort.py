class XSort:
    def __swap(self, num1, num2):
        num1, num2 = num2, num1
        return (num1, num2)
    def bubble_sort(self, data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j]>data[j+1]:
                    data[j], data[j+1] = self.__swap(data[j], data[j+1])
        return data
    def select_sort(self, data):
        for i in range(len(data)-1):
            min_value = i
            for j in range(i+1,len(data)):
                if data[min_value] > data[j]:
                    min_value = j
            data[min_value], data[i] = self.__swap(data[min_value], data[i])
        return data
    def insert_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            # 정렬된 부분(0 ~ i-1)을 뒤에서부터 탐색
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j] # 오른쪽으로 한 칸 이동
                j -= 1
            data[j + 1] = key
        return data
