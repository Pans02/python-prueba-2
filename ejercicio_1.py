def primo(num):
  for i in range(2,num//2+1):
    if(num%i==0):
      return False
    else:
      return True
    
numero=int(input("Ingrese el numero que desea comprobar si es primo o no: "))
if(primo(numero)):
  print("Es primo")
else:
  print("No es primo")
