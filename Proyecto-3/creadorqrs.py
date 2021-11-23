import qrcode
from random import randint
from PIL import Image
n=int(input("Cuantos códigos?: "))
archivo = open('permitidos.txt', 'a') #Abro el txt
for i in range(n):
    Cedula=randint(100000000, 800000000) #Creo un numero aleatorio
    print(Cedula)#Lo muestro, este paso es innecesario, solo es de prueba
    archivo.write(str(Cedula)) 
    archivo.write("\n")#Lo creo y añado el archivo
    archivo.close
    qr = qrcode.QRCode( 
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )#Creo el qr
    qr.add_data(Cedula) #Añado el dato al qr
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save(str(Cedula)+".png") #Creo la imagen


    