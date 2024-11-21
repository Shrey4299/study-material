import heapq
from typing import List

def explain_heaps():
    print("### Explanation of Heaps ###\n")
    print("1. A **Max Heap** is a binary heap where the root is the maximum element. "
          "In a Max Heap, for every parent node, its value is greater than or equal to the values of its children.")
    print("2. A **Min Heap** is a binary heap where the root is the minimum element. "
          "In a Min Heap, for every parent node, its value is smaller than or equal to the values of its children.\n")
    print("In Python, the `heapq` library only supports Min Heap. To implement Max Heap, we store negative values.\n")

def demonstrate_max_heap():
    print("\n### Max Heap Example (Using Negatives) ###")
    
    elements = [3, 1, 6, 5, 2, 4]
    print("Original elements:", elements)
    
    # Convert elements to negatives to simulate max heap
    max_heap = [-x for x in elements]
    
    # Heapify to build the max heap (negated values)
    heapq.heapify(max_heap)
    print("Max Heap (after heapify):", [-x for x in max_heap])  # Convert back to positive for display

    # Push element (negated to fit max heap behavior)
    heapq.heappush(max_heap, -7)
    print("After inserting 7 into Max Heap:", [-x for x in max_heap])
    
    # Get the max value (root of max heap)
    max_value = -max_heap[0]
    print("Maximum element (root of Max Heap):", max_value)
    
    # Pop the maximum element
    heapq.heappop(max_heap)
    print("After popping the maximum element:", [-x for x in max_heap])

def demonstrate_min_heap():
    print("\n### Min Heap Example ###")
    
    elements = [3, 1, 6, 5, 2, 4]
    print("Original elements:", elements)
    
    # Build min heap
    heapq.heapify(elements)
    print("Min Heap (after heapify):", elements)
    
    # Push element (regular since it's min heap)
    heapq.heappush(elements, 0)
    print("After inserting 0 into Min Heap:", elements)
    
    # Get the min value (root of min heap)
    min_value = elements[0]
    print("Minimum element (root of Min Heap):", min_value)
    
    # Pop the minimum element
    heapq.heappop(elements)
    print("After popping the minimum element:", elements)

def sortArray(self, nums: List[int]) -> List[int]:
    # Copy the input list
    element = [x for x in nums]

    print("Original elements:", element)

    # Convert the list into a Min Heap
    heapq.heapify(element)

    print("Min Heap:", element)

    # Extract elements from the heap and return in sorted order
    sorted_list = [heapq.heappop(element) for _ in range(len(element))]

    print("Sorted list:", sorted_list)

    return sorted_list

if __name__ == "__main__":
    explain_heaps()
    demonstrate_max_heap()
    demonstrate_min_heap()
