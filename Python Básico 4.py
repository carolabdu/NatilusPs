soma = 0
def prime(k):
    for x in range(2,int(k ** (1 / 2)) + 1):
      if k % x == 0: return False
    return True

for x in range (2,1000):
  if prime(x) == True:
    soma += x

print (soma)
