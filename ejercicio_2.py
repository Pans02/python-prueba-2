while True:
  opcion = int(
    input(
      "¿Que conversion desea realizar?: \n 1) kilometros->Millas \n 2) Millas->Kilometros\n 3) Kilogramos->Libras \n 4) Libras->Kilogramos \n 5) Celcius->Farenheit \n 6) Farenheit->Celsius \n 7) Salir  \n (Ingrese el numero de la operacion a realizar)\n:"
    ))
  
  if(opcion==1):
    num = float(input("Ingrese el valor en KM que desea convertir a Mi: "))
    print("El resultado de la conversion es de: ",num/1.60934)
  
  elif(opcion==2):
    num = float(input("Ingrese el valor Mi que desea convertir a KM: "))
    print("El resultado de la conversion es de: ",num/0.621371)
  
  elif(opcion==3):
    num = float(input("Ingrese el valor en Kg que desea convertir a Lb: "))
    print("El resultado de la conversion es de: ",num/0.453592)
  
  elif(opcion==4):
    num = float(input("Ingrese el valor en Lb que desea convertir a Kg: "))
    print("El resultado de la conversion es de: ",num/2.20462)
  
  elif(opcion==5):
    num = float(input("Ingrese el valor en °C que desea convertir a °F: "))
    resultado=(9/5)*num+32
    print("El resultado de la conversion es de: ",resultado)
  
  elif(opcion==6):
    num = float(input("Ingrese el valor en °F que desea convertir a °C: "))
    resultado=(5/9)*(num-32)
    print("El resultado de la conversion es de: ",resultado)  
  
  elif(opcion==7):
    break
  
  else:
    print("ERROR AL INGRESAR LA OPCION")
