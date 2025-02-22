#AMALYOT
#1 - Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. 
# Bu xususiyat parametr sifatida uzatilmasin va 
# obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
#2 - Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passpord,tyil):
        """Shaxsning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.passpord=passpord
        self.tyil=tyil
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"passport: {self.passpord}, {self.tyil} - yil tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxsni yoshini qaytaruvchi method"""
        return yil - self.tyil
class Fan:
    """Fan klassi"""
    def __init__(self,fan_nomi):
        """Fanlarning xususiyatlari"""
        self.fan_nomi=fan_nomi

    def get_science_name(self):
        """Fan nomini chiqarish"""
        return self.fan_nomi
# fanlar=Fan("matematika","fizika","kimyo")
#print(fanlar.get_science_name())
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passpord, tyil):
        super().__init__(ism, familiya, passpord, tyil)
        self.fanlar=[]
#3 - Talaba klassiga fanga_yozil() degan yangi metod yozing. 
# Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va 
# talabaning fanlar ro'yxatiga qo'shib qo'ysin.
    def fanga_yozil(self,fan):
        """Fanlar ro'yhatiga Fan klassdagi fanlarni qo'shish"""
        if isinstance(fan,Fan):
            self.fanlar.append(fan.fan_nomi)
        return self.fanlar
    def get_fanlar(self):
        """Talaba o'qiyotgan fanlar ro'yhatini chiqarish"""
        return ", ".join(self.fanlar) if self.fanlar else "Talaba hali hech qanday fanga yozilmadi."
#4 - Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini 
# yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini 
# qaytarsin.
    def remove_fan(self,fan):
        """Ro'yhatdan fanni o'chirish"""
        if isinstance(fan, Fan) and fan.fan_nomi in self.fanlar:
            self.fanlar.remove(fan.fan_nomi)
            print(f"{fan.fan_nomi} fani o'chirildi.")
        else:
            print("Siz bu fanga yozilmagansiz")
fan1=Fan("matematika")
fan2=Fan("kimyo")
fan3=Fan("fizika")
talaba1=Talaba("Ali","Valiyev","AB6072391",1995)
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.remove_fan(fan3)
#print(f"{talaba1.ism} o'qiyotgan fanlar: {talaba1.get_fanlar()}")

#5 - Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring 
# (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
#6 - Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
#7 - Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, passpord, tyil,tajriba):
        super().__init__(ism, familiya, passpord, tyil)
        """Professor xususiyatlari"""
        self.tajriba=tajriba
    def get_info(self):
        """Professor ma'lumotlarini ko'rsatish"""
        return f"{self.ism} {self.familiya} {self.tyil} - yil. Tajriba: {self.tajriba}"
professor1=Professor("Alisher","Aliyev","Ab564728",1980,5)
#print(professor1.get_info())
#8 - Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun 
# Foydalanuvchi klassidan Admin klassini yarating. 
class Foydalanuvchi:
    """Foydalanuvchi klassi"""
    def __init__(self,username,lastname,email,phone_number):
        """Foydalanuvchi xususiyatlari"""
        self.username=username
        self.lastname=lastname
        self.email=email
        self.phone_number=phone_number
    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        info = f"Username: {self.username}\nLastname: {self.lastname}\nEmail: {self.email}\nPhone_number: {self.phone_number}"
        return info
foydalanuvchi1=Foydalanuvchi("Sabohat","Qayumova","saboxatqayumova7@gmail.com",+998777777777)
#print(foydalanuvchi1.get_info())
#9 - Admin klassiga foydalanuvchida yo'q yangi metodlar yozing,
# masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.
class Admin(Foydalanuvchi):
    """Admin classi"""
    def __init__(self, username, lastname, email, phone_number,login,password):
        """Admin xususiyatlari"""
        super().__init__(username, lastname, email, phone_number)
        self.login=login
        self.password=password
        self.block_users=[]
    def get_info(self):
        info = f"Username: {self.username}\nLastname: {self.lastname}\nEmail: {self.email}\nPhone_number: {self.phone_number}"
        info += f"\nLogin: {self.login}\nPassword: {self.password}"
        return info
    def ban_user(self,foydalanuvchi):
        """Foydalanuvchini bloklash"""
        if isinstance(foydalanuvchi,Foydalanuvchi):
            if foydalanuvchi not in self.block_users:
                self.block_users.append(foydalanuvchi)
                print(f"{foydalanuvchi.username} bloklandi.")
            else:
                print(f"{foydalanuvchi.username} allaqachon bloklangan")
    def unban_user(self,foydalanuvchi):
        """Foydalanuvchini blokdan chiqarish"""
        if foydalanuvchi in self.block_users:
            self.block_users.remove(foydalanuvchi)
            print(f"{foydalanuvchi.username} blokdan chiqarildi.")
        else:
            print(f"{foydalanuvchi.username} foydalanuvchi bloklanmagan")
    def get_blocked_users(self):
        """Bloklangan foydalanuvchilarni chiqarish"""
        return [user.username for user in self.block_users] if self.block_users else "Hozircha hech kim bloklanmagan"
admin2=Admin("Madina","Bobomurodova","madinagmail.com",+998943332211,"madina",9595)
admin1=Admin("Sabohat","Qayumova","saboxatqayumova7@gmail.com",+998777777777,"sabohat",1201)
admin2.ban_user(foydalanuvchi1)
print(admin2.get_blocked_users())
