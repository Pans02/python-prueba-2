def palindromo(palabra):
  palabra=palabra.replace(" ","")
  palabra=palabra.lower()
  reves=palabra[::-1]
  if(palabra==reves):
    return True
  else:
    return False
palabra=input("Ingrese la palabra para saber si es palindromo(minimo 3 caracteres): ")
while(len(palabra)<3):
  print("ERROR: La palabra ingresada NO cumple con las condiciones")
  palabra=input("Ingrese la palabra para saber si es palindromo(minimo 3 caracteres): ")
if(palindromo(palabra)):
  print("Es palindromo")
else:
  print("No es palindromo")
