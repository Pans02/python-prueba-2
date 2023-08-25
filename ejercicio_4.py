dic = {}
total = 0
while True:
  producto = input("Ingrese el articulo que desea comprar: ")
  precio = int(input("Ingrese el precio del articulo: "))
  dic[producto] = precio
  total = total + precio
  opcion = int(input("¿Desea añadir otro articulo? 1-Si 2-No: "))
  if (opcion == 2):
    break
dic["Total"] = total
print("\nLista de compras:\n--------------------")
for key, values in dic.items():
  print(key, ": ", values)
