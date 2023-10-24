black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

new_list1 = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com'
}

new_list2 = {'hacker1@hacker.com'}

whole_list = black_list | new_list1

print(new_list1.isdisjoint(new_list2))
print(whole_list == black_list)
print(whole_list > new_list1)
print(whole_list >= new_list1)
print(whole_list.issubset(whole_list))
print(whole_list < whole_list)
print(new_list1 <= new_list2)
print(new_list1 >= new_list2)
print(new_list1 != new_list2)