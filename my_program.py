#made a correction

#def sentence_maker(phrase):
 #interrogatives = ("how", "what", "why")
  #capitalized = phrase.capitalize()
#if phrase.startswith(interrogatives):
   #return "{}?".format(capitalized)
#else:
  # return "{}.".format(capitalized)
#print(sentence_maker("how are you"))


#Weather = input("Say something:")
#message = f"{Weather}" 
#if message == "\end":
   # break
#else:
    #print(message)
  
    
temps = [221, 334, 556, 842]
new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
        
print(new_temps)

temps = [221, 334, 556, 842]
new_temps = [temp / 10 for temp in temps]

print(new_temps)

lst = [99, 'no data', 95, 94, 'no data'] 
def foo(lst):
    return [value for value in lst if isinstance(value, int)]

print(foo)

def foo(lst):
    return [value for value in lst if value > 0]

print(foo)

def foo(lst):
    return [value if isinstance(value, int) else 0 for value in lst]
lst=[100, 'no data', 95, 94, 'no data']

print(foo)

def foo(lst):
    return sum([float(i) for i in lst])
lst=['1.2', '2.6', '3.3']
print(foo)

[i*2 for i in [1, -2, 10] if i>0]