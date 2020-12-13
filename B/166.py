N, K = list(map(int, input().split()))
person = []
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    person.extend(a)

all_person = [i for i in range(1, N + 1)]

diff = list(set(all_person) - set(person))
    
result = len(list(set(diff)))
print(result)