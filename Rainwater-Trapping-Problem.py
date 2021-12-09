from datetime import datetime

def maxWaterVolume(arr, n):
    maxVolume = 0
    for i in range(1,n-1):
        leftMax = arr[i]
        for j in range(i):
            leftMax = max(leftMax, arr[j])

        rightMax = arr[i]
        for j in range(i+1, n):
            rightMax = max(rightMax, arr[j])
        maxVolume = maxVolume + min(leftMax, rightMax) - arr[i]
    return maxVolume

def maxWaterVolumeOptimised(arr, n):
    maxVolume = 0
    leftMax = [0]*n
    rightMax = [0]*n

    leftMax[0] = arr[0]
    for i in range(1,n):
        leftMax[i] = max(leftMax[i-1], arr[i])
    rightMax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], arr[i])

    for i in range(1,n):
        maxVolume = maxVolume + min(rightMax[i], leftMax[i]) - arr[i]
    return maxVolume

arr = [0,1,0,2,1,0,1,3,2,1,2,1,9,1,3,4,5,6,7,1,0,4,0,0,3,4,1,6,1,2,7,8,0,8]
start = datetime.now()
maxVolumeStored = maxWaterVolume(arr, len(arr))

# maxVolumeStored = maxWaterVolumeOptimised(arr, len(arr))
end = datetime.now()
# print('Maximum Volume of RainWater Stored:', maxVolumeStored )
print('Maximum Volume of RainWater Stored:', maxVolumeStored )
print('Total Time Taken:',end-start)
