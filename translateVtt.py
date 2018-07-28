import translate.cgt as traductor
import random
import os.path as path

print("Bienvenido a la traduccion automatica de archivos vtt\n\n")

separador = "@-.-@"
separador_mod = "@ -.- @"
ruta_archivo = input("Ingrese el nombre del archivo a traducir: ")

print("intentado abrir archivo: ", ruta_archivo)

archivo = open(ruta_archivo, "r", encoding='utf-8')


contador = 1
subconta = 0
traduccion = ""
elemento_a_traducir = ""
fNumero = False
fTimeLine = False

for linea in archivo.readlines():
    cadena_comp = linea.replace(' ', '')
    cadena_comp = cadena_comp.replace('\n', '')
    if(str(contador) == cadena_comp and fNumero == False):
        traduccion += linea.replace(' ', '')
        contador += 1
        fNumero = True
    elif(fNumero == True and fTimeLine == False):
        traduccion +=linea + "{"+ str(subconta) +"}\n"
        subconta += 1
        fTimeLine = True
    elif(fNumero == True and fTimeLine == True):
        if(linea != "\n"):
            elemento_a_traducir  += linea + " \n"
        else:
            elemento_a_traducir +=  separador + linea
            fNumero = False
            fTimeLine = False

archivo.close()


elemento = traductor.cgt()
resultado = elemento.obtener_traduccion(elemento_a_traducir)

prueba2 = resultado.split(separador_mod)[:subconta]

for i in range(len(prueba2)-1):
    prueba2[i] = prueba2[i].strip()
    prueba2[i]  = prueba2[i] + "\n"

reemplazo = traduccion.format(*prueba2)


archivo_resultado = ruta_archivo.split(".")[0] + str(random.randrange(9999)) + "." + ruta_archivo.split(".")[1]

archivo = open(archivo_resultado, "w", encoding='utf-8')
archivo.write(reemplazo)
archivo.close()



