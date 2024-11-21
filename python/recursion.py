
from typing import List


def print_1_to_n(n):

    if n == 1:
        print(n)
        return
    

    print_1_to_n(n-1)
    print(n)

def print_n_to_1(n):

    if n == 1:
        print(n)
        return
    
    print(n)
    print_n_to_1(n-1)

def factorial(n):

    if n == 1:
        return 1
    
    ans = n * factorial(n-1)

    return ans

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def recursive_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Remove the last element
    last = arr.pop()
    
    # Recursively sort the remaining array
    sorted_arr = recursive_sort(arr)
    
    # Insert the last element into the sorted array at the correct position
    return insert_sorted(sorted_arr, last)

def insert_sorted(arr, element):
    # Base case: If the array is empty or the element is greater than the last item
    if not arr or element >= arr[-1]:
        arr.append(element)
        return arr

    last = arr.pop()

    insert_sorted(arr, element)

    arr.append(last)

    return arr


def recursive_reverse(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Remove the last element
    last = arr.pop()
    
    # Recursively sort the remaining array
    sorted_arr = recursive_reverse(arr)
    
    # Insert the last element into the sorted array at the correct position
    return insert_last(sorted_arr, last)

def insert_last(arr, element):
    # Base case: If the array is empty or the element is greater than the last item
    if not arr:
        arr.append(element)
        return arr

    last = arr.pop()

    insert_last(arr, element)

    arr.append(last)

    return arr

def get_all_subset(input, output):

    if len(input) == 0:
        print("output", output)
        return
    
    op1 = output
    op2 = output

    op2 += input[0]
    input = input[1:]

    get_all_subset(input, op1)
    get_all_subset(input, op2)


    return


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def create_subset(i):
        if i == len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[i])

        create_subset(i + 1)

        subset.pop()

        create_subset(i + 1)


    create_subset(0)
    return res


def make_permutation(input):
        res = set()

        def permute(input, output, res):
            if len(input) == 0:
                res.add(output)
                return
            
            for i in range(len(input)):
    
                new_input = input[:i] + input[i+1:]
                new_output = output + input[i]
                permute(new_input,new_output, res)
            
        permute(input, "", res)
        return list(res)

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def permute(input, output, res):
        if len(input) == 0:
            res.append(output[:])  
            return
        
        for i in range(len(input)):
            # Exclude the current element
            new_input = input[:i] + input[i+1:]

            # Include the current element in the output
            output.append(input[i])

            # Recurse with the updated input and output
            permute(new_input, output, res)

            # Backtrack to explore other possibilities
            output.pop()
    
    permute(nums, [], res)
    return res











# print_1_to_n(7)
# print("\n")
# print_n_to_1(7)
# print("\n")
# print("Factorial of 6 is: ", factorial(6))
# print("Fibonacci of 6 is: ", fibonacci(6))


# arr = [3, 1, 4, 1, 5, 9, 2]
# print("Original array:", arr)

# sorted_arr = recursive_sort(arr.copy())
# print("Sorted array:", sorted_arr)

# reversed_arr = recursive_reverse(arr)
# print("Reversed array:", reversed_arr)

# all_subset = get_all_subset("abc","")
# print("All subset:", all_subset)

nums = [1,2]

subset_array = subsets(nums)
print("Subset:", subset_array)

input = "abc"

print("All permutation :", make_permutation(input))




