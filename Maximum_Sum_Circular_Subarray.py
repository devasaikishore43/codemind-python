def lastone(a, n):
	if (n == 1):
		return a[0]
	sum1 =sum(a)
	cm = a[0]
	ma = a[0]
	ci = a[0]
	mn = a[0]
	for i in range(1, n):
		cm = max(cm + a[i], a[i])
		ma = max(ma, cm)
		ci = min(ci + a[i], a[i])
		mn = min(mn, ci)
	if (mn == sum1):
		return ma
	return max(ma, sum1 - mn)
n=int(input())
a=list(map(int,input().split()))
print(lastone(a, n))