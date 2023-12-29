n,k,T = input().split()


words = []
for i in range(int(n)):
    word = input()
    if T in word:
        words.append(word)

words.sort()
print(words[int(k)-1])