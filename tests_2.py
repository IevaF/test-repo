#comment
i =  [1, -2, 10]
new_i = [i*2 for i in i if i>0]
print(new_i)


i =  [1, -2, 10]
new_i = [i*2 for i in i]
print(new_i)

i =  [1, -2, 10]
new_i = [i*2 if i > 0 else 0 for i in i]
print(new_i)



"""def foo(*args):
    return sum(args) / len(args)
foo = (10, 20, 30, 40)
print(foo)"""

x = 5
x = complex(x)
print(x)

txt = "Hello World"
x = (txt[0])
print(x)

txt = "Hello World"
x = txt[2:5]
print(x)

txt = "Hello World"
txt = txt.upper()
print(txt)
