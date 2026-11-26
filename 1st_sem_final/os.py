import os

os.rename("osFile.txt", "osRenamed.txt")
os.remove("osremove.txt")

os.mkdir("osFolder")
print(os.getcwd())
os.rmdir("osFolder")