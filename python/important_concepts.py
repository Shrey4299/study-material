from typing import List

# Sliding Window
# ================


from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    fright ,fleft = 0, 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            if right - left + 1 > maxLen:
                maxLen = right - left + 1
                fright = right
                fleft = left

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]


    return maxLen, a[fleft:fright + 1]

def getShortestSubarray(a: [int], k: int) -> int:
    n = len(a)  # size of the array

    left, right = 0, 0  # 2 pointers
    Sum = a[0]
    minLen = float('inf')  # Initialize to infinity to find minimum length
    fright, fleft = 0, 0
    found = False  # Flag to check if a valid subarray is found

    while right < n:
        # Shrink the window from the left while sum > k
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # If sum equals k, check for the shortest subarray
        if Sum == k:
            found = True  # Mark that we found a valid subarray
            if right - left + 1 < minLen:
                minLen = right - left + 1
                fright = right
                fleft = left

        # Move the right pointer forward and add the element
        right += 1
        if right < n:
            Sum += a[right]

    # If a subarray was found, return its length and elements
    if found:
        return minLen, a[fleft:fright + 1]
    else:
        return 0, []  # No valid subarray found

# Get the maximum sum of subarray of size k
def getSubarrayWithSumK(Arr: List[int], K: int) -> int:
    n = len(a) # size of the array.

    i = 0
    j = 0

    start = 0
    end = 0

    sum = 0
    max_sum = 0

    while j < len(Arr):

        sum = sum + Arr[j]

        if ( j - i + 1 < K):
            j += 1
        
        elif (j - i + 1 == K):
            if sum > max_sum:
                max_sum = sum
                start = i
                end = j


            sum = sum - Arr[i]
            j += 1
            i += 1

    return max_sum , Arr[start:end + 1]

def getShortestSubarrayWithGreaterThan(a: List[int], k: int) -> int:
        n = len(a)  # size of the array
    
        left = 0  # Left pointer
        Sum = 0  # Sum of the current window
        minLen = float('inf')  # Initialize to infinity to find minimum length
        start = 0
        end = 0
    
        # Iterate with the right pointer
        for right in range(n):
            # Add the current element to the sum
            Sum += a[right]
    
            # While the sum is greater than the target k, shrink the window from the left
            while Sum > k:
                # Update the minimum length of the subarray
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left
                    end = right
    
                # Shrink the window by removing the leftmost element and moving the left pointer
                Sum -= a[left]
                left += 1
    
        # If no valid subarray is found, return 0
        return minLen if minLen != float('inf') else 0 , a[start: end + 1]

def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s) # size of the array.

    left, right = 0, 0 # 2 pointers
    unique_str = set()
    maxLen = 0
    while right < n:

        if s[right] not in unique_str:
            unique_str.add(s[right])
            right += 1

        else:
            left += 1
            right = left
            unique_str.clear()



        # if sum = k, update the maxLen i.e. answer:
        if len(unique_str) > maxLen:
            print(s[left:right+1])
            maxLen = len(unique_str)


    return maxLen

a = [4, 1, 1, 2, 1, 1, 5]
k = 5  # Example subarray size

a2 = [1, 4, 45, 6, 0, 19]
k2 = 51

# Get the maximum sum of subarray of size k
max_sum, sub_arr = getSubarrayWithSumK(a, k)
print(f"The maximum sum of the subarray with size {k} is: {max_sum} with arr {sub_arr}")

# Get the longest subarray with sum k
max_len, sub_arr = getLongestSubarray(a, k)
print(f"The longest subarray with sum {k} is: {max_len} elements long with arr {sub_arr}.")

# Get the shortest subarray with sum k
min_len, sub_arr = getShortestSubarray(a2, k2)
print(f"The shortest subarray with sum {k2} is: {min_len} elements long with arr {sub_arr}.")

min_len, sub_arr = getShortestSubarrayWithGreaterThan(a2, k2)
print(f"The shortest subarray with sum greater than {k2} is: {min_len} elements long with arr {sub_arr}.")