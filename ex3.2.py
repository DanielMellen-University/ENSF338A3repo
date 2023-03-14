import json
import time
import matplotlib.pyplot as plt


# Load the array and list of search tasks
with open("ex2data.json", "r") as f:
   array = json.load(f)


with open("ex2tasks.json", "r") as f:
   tasks = json.load(f)


# Define a function to perform binary search with configurable initial midpoint


def isInArray(arr, target,mI):
   startI = 0
   endI = len(arr) - 1


   while(startI < endI - 1):
       if(target < arr[mI]):
           endI = mI
       else:
           startI = mI
       if (target == arr[mI]):
           return True
       mI = round((startI + endI)/2)


   if(target == arr[startI] or (target == arr[endI])):
       return True;
   return False;






# Define a function to time the performance of each search task
def time_search_task(array, tasks):
   bestMP = [];
   for t in tasks:
       bestTime = -1
       for mp in (range(array[0],array[len(array)-1],10)):      
           start_time = time.time()
           isInArray(array, t,mp)
           end_time = time.time()
           extime = end_time - start_time
           if ((bestTime == -1) or (extime < bestTime)):
               bestTime = extime;
               bestMP4t = mp;
       bestMP.append(bestMP4t)
   return bestMP;
  






# Perform the search tasks and record the best midpoints and times
"""
t = 384;
print("\n" + str(t) + "\n" + str(isInArray(array, t)))


t = 385;
print("\n" + str(t) + "\n" + str(isInArray(array, t)))


t = 386;
print("\n" + str(t) + "\n" + str(isInArray(array, t)))


"""


resultsBMP = time_search_task(array, tasks);


# Produce a scatterplot of the results
plt.scatter(tasks, resultsBMP)
plt.xlabel("Search Task")
plt.ylabel("Best Midpoint")
plt.title("Optimal Midpoint for Each Search Task")
plt.show()