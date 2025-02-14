from uzwords import words
import random as r
print("Мен 5 хонали сон уйладим. Топа оласизми?\n _ _ _ _ _")


sozlar=[]
for n in words:
    if len(n)==5:
        sozlar.append(n)
tanlangan_soz=r.choice(sozlar)
def get_words(soz):
    return list(soz)
soz=tanlangan_soz.lower()
harflar=get_words(soz)
print(harflar)
def display(soz=tanlangan_soz):
    soz_top=['_','_','_','_','_']
    kiritgan_harflar=set()
    taxminlar=0
    while '_' in soz_top:
        harf_kiritish=input("Харф киритинг: ")
        if harf_kiritish in kiritgan_harflar:
            print("Бу харфни аввал киритгансиз.Бошкасини киритинг.")
            print(f"Шу вактгача киритган харфларингиз {kiritgan_harflar} ")
            continue
        kiritgan_harflar.add(harf_kiritish.lower())
        taxminlar+=1
        if harf_kiritish in harflar:
            print(f"{harf_kiritish} харфи тугри!")
            for n in range(5):
                if harflar[n]==harf_kiritish:
                    soz_top[n]=harf_kiritish
            print(soz_top)
            print(f"Шу вактгача киритган харфларингиз {kiritgan_harflar} ")
        else:
            print("Бундай харф йук!")
            print(soz_top)  
            print(f"Шу вактгача киритган харфларингиз {kiritgan_harflar} ")
            continue
    print(f"Табриклаймиз! {soz} сузини {taxminlar} та тахмин билан топдингиз!")      
    return soz_top
print(display())
