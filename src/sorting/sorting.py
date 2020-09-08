# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # 1st - loop through the merged arr
    # if the arrays are larger than 0, pinpoint which element is larger
    # pop the smaller element into merged arr
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)
        else:
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) > 1:
        # splitting array until 1 item is left on left side
        l = merge_sort(arr[:len(arr) // 2])
        # splitting array until 1 item is left on right side
        r = merge_sort(arr[len(arr) // 2:])
        # merge both items
        arr = merge(l, r)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
