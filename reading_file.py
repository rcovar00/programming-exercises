file = open('test.txt')

# print file.read()
for i in range(4):
    print file.readline()

file.close()
