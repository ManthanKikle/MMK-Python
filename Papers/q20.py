speed = list(map(int, input().split()))

def speed_sorted(speed):
    Sorted_speed = list(set(speed))
    Sorted_speed.sort(reverse=True)

    if len(Sorted_speed) < 2:
        print("Not enough data")

    return Sorted_speed[1]

print(speed_sorted(speed))