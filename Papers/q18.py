message = "welcome to python"
freq = {}

for chars in message:
    if chars == " ":
        continue
    if chars in freq:
        freq[chars] = freq[chars]+1
    else:
        freq[chars] = 1

sorted_freq = {}
for key in sorted(freq):
    sorted_freq[key] = freq[key]

print(sorted_freq)