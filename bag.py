B = [1, 50, 90]
S = 100
inf = 10 ** 6
F = [0] + [inf] * S
Prev = [-1] * (S + 1)
for i in range(1, S + 1):
    for j in range(len(B)):
        if i - B[j] >= 0 and F[i - B[j]] < F[i]:
            F[i] = F[i - B[j]]
            Prev[i] = B[j]
    F[i] += 1
Ans = []
while S > 0:
    Ans.append(Prev[S])
    S -= Prev[S]
print(Ans)
