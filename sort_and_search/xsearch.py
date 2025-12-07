import xsort

class XSearch:
    def sequence_search(self, data, num):
        index_list = []
        for i in range(len(data)):
            if data[i]==num:
                index_list.append(i)
        return index_list
    def binary_search(self, data, num):
        xs = xsort.XSort()
        temp = xs.insert_sort(data)

        index_list = []

        left=0
        right=len(temp)-1
        p=m=n=None

        while left<=right:
            mid=(left+right)//2
            if temp[mid]>temp[num]:
                right=mid-1
            elif temp[mid]<temp[num]:
                left=mid+1
            else:
                p=mid
                break
        if p==None:
            return None

        for i in range(p,-1,-1):
            if temp[p]!=temp[i]:
                m=i+1
                break
        if m==None:
            m=0

        for i in range(p,len(data)):
            if temp[p]!=temp[i]:
                n=i-1
                break
        if n==None:
            n=len(temp)-1

        return (m,n)
