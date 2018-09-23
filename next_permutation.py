def swapIndex(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def reverse(arr,a,b):
    for i in range((b-a)//2+1):
        swapIndex(arr, a+i, b-i)
    
def next_permutation(arr):
    # 在这里回答吧 mua~
    if not arr:
        # Empty arr!
        # len(arr) - 1 will be -ve!!!!!!!
        return False
    size = len(arr)
    i = size - 2
    while arr[i] >= arr[i + 1]:
        i -= 1
    # arr[i] < arr[i+1]
    # arr[i+1] > arr[i+2] > ... > arr[size-1] 
    if i == -1:
        return False
    else:
        peak = i + 1
        if arr[peak-1] >= arr[size - 1]:
            l_index = peak
            se_index = size - 1
            mid = (l_index + se_index) // 2
            while l_index + 1 != se_index:
                if arr[mid] > arr[i]:
                    l_index = mid
                else:
                    se_index = mid
                mid = (l_index + se_index) // 2
        else:
            l_index = size - 1
        swapIndex(arr, i, l_index)
        reverse(arr, i + 1, size - 1)
        return True



def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)    

def next_permutation_answer(arr):
    if not arr:
        # Empty arr!
        # len(arr) - 1 will be -ve!!!!!!!
        return False
    peakPtr = len(arr) - 1
    while (peakPtr > 0):
        if arr[peakPtr - 1] < arr[peakPtr]:
            break
        peakPtr -= 1
    reverse(arr, peakPtr, len(arr) - 1)
    prePeak = peakPtr - 1
    if prePeak < 0:
        return False
    # In the reversed part, 
    # find the smallest element that is larger than prePeak
    # then swap it with prePeak
    for i in range(peakPtr, len(arr)):
        if arr[prePeak] < arr[i]:
            swapIndex(arr, prePeak, i)
            return True


if __name__ == '__main__':
    arr = [3, 3, 8, 8]

    # num = factorial(len(arr))
    # for i in range(num):
    #     print(arr)
    #     next_permutation(arr)

    # Bonus: return False if arr is changed from the last permutation to first permutation;
    # return True otherwise
    # The benefit is that you don't have to start from the first permutation
    # and you can write the loop like this:

    count = 0
    while True:
        count += 1
        print(arr)
        if not next_permutation(arr):
            break
    print(count)

