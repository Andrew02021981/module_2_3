my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#my_list = [3, 0, 0, 1, 0, 4, 0, 7, 8, 0, 0, 2]  # test
number_ind = 0
while number_ind <= len(my_list) - 1:
    if my_list[number_ind] == 0:
       number_ind = number_ind + 1
       continue
    elif my_list[number_ind] > 0:
        print(my_list[number_ind])
        number_ind = number_ind + 1
    else:
        break
