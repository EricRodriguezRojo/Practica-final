trabajadores = input("Numero trabajadores? ")
num_trabajadores=int(trabajadores)
print(num_trabajadores)
hora_referencia = input("selecciona hora  de referencia(0-23): ")

if hora_referencia < 0:
    print("La hora de referncia es incorrecta")
    exit()
elif hora_referencia > 23:
    print("La hora de referncia es incorrecta")
else:
    print("La hora de referncia es: " + str(hora_referencia))
num_trbjs_hora_ref = 0

while num_trabajadores > 0:
    nombre_empleado = input("Nombre del empleado: ")
    hora_entrada = input("Hora de entrada: ")
    hora_salida = input("Hora de salida: ")


    if hora_entrada < hora_salida:
        print("hora correcta!")
        num_trabajadores = num_trabajadores-1
    else:
        print("hora incorrecta, Vuelve a intentarlo!")    

    if hora_referencia >= hora_salida:
        num_trbjs_hora_ref = num_trbjs_hora_ref+1

    if (num_trabajadores != 0):
        print("Numero de trabajadores restantes para añadir: "+ str(num_trabajadores))

else:
    if num_trbjs_hora_ref == 0:
        print("No hay trabajadores que han salido a la hora de referencia o antes.")    
    elif num_trbjs_hora_ref == 1:
        print("Han salido antes o igual a la hora de refencia " + str(num_trbjs_hora_ref) + " trabajador!")    
    else:
        print("Han salido antes o igual a la hora de refencia " + str(num_trbjs_hora_ref) + " trabajadores!")    

print("fin! :D")

