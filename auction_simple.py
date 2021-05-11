from gen_AP import gen_AP
import numpy as np
import random

###########
# 1. Start with a set U of all bidders.U denotes the set of allunassigned bidders. 
# We also maintain a set of prices which are initialized to all 0, 
# and any structure that stores the current
# tentative (partial) assignment.
# 2. Pick any bidder i from U. Search for the item j that gives her the highest net payoff Aij - pj,
# and also an item k that gives her the second highest net payoff.
# 3. The price pj of item j is updated to be pj <- pj + (Aij - pj) - (Aik - pk). 
# This update simply says that pj is raised to the level at which bidder i is different 
# (in terms of net payoff) bewteen item j and item k, i.e., the updated prices satisfy Aij - pj = Aik - pk.
# 4. Now assign item j to bidder i. If item j was previously assigned to another bidders, then remove that assignment and adds to U.
# 5. If U becomes empty, the algorithm is over; otherwise, go back to Step (2).


dim = 4 # size of cost matrix should be dim*dim
c_range = 1 # lagest possible value in cost
cost = gen_AP(dim, c_range) # cost matrix

cost = -1 * np.array([[14, 5, 8, 7],
        [2, 12, 6, 5],
        [7, 8, 3, 9],
        [2, 4, 6, 10]])

U = list(range(dim)) # initialize unassigned bidders
P = np.zeros(dim) # initialize the p list
A = {} # dict for assignment: keys are terminal points and items are start points

# sorting algorithm copyed from leetcode https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
# dont know how it works
def find (row):
    origin_row = row.copy() # partition method will change the arrangement of row
    size = len(row)
    target = size - 2
    left = 0
    right = size - 1
    while True:
        index = partition(origin_row, left, right)
        if index == target:
            rowk, rowj = origin_row[index], origin_row[index+1]
            break
        elif index < target:
            # 下一轮在 [index + 1, right] 里找
            left = index + 1
        else:
            right = index - 1
    
    j = -1
    k = -1
    for i in range(len(row)):
        if row[i] == rowk:
            k = i
        if row[i] == rowj:
            j = i
        if j >= 0 and k >= 0:
            return j, k


def partition(nums, left, right):
    pivot = nums[left]
    j = left
    for i in range(left + 1, right + 1):
        if nums[i] < pivot:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[left], nums[j] = nums[j], nums[left]
    return j
'''
a =  [0.23444484, 0.94515553, 0.18878696, 0.26411619, 0.52362011, 0.16681413, 0.20362039, 0.99637351, 0.01949381, 0.95225676]
print(find(a))
print(a)
'''
while len(U) > 0:
    random.shuffle(U)
    i = U.pop()
    j, k = find(cost[i]-P) # find i, k that give largest and second largest Aij - Pj
    P[j] = cost[i,j] - cost[i, k] + P[k] # update Pj
    if j in A.keys(): # assign j to i
        U.append(A[j])
        A[j] = i 
    else:
        A[j] = i

print(A)
