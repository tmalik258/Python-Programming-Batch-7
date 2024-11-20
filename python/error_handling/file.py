# try:
#     f = open('test.txt', 'rt')
#     print(f.read())
#     f.close()
# except:
#     print("File doesn't exist")

num1 = 7
num2 = 0
result = 0

try:
    result = num1 / num2
except ZeroDivisionError:
    print('Cant divide by zero')
else:
    print(result)
finally:
    print('abc')
    
    
# ValueError
# NameError
# SyntaxError
# ImportError
# TypeError
# IndexError