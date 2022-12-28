'''
1.Crea una nueva carpeta denominada edu-ws en tu carpeta Documentos.
2.Cambia el workspace para que apunte a este nuevo directorio.
3.Genera un nuevo proyecto python con la estructura adecuada (nombre de tu elección) y al menos dos archivos de código fuente en python.
4.En uno de los archivos pega el siguiente código y a continuación, realiza varias capturas de tu entorno de ejecución en modo depuración mostrando el contenido de las variables.
5.Evalúa una de las expresiones booleanas durante la ejecución en modo depuración.
6.Incluye las capturas en el directorio del proyecto y expórtalo comprimido con tu nombre y apellidos. 
7.Por último, súbelo a la plataforma.
'''
def es_primo(numero):
    esPrimo = True
    
    if numero > 2:
        for i in range(2, numero):
            if numero%i==0:
                esPrimo = False
                
    return esPrimo


for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    print(i, es_primo(i))