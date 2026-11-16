#Opening files

file = open("file.txt","rb")
print(file)

#file object attributes

file = open('file.txt',"wb")
print(file.name)
print(file.closed)
print(file.mode)

file.close()
print(file.closed)

#Writing to files

file = open('file.txt','w+')
file.write("Hello my name is MMK")
file.seek(0)
print(file.read())
file.close()

file = open('file.txt', 'w+')
lst = ['a','b','c','d']
file.writelines(lst)
file.seek(0)
print(file.read())
file.close()

#append
file = open('file.txt', 'a+')
file.write("\n Hello to python")
file.close()

#readline
file = open('file.txt', 'r')
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(list(file))
file.close()

#using loops 
file = open('file.txt','r')
file.seek(0)
for line in file:
    print(line)
file.close()

#Open with

with open('file.txt', 'r') as file:
    print(file.read())

#splitting words

with open('file.txt','r') as file:
    line = file.readline()
    words = line.split()
    print(words)