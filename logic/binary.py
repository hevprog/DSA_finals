#binary search 
import time

class BinarySearchLogic:
    def __init__(self, delay=1):
        self.delay = delay  # delay between steps

    def run_search(self, arr, target, callback):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            
            callback(mid, "reset")
            time.sleep(self.delay)

            callback(mid, "highlight")
            time.sleep(self.delay)

            if arr[mid] == target:
                callback(mid, "found")
                return
            elif arr[mid] < target:
                callback(mid, "left_red")
                time.sleep(self.delay)
                left = mid + 1
            else:
                callback(mid, "right_red")
                time.sleep(self.delay)
                right = mid - 1