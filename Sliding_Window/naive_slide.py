#Find the maximum sum of any 3 consecutive elements.
arr = [2, 1, 5, 1, 3, 2]


def max_sum_naive(arr,k):
    n = len(arr)
    max_sum  = 0
    for i in range(n-k+1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_sum_naive(arr,3))
