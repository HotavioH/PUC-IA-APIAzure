#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


camera = cv2.VideoCapture(0)
file = ('imagens/fotocamera.png')
print("Aperde 's' para tirar uma foto ou 'e' para sair")
while True:
        retval, img = camera.read()
        cv2.imshow('Câmera',img)     
        k = cv2.waitKey(30)     
        if k == ord('s'):
            cv2.imwrite(file,img)
            break

        elif k == ord('e'):
            break     
camera.release()
cv2.destroyAllWindows()
