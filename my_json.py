import json
x=10
x_jon=json.dumps(x)
#print(x_jon)

y=5.5
y_json=json.dumps(y)

m=True
m_json=json.dumps(m)

sonlar=(12,45,23,67)
sonlar_json=json.dumps(sonlar)
sonlar2=json.loads(sonlar_json)

bemor ={
        "ismi":"Sabohat Qayumova",
        "yosh":24,
        "oila":True,
        "farzandlar":('Azizbek',"E'zoza"),
        "allergiya":None,
        "dorilar":[
            {"nomi":"Analgin","miqdori":0.5},
            {"nomi":"Panodol","miqdori":1.3}
            ]
        }
bemor_json=json.dumps(bemor,indent=4)
# print(bemor_json)
#JSONni faylga saqlash
with open('data/bemor.json','w') as f:
    json.dump(bemor,f)

filename="data/bemor.json"
with open(filename) as f:
    bemor=json.load(f)
# print(type(bemor))
# print(bemor.keys())
# print(bemor["dorilar"][0])
# print(bemor)

#AMALYOT
#1 - Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json=json.dumps(data)
print(data_json)
#2 -  Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring:
#  talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
talaba={"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba_json=json.dumps(talaba)
talaba2=json.loads(talaba_json)
print(f"{talaba2["ism"]} {talaba["familiya"]}") 
#3 - Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang
with open("data/data.json",'w') as file:
    json.dump(data,file)
with open("data/talaba.json",'w') as f:
    json.dump(talaba,f)
#4 - Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. 
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida 
# konsolga chiqaring.
filename="data/students.json"
with open(filename) as file:
    student=json.load(file)
print(student.keys())
print(f"{student["student"][0]["name"]} {student["student"][0]["lastname"]} {student["student"][0]["year"]} - kurs, {student["student"][0]["faculty"]} fakultet talabasi.")
print(f"{student["student"][1]["name"]} {student["student"][1]["lastname"]} {student["student"][1]["year"]} - kurs, {student["student"][1]["faculty"]} fakultet talabasi.")
print(f"{student["student"][2]["name"]} {student["student"][2]["lastname"]} {student["student"][2]["year"]} - kurs, {student["student"][2]["faculty"]} fakultet talabasi.")

#5 - Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani 
# JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang 
# (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi
#  (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python
import requests
urls="https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python"
responce=requests.get(urls)
#print(json.dumps(responce.json(), indent=4))
text={
    "batchcomplete": "",
    "query": {
        "pages": {
            "13801": {
                "pageid": 13801,
                "ns": 0,
                "title": "Python",
                "extract": "Python ([\u02c8p\u028c\u026a\u03b8 (\u0259)n] \u2014 payton, piton) \u2014 turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning o\u02bbqilishiga urg\u02bbu beradi. Uning til konstruksiyalari va obyektga yo\u02bbnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sun\u02bciy intellekt hamda ma\u02bclumotlar muhandisiligi sohalarining tili hisoblanadi.\nPython deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud bo\u02bblib, uning nomi \u2014 IronPython dasturlash muhitidir.\nGuido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga e\u02bclon qildi.\nPython dasturlash tiliga bo\u02bblgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga ko\u02bbra, 2020\u20142021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng ko\u02bbp talab bo\u02bblgan."
            }
        }
    }
}


with open('data/python.json','w') as f:
    json.dump(text,f)
with open("data/python.json") as f:
    text2=json.load(f)

print(text2["query"]["pages"]["13801"]["title"])
print(text2["query"]["pages"]["13801"]["extract"])
