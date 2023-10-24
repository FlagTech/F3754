squared_set = {x**2 for x in range(10)}
print(squared_set)

squared_dict = {
    x:x**2 for x in range(10) if str(x**2)[-1] == '6'
}
print(squared_dict)
