#Homework 1 - 1 ; Jump Game

# Key note : 'Maximun Jump length" : 0 <= jump length <=  nums[n]
# Trying out Greedy Method
# takeaways : implementing greedy principe, along with using range as a alternate list for index. keeping a physical note by my side and following along the codes helped a lot!


nums = [3,2,4,1,3,2,0,1] #list of 8


def jump(list) :
    goal = len(list)-1 #idx

    # for idx,val in enumerate(list) : #for efficiency, I need this to be in same order but start from backward - hence nums_alt
    #     if idx + val >= goal :
    #         goal = nums[idx]
    #         return goal
    #     else :
    #         continue

# when there is no possible result?

    for i in range(len(list)-2, -1, -1) : #tuple : 6 to 0 (index of 7th element to 1st, backward), i being the index
        if i + list[i] >= goal : 
            goal = i
        else :
            continue
        # working backward solves the problem of order
        #key being having to repeat the least times as possible

    if goal == 0 :
        print(True)

    else :
        print(False)

jump(nums)

    #     for hop in jump_len : # find alternative goalpoint - result is false if there isn't any
    #         if idx + hop == goal :
    #             goal = nums[idx]
    #             return goal # goal renewed ## in occasion with 2 or more renewable goals?
    #         else :
    #             continue


#Homework 1 - 2 ; Rotate Image
#Key ides : inner/outer squares
    
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
square2 = [[2,1],[5,4]] #simpler one for testing out

# algorithm for sectioning out cycles
# WITHOUT ANOTHER 2D MATRICES



def Rotate_90(matrix) : #works for outermost square of the matrix
    n = len(matrix) #number of elements
    n = n-1 #last index

    #find the # of cycle needed
    cycleNo = n//2 #integer devision
        # if n is odd No., the center piece doesn't need to move
        
    for k in range(0, cycleNo) :
        #redefine range
        
        # single save variable method
        for a in range (k,n-k) : #matrices size/area control
            i = a - k # offset ; k being initial range (starting point)

            temp = matrix[k,a+k] #save top
            matrix[k][a+k] = matrix[n-i][k] #top = left
            matrix[n-i][k] = matrix [n-k][n-a-k] #left = bottom
            matrix[n-k][n-a-k] = matrix[a][n-k] #bottom = right
            matrix[a+k][n-k] = temp #right = top

        
        









    # #single rotation method
    # for a in range(0,n-1) :
    #     #top to right
    #     temp1 = matrix[a][n] #right
    #     matrix[a][n] = matrix[0][adj] 
    #     #right to bottom
    #     temp2 = matrix[n-a][n] #bottom
    #     matrix[n-a][n] = temp1
    #     #bottom to left
    #     temp1 = matrix[n-a][0] #left
    #     matrix[n-a][0] = temp2
    #     #left to top
    #     matrix[0][a] = temp1
    



print(Rotate_90(square2))
    # top_list = None
    # left_list = None
    # right_list = None
    # bottom_list = None

    # # create new sets of list
    # for a in range (0,n-2) :
    #     top = matrix[0][a]
    #     top_list.append(top)
    #     right = matrix[a][n-1]
    #     right_list.append(right)

    # #In reverse order
    # for a in range (n-2,0,-1) :
    #     bottom = matrix[n-1][a]
    #     bottom_list.append(bottom)
    #     left = matrix[a][0]
    #     left_list.append(left)

    # #reassign matrix elemets
    # for a in range(0,n-2) :
    #     matrix[a][n-1] = top_list[a]
    #     matrix[0][a] = right_list[a]
    
    # for a in range (n-1,1,-1) :
    #     matrix[end][a] = left_list[a]
    #     matrix[0][a] = bottom_list[a]

    # print(top_list)
    # print(bottom_list)
    # print(right_list)
    # print(left_list)


#     top = matrix[0]
#     left = matrix[:][0]
#     right = matrix[:][n]
#     bottom = matrix[n][:] 
            

#     for k in range(0,n):
#         matrix[k][n] = top[k]

#     for k in range(0,n):
#         matrix[n][k] = right[k*(-1)][n]

#     for k in range(0,n):
#         matrix[0][k] = bottom[k][n]

#     for k in range(0,n):
#         matrix[0][k] = left[k*(-1)][0]






        
            