n = int(input())
m = list(map(int,input().split()))
low = min(m)
result = m.index(low)
print("Dealer"+str(result))