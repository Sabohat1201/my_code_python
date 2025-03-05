class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. ".title()
        info += f"Passport: {self.passport}, {self.tyil} - yil tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxsni yoshini qaytaruvchi method"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
#POLYMORPHISM
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} ".title()
        info += f"{self.bosqich} bosqich. ID raqami {self.idraqam}"
        return info

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil=f"{self.viloyat.capitalize()} , {self.tuman.title()} tumani, {self.kocha.title()} ko'chasi, {self.uy} uy."
        return manzil

talaba_manzil=Manzil("8","normuhammedov","Yashnobod","Toshkent shahar")
talaba=Talaba("Sabohat","Qayumova","AB6480535",2001,"FU0867963",talaba_manzil)

#print(talaba.manzil.get_manzil())
#print(talaba.get_info())
# print(talaba.get_id())
# print(talaba.get_bosqich())
# print(talaba.get_info())
# print(talaba.get_age(2025))

