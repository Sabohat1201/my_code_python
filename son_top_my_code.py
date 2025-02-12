import random as r
print("Keling o'ylagan sonni topish o'ylaymiz!!")
def son_top(x):
    son=r.choice(list(range(1,x+1)))
    print(f"1 dan {x} gacha son o'yladim. Topa olasanmi?")
    taxmin_son=0
    while True:
        oylagan_son=int(input(">>>"))
        taxmin_son +=1
        if oylagan_son>son:
            print("Xato men o'ylagan son bundan kichiqroq. Yana harakat qiling")
        elif oylagan_son<son:
            print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling")
        else:
            print(f"Siz {taxmin_son} ta taxmin bilan topdingiz")
            return taxmin_son
       


def son_top_pc(y=10):
    print(f"1 dan {y} son o'ylang. Men topishga harakat qilaman!")
    print(input("Son o'ylagan bo'lsangiz istalgan tugmani bosing"))
    taxmin_son2=0
    past,yuqori=1,y
    while True:
        tasodif_son=(past + yuqori)//2
        oylangan_son=input(f"Siz {tasodif_son} ni o'yladingiz: to'g'ri T, men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)??").strip().upper()
        taxmin_son2+=1
        if  oylangan_son=='-':
            yuqori=tasodif_son-1
        elif oylangan_son == '+':
            past=tasodif_son+1
        elif oylangan_son == 'T':
            print(f"Soningizni {taxmin_son2} ta taxmin bilan topdim")
            return taxmin_son2
        else:
            print("Iltimos, faqat 'T', '+', yoki '-' ni kiriting")
            
        
#TAQQOSLASH
t_son=son_top(10)
t2_son=son_top_pc(10)
while True:
    if t_son<t2_son:
        print(f"Siz {t_son} taxmin bilan topdingiz va yutdingiz!")
    elif t_son>t2_son:
        print(f"Soningizni {t2_son} taxmin bilan topdim va yutqazdingiz")
    else:
        print(f"Durrang! Ikkimiz ham {t2_son} ta taxmin bilan topdik!")

    savol=input("Yana o'ynaymizmi? (ha/yo'q)")
    if savol == 'ha':
        t_son=son_top(10)
        t2_son=son_top_pc()
    elif savol == 'yo\'q':
        print("O'yin tugadi!😊")
        break




    

