file= open('text.txt')
line= file.readline()
while line!="":
    print(line)
    line = file.readline()

#how to read a file using readlines
#values = [abc, decf, "cat", dog, 5]
for line in file.readlines():
    print(line)

file.close()
#print line by line using readline method
