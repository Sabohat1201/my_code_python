# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 
# Obyekt haqida ma'lumot (__rerp__)
# Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odmalar_soni=0
    def __init__(self,ism,familiya):
        """Shaxsning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        Shaxs.__odmalar_soni+=1
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odmalar_soni

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni=0
    def __init__(self, ism, familiya,bosqich,id):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya)
        self.bosqich=bosqich
        self.id=id
        Talaba.__talabalar_soni+=1
    def __repr__(self):
        return super().__repr__()
    def __lt__(self,talaba):
        return self.bosqich<talaba.bosqich
    def __eq__(self, talaba):
        return self.bosqich==talaba.bosqich
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
   
talaba1=Talaba("Sabohat","Qayumova",2,1)
talaba2=Talaba("Madina","Bobomurodova",3,2)
print(talaba1)
print(talaba1<talaba2)
print(talaba1==talaba2)
#2 - Fan degan yangi klass yarating. 
#Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. 
# Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi 
# metodlarni qo'shing.
class Fan:
    """Fan klassi"""
    def __init__(self,name):
        """Fan xususiyatlari"""
        self.name=name
        self.students=[]
    def add_students(self,*talabalar):
        for talaba in talabalar:
            if isinstance(talaba,Talaba):
                self.students.append(talaba)
            else:
                print("Talabalar kiriting.")
    def __getitem__(self,index):
        return self.students[index]
    def __setitem__(self,index,values):
        if isinstance(values,Talaba):
            self.students[index]=values
    def __len__(self):
        return len(self.students)
#3 - Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
    def __add__(self,fan):
        if isinstance(fan,Fan):
            fanlar=Fan(f"{self.name} and {fan.name}")
            fanlar.students=self.students+fan.students
            return fanlar
        elif isinstance(fan,Talaba):
            self.add_avto(fan)
        else:
            print(f"AvtoSalon ga {type(fan)} ni qo'shib bo'lmaydi.")
#4 - Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing
#(bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
    def __sub__(self, student_id):
        """Talabani ID bo'yicha o'chirish"""
        self.students = [student for student in self.students if student.id != student_id]
#5 - Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). 
# Bu metodlarni o'zingiz istagandek talqin qiling.
    def __call__(self, *qiymat):
        if qiymat:
            for talaba in qiymat:
                self.add_students(talaba)
        else:
            return [talaba for talaba in self.students]
matem=Fan("Oliy matematika")
fizika=Fan("Fizika")
talaba3=Talaba("Murod","Qayumov",2,3)
talaba4=Talaba("Nilufar","Xayitova",4,4)
matem.add_students(talaba1,talaba2)
fizika.add_students(talaba3,talaba4)
talaba5=Talaba("Olim","Eshqobilov",3,5)
matem.students[0]=talaba5
fanlar=matem+fizika
print(fanlar.name)
print(fanlar.students)
fanlar-5
#print(fanlar.students)
talaba6=Talaba("Guli","Eshqobilova",3,6)
matem(talaba6)
print(matem())
print(fizika())
# print(matem.students)
# print(matem.students[0])
# print(len(matem))