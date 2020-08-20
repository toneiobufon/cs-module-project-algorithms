'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #check if any int is twice in the array, list, set
    # if so remove one and leave one in the set
    numbers = set() # creating a set limits the existence of any number to be unique

    for i in arr:
        if i in numbers:
            numbers.remove(i)
        else:
            numbers.add(i)

    return list(numbers)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")