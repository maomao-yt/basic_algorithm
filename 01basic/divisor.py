#約数の列挙
N = int(input())

def get_divisorts(N):
    if N < 1:
       return

    ans =[]
    i = 1
    while i*i <= N:
        if N % i == 0:
          ans.append(i)
          if i * i != N:
              ans.append(int(N/i))
        i += 1

    return sorted(ans)
nums =get_divisorts(N)
for ans in nums:
    print(ans)
