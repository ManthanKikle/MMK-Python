n = list(map(int, input().split()))
sortedN = list(set(n))
sortedN.sort(reverse=True)
print(sortedN)