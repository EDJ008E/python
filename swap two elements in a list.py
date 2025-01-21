def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]

my_list = [3, 7, 11, 15, 19]
swap_elements(my_list, 1, 3)
print(my_list)
