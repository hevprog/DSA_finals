#binary search 

class binarySEARCH:
    def __init__(self):
        pass
    def Binary_Search(self, arr, target):
        steps = []
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            steps.append(f"Checking middle index {mid}, {arr[mid]} is the middle number")

            if arr[mid] == target:
                steps.append(f"Found {target} at index {mid}")
                
                return mid, steps
            elif arr[mid] < target:
                steps.append(f"{arr[mid]} < {target}, search right half")
                low = mid + 1
            else:
                steps.append(f"{arr[mid]} > {target}, search left half")
                high = mid - 1

        steps.append(f"{target} not found")
        
        return -1, steps