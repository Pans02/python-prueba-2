palabra=input("Ingresa la palabra que desee: ")
letra=input("Ingrese la letra que quiere buscar: ")
cont=0
for i in palabra:
  if(i==letra):
    cont=cont+1
print("La letra ",letra," Se encuentra ",cont," en la palabra")
