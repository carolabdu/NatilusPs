n =input('Digite um número:')
t= len(n)
if t%2== 0:
    a= n[0:t//2]
    b=n[-1:t//2-1:-1]
if t%2!= 0:
    a = n[0:t // 2]
    b = n[-1:t // 2 :-1]
print(n, 'é palíndromo?',a==b)
