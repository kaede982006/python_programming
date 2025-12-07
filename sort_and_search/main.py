import xsort
import xsearch
import xrandom

xrandom = xrandom.XRandom()
data = xrandom.randint(20, 0, 20)

xsort = xsort.XSort()

print(data)
print(xsort.bubble_sort(data))
print(xsort.select_sort(data))
print(xsort.insert_sort(data))

print()

xsearch = xsearch.XSearch()
num = int(input("Search for: "))
print(xsearch.sequence_search(data, num))
print(xsearch.binary_search(data, num))
