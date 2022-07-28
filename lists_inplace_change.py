def modify_list(ls: list):
    new_l = [i // 2 for i in ls if i % 2 == 0]
    ls.clear()
    ls += new_l


# it is possible to change all elements with the same memory allocation using [:]. Functions are equal.
def modify_list_2(ls: list):
    ls[:] = [i // 2 for i in ls if i % 2 == 0]


arr = [1, 2, 3, 4, 5, 6, 7]
modify_list(arr)
print(arr)
arr = [1, 2, 3, 4, 5, 6, 7]
modify_list_2(arr)
print(arr)

