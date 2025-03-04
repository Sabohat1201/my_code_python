def tubSonmi(n):
    if n==2 or n==3: 
        return True
    if n%2==0 or n<2: 
        return False
    for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
        if n%i==0:
            return False   
    return True

#AMALYOT
#1 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
def numbers_compare(x,y,z):
    return max(x,y,z)
print(numbers_compare(4,12,8))

#2 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi
#  harfini katta harfga o'zgatiruvchi funksiya
def text_list(*names):
    matn=[]
    for name in names:
        matn.append(name.capitalize())
    return matn
    
print(text_list('salom dunyo','o\'tgan kunlar','mehrobdan chayon'))

#3 - Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
def juft_sonlar(*son):
    sonlar=[]
    for n in son:
        if n%2==0:
            sonlar.append(n)
    return sonlar
print(juft_sonlar(3,5,6,8,12,13,15))

#4 - Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) 
# qaytaruvchi funksiya yozing.
def is_fibonacci(n):
    if n < 0:
        return False  # Manfiy sonlar Fibonacci ketma-ketligida bo‘lmaydi
    
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True  # Son Fibonacci ketma-ketligida bor
        a, b = b, a + b  # Yangi Fibonacci sonini hisoblash
    return False  # Son Fibonacci ketma-ketligida yo‘q

# Test
print(is_fibonacci(8))   # True (8 Fibonacci ketma-ketligida bor)
print(is_fibonacci(10))  # False (10 yo‘q)
print(is_fibonacci(13))