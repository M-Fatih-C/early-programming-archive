# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 02:27:50 2023

@author: Muhammet Fatih
"""

def faktoriyel_hesapla(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel_hesapla(n - 1)

try:
    sayi = int(input("Faktöriyellerini hesaplamak istediğiniz üst sınıra bir sayı girin: "))
    if sayi < 0:
        print("Negatif sayıların faktöriyeli tanımlı değildir.")
    else:
        for i in range(sayi + 1):
            faktoriyel = faktoriyel_hesapla(i)
            print(f"{i}! = {faktoriyel}")
except ValueError:
    print("Geçersiz bir sayı girdiniz. Lütfen bir tam sayı girin.")
