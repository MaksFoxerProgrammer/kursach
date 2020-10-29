b = []
num = int(input())
p = int(input())
while num >= 1:
	b += num % p
	num //= p
for i in reversed(b):
	print(i,end="")