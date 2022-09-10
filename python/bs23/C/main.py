

length_s = int(input())
left_s = input()
right_s = input()


pair_n = 0
pairs = []
for i in range(len(left_s)):
    for j in range(len(right_s)):
        if left_s[i] == right_s[j]:
            pairs.append(str(i+1) + ' ' + str(j+1))
            pair_n = pair_n + 1
        elif left_s[i] == '?' or right_s[j] == '?':
            pairs.append(str(i+1) + ' ' + str(j+1))
            pair_n = pair_n + 1

print(pair_n)
for pair in pairs:
    print(pair)