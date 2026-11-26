text = input().split()

words = []
numbers = []

for items in text:
    if items.isdigit():
        numbers.append(int(items))
    else:
        words.append(items)

print(f"Words: {" ".join(words).upper()}, Word count: {len(words)}, Number count: {len(numbers)}, Sum: {str(sum(numbers))}, Lagest: {max(numbers)}")