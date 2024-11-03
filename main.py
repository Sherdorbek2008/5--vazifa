while True:
    print("buyruq lar add qoshilish "
          " view file ni korish")
    comand = input('buyruqni kiriting:')
    while True:
        if comand=='add':
            name=input("ismingiz")
            if name.isalpha() and name.istitle():
                pass
            else:
                print('ism faqat harfdan iborat va birinchi harfi kata bolishi kerak')
                continue

            soname=input("familyangiz")
            if soname.isalpha()and soname.istitle() and soname.endswith('ov'):
                pass
            else:
                print('familya faqat harfdan iborat va birinchi harfi kata bolishi  va ov bilan yugashi kerak kerak')
                continue
            phone=input('telefon raqamingizni kiriting:')
            if phone.startswith("+998") and phone[1:12].isnumeric():
                pass
            else:
                print('telefon nomer faqat +998 dan boshlashi va + dan song hammasi raqam bolishi kerak')
                continue
            email=input('emailni kiriting:')
            if email.endswith('@gmail.com'):
                pass
            else:
                print('email faqat @gmail.com bilan tugating')
                continue
            address=input('manzilni kiriting')
            if address.isalnum():
                pass
            else:
                print('manzil faqat raqam va harf bolishi kerak')
            with open("users_info.txt",'a')as file:
                 file.write(f"ism{name},familya{soname},tel raqam{phone},email{email},address{address}")
            break
    if comand=='view':
        with open("users_info.txt", 'r', encoding="utf-8")as file:
          file.read()
        print(file.read())

    if comand=='stop':
        break



