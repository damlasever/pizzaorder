#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from datetime import datetime


# In[2]:


with open("Menu.txt", "w") as file:
    file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")


# In[3]:


class Pizza:
    def __init__(self):
        self.description = "Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0

class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza (domates sosu,mozarella)"
    
    def get_cost(self):
        return 20.0

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza (domates sosu, mozarella, fesleğen)"
    
    def get_cost(self):
        return 22.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza (domates sosu, mozarella, sucuk, yeşil biber, domates, soğan)"
    
    def get_cost(self):
        return 25.0

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza (mozarella)"
    
    def get_cost(self):
        return 18.0


# In[4]:


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
    
    def get_cost(self):
        return self.component.get_cost() + 2.0

class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantarlar"
    
    def get_cost(self):
        return self.component.get_cost() + 3.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
    
    def get_cost(self):
        return self.component.get_cost() + 4.0

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
    
    def get_cost(self):
        return self.component.get_cost() + 5.0

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
    
    def get_cost(self):
        return self.component.get_cost() + 1.5

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
    
    def get_cost(self):
        return self.component.get_cost() + 2.5


# In[5]:



def main():
    # Menüyü yazdır
    with open('Menu.txt') as f:
        print(f.read())

    # Pizza seçimi
    while True:
        pizza_choice = input("Lütfen bir pizza tabanı seçin (1-4): ")
        if pizza_choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

    pizza = None
    if pizza_choice == "1":
        pizza = KlasikPizza()
    elif pizza_choice == "2":
        pizza = MargaritaPizza()
    elif pizza_choice == "3":
        pizza = TurkPizza()
    elif pizza_choice == "4":
        pizza = SadePizza()

    # Sos seçimi
    while True:
        print("\nLütfen bir sos seçin:")
        print("11: Zeytin")
        print("12: Mantarlar")
        print("13: Keçi Peyniri")
        print("14: Et")
        print("15: Soğan")
        print("16: Mısır")
        sos_choice = input("Sos seçimi (11-16): ")
        if sos_choice in ["11", "12", "13", "14", "15", "16"]:
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

    sos = None
    if sos_choice == "11":
        sos = Zeytin(pizza)
    elif sos_choice == "12":
        sos = Mantarlar(pizza)
    elif sos_choice == "13":
        sos = KeciPeyniri(pizza)
    elif sos_choice == "14":
        sos = Et(pizza)
    elif sos_choice == "15":
        sos = Sogan(pizza)
    elif sos_choice == "16":
        sos = Misir(pizza)

    print("\nSeçtiğiniz pizza: ", sos.get_description())
    print("Toplam fiyat: ", sos.get_cost())

    # Kullanıcı bilgileri
    name = input("\nAdınız: ")
    tc = input("TC Kimlik Numaranız: ")
    credit_card_number = input("Kredi Kartı Numaranız: ")
    credit_card_cvv = input("Kredi Kartı CVV: ")

    # Sipariş kaydetme
    with open('Orders_Database.csv', mode='a') as csv_file:
        fieldnames = ['Kullanıcı Adı', 'TC Kimlik Numarası', 'Kredi Kartı Numarası', 'Sipariş Açıklaması', 'Sipariş Zamanı', 'Kredi Kartı Şifresi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({
            'Kullanıcı Adı': name,
            'TC Kimlik Numarası': tc,
            'Kredi Kartı Numarası': credit_card_number,
            'Sipariş Açıklaması': sos.get_description(),
            'Sipariş Zamanı': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'Kredi Kartı Şifresi': credit_card_cvv
        })

        print("\nSiparişiniz başarıyla kaydedildi.")


# In[ ]:

main()

