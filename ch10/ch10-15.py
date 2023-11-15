def a_simple_generator():
    yield 1
    yield 2
    yield 3
    
for i in a_simple_generator():
    print(i)