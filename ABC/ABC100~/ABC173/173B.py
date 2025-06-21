N = int(input())
cnt = [0,0,0,0]
word = ["AC","WA","TLE","RE"]
for i in range(N):
    S = input()
    if S == "AC":
        cnt[0] += 1
    elif S == "WA":
        cnt[1] += 1
    elif S == "TLE":
        cnt[2] += 1
    else:
        cnt[3] += 1

for i in range(4):
    print(word[i] + " x " + str(cnt[i]))