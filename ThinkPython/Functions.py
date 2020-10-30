import math

print(int(3.9999))
print(float(32))
print(str(3.14), end=" ")
print(type(str(3.14)))

print(math)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
print(math.sqrt(2)/2.0)
x =radians
x =math.exp(math.log(x+1))
print(x)
#Adding new Functions
'''
def print_lyrics():
print "I'm a lumberjack, and I'm okay."
print "I sleep all night and I work all day."
'''
def print_twice(parametros):
    print(parametros)
    print(parametros)
print_twice('Spam')
print_twice(17)
print_twice('Yo' * 4)
print_twice(math.cos(math.pi))
samuel = 'Yo soy samuel'
print_twice(samuel)
#variebles  and parametros locales
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'

cat_twice(line1, line2)
print(math.sqrt(5))
result = print_twice('Bing')
print(result)
print(len('allen'))

print(((('+' + ('-'*4))*2 +'+')+ '\n|    |    |'*4 +'\n')*3)

