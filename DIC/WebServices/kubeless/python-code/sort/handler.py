import time
import socket

def handler(event, context):
    startTime = time.time()
    arr = [3, 6, 8, 10, 1, 2, 1, 4, 5, 6, 7, 8, 2232, 2, 4, 5, 7, 9, 20, 0, 88, 7, 34]
    time_load = time.time() - startTime
    result = quicksort(arr)
    token = str(result)
     
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler("","")


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
