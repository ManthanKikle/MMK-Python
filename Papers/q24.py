message = input()
count =0
vowles = "aeiou"

message_clean = message.lower()

for chars in message_clean:
    if chars in vowles:
        count += 1

print(message)
print(f"The total vowels are: {count}")