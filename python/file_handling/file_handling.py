## Read Mode
# f = open('test.txt', 'rt')

# # print(f.read(15))
# # print(f.readline())
# # print(f.readline())

# for line in f:
#     print(line)


# f.close()



## Append Mode
# f = open('test.txt', 'a')
# f.write('this is new text added by python file')
# f.close()

# # Open and read the file after the appending
# f = open('test.txt', 'r')
# print(f.read())
# f.close()

f = open('random.txt', 'x')
f.write('hello world')
f.close()