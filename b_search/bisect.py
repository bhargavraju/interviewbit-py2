def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo+hi)//2
        if target > arr[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) / 2
        if target >= arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low
