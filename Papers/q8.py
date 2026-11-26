name = input("Enter your name: ")
last_name = input("Enter your Last name: ")
year = input("Enter the Year: ")

part1 = name[:2].upper()
part2 = last_name[-2:].lower()
part3 = str(len(name+last_name))
part4 = year[-2:]

password = part1+part2+part3+part4

print(password)