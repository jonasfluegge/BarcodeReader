# Project: SimpleBarcodeReader
# Author: Jxnasnet
# Version: 1.0

# Imports
import cv2
from pyzbar.pyzbar import decode

# Methode, um Barcode zu dekodieren
def BarcodeReader(image):
    img = cv2.imread(image)

    detectedBarcodes = decode(img)

    if not detectedBarcodes:
        # Fehlermeldung bei falschem Barcode
        print("Barcode nicht erkannt oder der Barcode ist leer bzw. beschädigt!")
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Ergebnisse ausgeben
                print(barcode.data)
                print(barcode.type)

# Pfad zum Bild mit Barcode
image = input("Pfad zum Bild inkl. Name: ")
BarcodeReader(image)
