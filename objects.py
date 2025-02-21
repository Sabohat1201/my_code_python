class Student:
    def __init__(self,name,lastname,y_of_birth):
        self.name=name
        self.lastname=lastname
        self.years_of_birth=y_of_birth
        self.year=1
    def set_year(self,new_year):
        """Talabaning bosqichini yangilaydigan metod"""
        self.year=int(new_year)
    def update_year(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.year+=1
    def get_name(self):
        return self.name
    def get_lastname(self):
        return self.lastname
    def get_age(self,year):
        return year-self.years_of_birth
    def introduce(self):
        return f"Men {self.lastname} {self.name}, {self.years_of_birth} - yil tug'ilganman.{self.year} - bosqich talabasi"
    def get_fullname(self):
        """Talaba haqida malumot"""
        return f"{self.name} {self.lastname} "
    
student1=Student("Sabohat","Qayumova",2001)
student2=Student("Madina","Bobomurodova",1995)
# print(student1.year)
# student1.update_year()
# student2.set_year(4)
# print(f"{student1.year} {student2.year}")
class Science:
    """Fan nomli klass"""
    def __init__(self,name):
        self.name=name
        self.number_of_students=0
        self.students=[]

    def add_students(self,talaba):
        """Fanga talabalar qo'shing"""
        self.students.append(talaba)
        self.number_of_students+=1
  
    def get_students(self):
        return [student.get_fullname() for student in self.students]

# matem=Science("Oliy matematika")
# matem.add_students(student1)
# matem.add_students(student2)
# matematika=matem.get_students()
# print(matematika)
# print(matem.number_of_students)

#DUNDER metodlar
#print(dir(Student))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
# print(see_methods(Student))
# print(see_methods(Science))
# print(student1.__dict__)
# print(student1.__dict__.keys())

#AMALYOT
#1 - Avto degan yangi klass yarating. 
# Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. 
# Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
class Avto:
    """Avtomobil nomli klass"""
    def __init__(self,model,rang,korobka,narx):
        """Avtomobil xususiyatlari"""
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.kilometr=0
#2 - Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
    def get_info(self):
        """Avtomobil ma'lumotlarini qaytaruvchi funksiya"""
        return f"Modeli: {self.model}. Rangi {self.rang}. Korobkasi {self.korobka}. Narxi {self.narx}. Kilometr {self.kilometr} ga teng."

#3 - Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    def set_kilometr(self,new_kilometr):
        """Kilometrni yangilaydigan funksiya"""
        self.kilometr=new_kilometr
    def update_km(self):
        """Kilometrni 1 ga ko'paytiradi"""
        self.kilometr += 1

#4 - Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
class YangiAvtosalon:
    """Yangi avtosalon nomli klass"""
    def __init__(self,salon_nomi,manzili):
        """Yangi avtomobillar xususiyatlari"""
        self.salon_nomi=salon_nomi
        self.manzili=manzili
        self.sotuvdagi_avtomobillar=[]
#5 - Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
    def add_new_avto(self,avto):
        """Yangi avtomobillar qo'shuvchi funksiya"""
        self.sotuvdagi_avtomobillar.append(avto)
#6 - Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    def get_info2(self):
        """Yangi avtosalondagi avtomobillar haqida ma'lumot"""
        return [avto.get_info() for avto in self.sotuvdagi_avtomobillar]
    def see_methods(klass):
        """Methodlarni chiqarish"""
        return [method for method in dir(klass) if method.startswith('__') is False ]
#7 - Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

avto1=Avto("malibu","qora","avtomat",150000)
avto2=Avto("cobolt",'oq','mexanik',12000)
# avto_sex=YangiAvtosalon("SabohatAvto","Yashnobod")
# avto1.set_kilometr(4)
# avto_sex.add_new_avto(avto1)
# avto_sex.add_new_avto(avto2)
# print(avto_sex.get_info2())
# print(avto1.get_info())
# avto1.update_km()
# print(avto1.get_info())

#8 - dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan 
# va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping 
# (dir(str), dir(int) va hokazo)
print(see_methods(Avto))
print(see_methods(YangiAvtosalon))
print(avto1.__dict__)
print(avto2.__dict__)