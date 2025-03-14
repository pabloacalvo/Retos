def quicksort(arr:list):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Aplica la division entera //, division flotande /
    # Particionar en tres listas
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"Pivot: {pivot}, quicksort_left: {left}, middle: {middle}, quisort_right: {right}")
    return quicksort(left) + middle + quicksort(right)


ejemplo = [10,23,2,4,1,8,100,99,67,108,56,6,5]

print(quicksort(ejemplo))
