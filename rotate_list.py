# Add your clarifying questions here


# ["a", "b", "c"] -> shift_by 2 
# ["b", "c", "a"]
# i = shift_by
# ["c","d",]
# 15, 15 - 3 =12,9,6,3

def rotate_list(list, shift_by):
    if shift_by > len(list):
        shift_by %= len(list) 

    for i in range(shift_by, len(list)):
     rotated_list = [list[shift_by]]
        #if shift_by <= len(list)
            # if at end of list
                # update i with ((len-1) - i)
                # if i == shift_by -1 
                # return rotated_list
                
            #append list[shift_by] to rotated_list
            #rotated_list.append(list[i])


assert rotate_list(["a", "b", "c"], 2) == ["b", "c", "a"]      
assert rotate_list(["a", "b", "c"], 0) == ["a", "b", "c"]
assert rotate_list(["a", "b", "c"], 3) == ["a", "b", "c"]
assert rotate_list([], 4) == []