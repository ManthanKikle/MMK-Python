count = 0
good = []

with open("feedback.txt", "r") as infile:
    for line in infile:
        review = line.lower()
        if review == 'bad' or review == 'poor':
            count += 1
        else:
            good.append(line)

with open("good_reviews.txt", "w") as outfile:
    for line in good:
        outfile.write(line)


print(count)
    
