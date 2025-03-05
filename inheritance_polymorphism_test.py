#AMALYOT 
#Shaxs va Talaba klasslarini yaratgan edik. 
# Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi test dasturlar yozing.
# Ikki klass uchun yagona test yoza olasizmi? (isInstance() funksiyasini eslang)
import unittest
from inheritance_polymorphism import Shaxs,Talaba
class SHaxsTalabaTest(unittest.TestCase):
    """Shaxs va Talaba klassi uchun test"""
    def setUp(self):
        self.ism="sabohat"
        self.familiya="qayumova"
        self.passport="AB6480535"
        self.tyil=2001
        self.idraqam="FZ20011201"
        self.bosqich=1
        self.manzil="Qashqadaryo"
        self.talaba1=Talaba(self.ism,self.familiya,self.passport,self.tyil,self.idraqam,self.manzil)
        self.shaxs1=Shaxs(self.ism,self.familiya,self.passport,self.tyil)
    def test_create_shaxs(self):
        self.assertIsInstance(self.shaxs1, Shaxs)
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
    def test_create_talaba(self):
        self.assertIsInstance(self.talaba1, Talaba)
        self.assertIsInstance(self.talaba1, Shaxs)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.bosqich)
        self.assertIsNotNone(self.talaba1.manzil)
    def test_get_info(self):
        info="Sabohat Qayumova 1 bosqich. ID raqami FZ20011201"
        self.assertEqual(info,self.talaba1.get_info())
    def test_get_age(self):
        self.assertEqual(24,self.shaxs1.get_age(2025))
    def test_get_id(self):
        self.assertEqual(self.idraqam,self.talaba1.get_id())
    def test_get_bosqich(self):
        self.assertEqual(self.bosqich,self.talaba1.get_bosqich())

unittest.main()