import cv2

with open('permitidos.txt') as f:
	datos = f.read().splitlines()

cap = cv2.VideoCapture(0)


detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()  #Lee los datos
    data, bbox, _ = detector.detectAndDecode(img) #Lee los datos dentro del qr y las coordenadas del mismo (esquinas)
    if(bbox is not None):
        xa=(int(bbox[0][0][0]))
        xb=(int(bbox[0][1][0]))
        xc=(int(bbox[0][2][0]))
        xd=(int(bbox[0][3][0]))
        ya=(int(bbox[0][0][1]))
        yb=(int(bbox[0][1][1]))
        yc=(int(bbox[0][2][1]))
        yd=(int(bbox[0][3][1]))
        #Toma la posición de cada una de las esquinas del qr#
        
        cv2.line(img, (xa,ya),(xb,yb), (160,20,70), thickness=4)
        cv2.line(img, (xa,ya),(xd,yd), (160,20,70), thickness=4)
        cv2.line(img, (xd,yd),(xc,yc), (160,20,70), thickness=4)
        cv2.line(img, (xb,yb),(xc,yc), (160,20,70), thickness=4)
        #Crea lineas entre las esquinas adyacentes, puede hacerse con un for, pero no es necesario
        if data:
            if data not in datos:
                cv2.putText(img, "No permitido", (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (34,0,227), 2) #Si el dato no existe lo pongo en rojo
                
 
                

            else:
                cv2.putText(img, "Permitido", (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (60, 107, 0), 2) #Si el dato existe en la lista lo pongo en verde
                

    cv2.imshow("Codigo QR", img) #Cambio el nombre de la ventana
    
    if(cv2.waitKey(1) == ord("q")): #Comando para salir del programa
        break



cap.release()
cv2.destroyAllWindows()
