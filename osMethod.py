import os

#Absolute and relative paths
print(os.path.abspath('file.txt'))

print(os.path.isabs("C:\\Users\\Manthan Kikle\\Desktop\\repos\\Python\\python-Questions\\file.txt"))
print(os.path.isabs("\\Manthan Kikle\\Desktop\\repos\\Python\\python-Questions\\file.txt"))

print(os.path.relpath("C:\\Users\\Manthan Kikle\\Desktop\\repos\\Python\\python-Questions\\file.txt", "C:\\Users\\Manthan Kikle"))

#File and Folder Information

print(os.path.getsize("file.txt"))
print(os.listdir("."))
print(os.path.exists("File1.txt"))
print(os.path.isfile("File1.txt"))
print(os.path.isdir("File1.txt"))
