#AMALYOT
#1 - Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va 
# ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
#2 - Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
#3 - Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing
from uuid import uuid4
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odmalar_soni=0
    def __init__(self,ism,familiya,tyil):
        """Shaxsning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        Shaxs.__odmalar_soni+=1
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"{self.tyil} - yil tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxsni yoshini qaytaruvchi method"""
        return yil - self.tyil
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odmalar_soni
shaxs1=Shaxs("Murod","Qayumov",1993)
shaxs2=Shaxs("Nilufar","Xayitova",2000)
class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni=0
    def __init__(self, ism, familiya,tyil,passport,bosqich):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, tyil)
        self.__bosqich=bosqich
        self.__passport=passport
        self.__idraqam=uuid4()
        Talaba.__talabalar_soni+=1
    def get_bosqich(self):
        return self.__bosqich
    def get_passport(self):
        return self.get_passport
    def get_id(self):
        return self.__idraqam
    def add_bosqich(self):
        self.__bosqich+=1
        return self.__bosqich
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"{self.tyil} - yil tug'ilgan. {self.__bosqich} - kurs talabasi"
        return info
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
talaba1=Talaba("Sabohat","Qayumova",2001,"AB6480535",2)
talaba2=Talaba("Madina","Bobomurodova",1995,"AB6743592",3)
print(Talaba.get_talabalar_soni())
print(Shaxs.get_odamlar_soni())
print(talaba1.get_info())
print(talaba1.get_id())
print(talaba2.get_info())
print(talaba2.get_id())
talaba1.add_bosqich()
talaba2.add_bosqich()
print(talaba1.get_info())
print(talaba2.get_info())