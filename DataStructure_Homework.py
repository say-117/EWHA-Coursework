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


    


