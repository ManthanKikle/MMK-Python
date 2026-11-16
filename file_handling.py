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
    file.seek(0)


#File Positions

file_path = 'file.txt'

with open(file_path, 'r') as fileobj:
    content1 = fileobj.read(5)
    print(content1)
    current_pointer = fileobj.tell()
    print(current_pointer)
    fileobj.seek(0)

with open(file_path,'rb') as fileobj:
    fileobj.seek(2,1)
    print(fileobj.read())


file = open('file2.txt', 'w')
letters = ['a', 'b', 'c', 'a', 'bb', 'ccc']
file.writelines(letters)
file.close

with open('file2.txt', 'rb') as a:
    with open('file3.txt', 'wb') as b:
        content = a.read(10)
        b.write(content)
        print(b.read)


    
