g = [4, 2, 6, 1, 8]
s = [2, 3, 1, 2, 4, 7]
count = 0
n = len(g)
m = len(s)
g.sort()
s.sort()
left = 0
right = 0
while left < n and right < m:
    if g[left] <= s[right]:
        count += 1
        left += 1
    right += 1
print(count)
