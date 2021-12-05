import heapq

a = [1, 4, 3, 5, 2]
print("List =", a)
# Convert the iterable (list) into a min-heap in-place
heapq.heapify(a)
print("Min Heap =", a)
# Use heappush heapq.heappush(a, 10)
print("After heappush(), Min Heap =", a)
# Use array indexing to get the smallest element
print(f"Smallest element in the heap queue = {a[0]}")
# Use heappop() and return the popped element
popped_element = heapq.heappop(a)
print(f"Popped element = {popped_element}, Min Heap = {a}")

