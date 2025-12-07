import xsort

class XSearch:
    def sequence_search(self, data, num):
        index_list = []
        for i, value in enumerate(data):
            if value == num:
                index_list.append(i)
        return index_list

    def binary_search(self, data, num):
        # 주의: 내부에서 정렬하면 원본 인덱스 정보가 소실됩니다.
        # 단순히 값의 존재 여부나, 정렬된 상태에서의 위치를 찾는 것이라면 유효합니다.
        xs = xsort.XSort()
        # 원본 데이터 보존을 위해 복사본 사용 권장
        temp = xs.insert_sort(data[:]) 

        left = 0
        right = len(temp) - 1
        found_index = None

        while left <= right:
            mid = (left + right) // 2
            if temp[mid] > num:  # temp[num]이 아니라 num과 비교
                right = mid - 1
            elif temp[mid] < num: # temp[num]이 아니라 num과 비교
                left = mid + 1
            else:
                found_index = mid
                break
        
        if found_index is None:
            return None

        # 중복된 값이 있을 경우 범위 탐색 (m, n)
        # 기존 로직을 더 간결하게 다듬을 수 있으나, 작성하신 로직의 흐름을 유지함
        m = found_index
        while m > 0 and temp[m-1] == temp[found_index]:
            m -= 1
            
        n = found_index
        while n < len(temp) - 1 and temp[n+1] == temp[found_index]:
            n += 1

        return (m, n)
