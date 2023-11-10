#Creo una función de temperatura media
def temperatura_media(temperaturas):
    total=sum(temperaturas)
    media=total/7
    return media
#Creo una función para definir el día de máxima temperatura
def dia_de_maximo(temperaturas):
    temp_max=max(temperaturas)
    if temp_max == temperaturas[0]:
        return "día 1"
    elif temp_max==temperaturas[1]:
        return "día 2"
    elif temp_max==temperaturas[2]:
        return "día 3"
    elif temp_max==temperaturas[3]:
        return "día 4"
    elif temp_max==temperaturas[4]:
        return "día 5"
    elif temp_max==temperaturas[5]:
        return "día 6"
    elif temp_max==temperaturas[6]:
        return "día 7"
    else:
        print("Ha habido un error, intentalo de nuevo")
#Creo una función para especificar si la temperatura de esa semana ha oscilado entre los 20 y los 25 grados
def mild(temperaturas):
    if 20<=temperaturas[0]<=25 and 20<=temperaturas[1]<=25 and 20<=temperaturas[2]<=25 and 20<=temperaturas[3]<=25 and 20<=temperaturas[4]<=25 and 20<=temperaturas[5]<=25 and 20<=temperaturas[6]<=25:
        print("Esta semana la temperatura ha estado entre los 20 y los 25 grados Celsius.")
    else:
        pass
#Creo una función para ver cuanto ha subido o bajado la temperatura cada día a lo largo de la semana
def fluctuación(temperaturas):
    día_uno=temperaturas[0]-temperaturas[0]
    día_dos=temperaturas[1]-temperaturas[0]
    día_tres=temperaturas[2]-temperaturas[1]
    día_cuatro=temperaturas[3]-temperaturas[2]
    día_cinco=temperaturas[4]-temperaturas[3]
    día_seis=temperaturas[5]-temperaturas[4]
    día_siete=temperaturas[6]-temperaturas[5]

    if día_uno < 0:
        temperatura = día_uno*-1
        print("La temperatura ha bajado", temperatura,"grados Celsius el día uno.")
    elif día_uno>0:
        print("La temperatura ha subido", día_uno,"grados Celsius el día 1.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 1.")

    if día_dos < 0:
        temperatura2 = día_dos*-1
        print("La temperatura ha bajado", temperatura2,"grados Celsius el día 2.")
    elif día_dos>0:
        print("La temperatura ha subido", día_dos,"grados Celsius el día 2.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 2.")

    if día_tres < 0:
        temperatura3 = día_tres*-1
        print("La temperatura ha bajado", temperatura3,"grados Celsius el día 3.")
    elif día_tres>0:
        print("La temperatura ha subido", día_tres,"grados Celsius el día 3.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 3.")

    if día_cuatro < 0:
        temperatura4 = día_cuatro*-1
        print("La temperatura ha bajado", temperatura4,"grados Celsius el día 4.")
    elif día_cuatro>0:
        print("La temperatura ha subido", día_cuatro,"grados Celsius el día 4.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 4.")

    if día_cinco < 0:
        temperatura5 = día_cinco*-1
        print("La temperatura ha bajado", temperatura5,"grados Celsius el día 5.")
    elif día_cinco>0:
        print("La temperatura ha subido", día_cinco,"grados Celsius el día 5.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 5.")

    if día_seis < 0:
        temperatura6 = día_seis*-1
        print("La temperatura ha bajado", temperatura6,"grados Celsius el día 6.")
    elif día_seis>0:
        print("La temperatura ha subido", día_seis,"grados Celsius el día 6.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 6.")

    if día_siete < 0:
        temperatura7 = día_siete*-1
        print("La temperatura ha bajado", temperatura7,"grados Celsius el día 7.")
    elif día_siete>0:
        print("La temperatura ha subido", día_siete,"grados Celsius el día 7.")
    else:
        print("La temperatura no ha subido ni ha bajado el día 7.")

#especfico las temperaturas a lo largo de los días de las diferentes semanas
temperatura_semana_1=[22,24,19,21,25,23,20]
temperatura_semana_2=[20,22,21,23,24,22,21]
temperatura_semana_3=[23,21,20,22,24,25,23]
#Escribo los resultados
print("La temperatura media de la semana uno es de", temperatura_media(temperatura_semana_1),"grados Celsius. El día de máxima temperatura ha sido el", dia_de_maximo(temperatura_semana_1))
mild(temperatura_semana_1)
print("La fluctuación en la semana 1 ha sido la siguiente:")
fluctuación(temperatura_semana_1)

print("La temperatura media de la semana dos es de", temperatura_media(temperatura_semana_2),"grados Celsius. El día de máxima temperatura ha sido el", dia_de_maximo(temperatura_semana_2))
mild(temperatura_semana_2)
print("La fluctuación en la semana 2 ha sido la siguiente:")
fluctuación(temperatura_semana_2)

print("La temperatura media de la semana tres es de", temperatura_media(temperatura_semana_3),"grados Celsius. El día de máxima temperatura ha sido el", dia_de_maximo(temperatura_semana_3),)
mild(temperatura_semana_3)
print("La fluctuación en la semana 3 ha sido la siguiente:")
fluctuación(temperatura_semana_3)