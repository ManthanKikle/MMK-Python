#String Indexing and Slicing

s = "abcdefgh"
thrid_char = s[2]
print(thrid_char)

subset = s[2:5]
print(s)

subset_staring = s[:3]
subset_ending = s[3:]

print(subset_staring)
print(subset_ending)

#String Method

str = "Hello my name is MMK"
print(str.upper())
print(str.lower())
print(str.split())
print(str.join(str.split()))
print(str.replace("Hello","Hi"))
print(str.count('o'))
print(str.find('my'))