marks = {
    "Arjun": [85, 90, 92],
    "Bhavya": [78,81,85],
    "Charan": [95, 92, 88]
}

highest = 0
topper = ''

for names in marks:
    total = 0
    for i in marks[names]:
        total += i
    avg = total/len(marks[names])

    if avg > highest:
        highest = avg
        topper = names


print(highest)
print(topper)