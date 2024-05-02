def rotate(nums,k):
    n = len(nums)
    k = k % n  # Ensure k is within the range of the array size

    # Reverse the last k elements
    nums[:n - k] = reversed(nums[:n - k])

    print(nums)
    
    # Reverse the first n-k elements
    nums[n - k:] = reversed(nums[n - k:])

    print(nums)
    
    # Reverse the whole array
    nums[:] = reversed(nums)

    return nums


print(rotate([1,2,3,4,5,6,7],3))

