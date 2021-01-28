# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:24:08 2021

@author: saban.m
"""

def dogrusal_arama(liste_array: list, hedef: int) -> int:
    for index, item in enumerate(liste_array):
        if item == hedef:
            return index
    return -1    

    
if __name__ == "__main__":
    liste = input("Numaraları virgül ile ayırarak giriniz:\n").strip()
    liste_array = [int(item.strip()) for item in liste.split(",")]  #array 'e çeviriyoruz virgül ile ayırarak ve sol ve sağındaki boşlukları siler
    
    
    hedef = int(input("Listede aranacak bir sayı girin:\n").strip())

    result = dogrusal_arama(liste_array, hedef)    
    if result != -1:
        print(result)
        print("Dogrusal arama listesi: {} , Hedef: {} , kaçıncı sırada bulundu: {} ".format(liste_array,hedef,result+1))
    else:
        print("{} sayısı {} listesi içinde bulunamadı".format(hedef,liste_array))
    