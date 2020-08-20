'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    # Your code here
    right_pointer = k

    for i in range(len(nums)):
        if len(nums[i:right_pointer]) == k:
            nums[i] = max(nums[i:right_pointer])
            right_pointer += 1
        else:
            nums.pop()
              
    return nums

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
