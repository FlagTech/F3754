blacklist = frozenset({
    'hacker@hacker.com',
    'badboy@badbadguy.com'
})

new_list1 = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com'
}

union1 = blacklist | new_list1
union2 = new_list1 | blacklist

print(type(union1))
print(type(union2))