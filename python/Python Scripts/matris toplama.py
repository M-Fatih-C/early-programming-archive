# -*- coding: utf-8 -*-

def matris_topla(matris1, matris2):
    satir = len(matris1)
    sutun = len(matris1[0])
    
    if len(matris2) != satir or len(matris2[0]) != sutun:
        return None  # Matrislerin boyutları uyuşmuyorsa toplama yapılamaz
    
    sonuc = []
    for i in range(satir):
        satir_sonuc = []
        for j in range(sutun):
            toplam = matris1[i][j] + matris2[i][j]
            satir_sonuc.append(toplam)
        sonuc.append(satir_sonuc)
    
    return sonuc

# İki örnek matris
matris1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matris2 = [
    [5, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

toplam_matris = matris_topla(matris1, matris2)

if toplam_matris is None:
    print("Matris boyutları uyuşmuyor. Toplama yapılamaz.")
else:
    print("Toplam Matris:")
    for satir in toplam_matris:
        print(satir)
