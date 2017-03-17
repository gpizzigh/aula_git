n=int(input("Digite o maximo de numeros:"))
def ler_numeros(n):
  l=[]
  for i in range(n):
  	x=float(input("Digite os numeros:"))
  	#l=[]
  	l.append(x)
  	i=i+1
  return l
print(ler_numeros(n))
   