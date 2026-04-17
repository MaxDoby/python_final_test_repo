# EX 1  Scrieți un program Python care să afișeze rezultatele următoarelor operații:
# # -6 + 8 * 6
# # (44 + 8) % 5
# # 19 + -3 * 2 / 8
# # 5 + 20 / 3 * 2 - 8 % 4
#
# print(-6+8*6)
# print((-44+8)%5)
# print(19+-3*2/8)
# print(5+20/3*2-8%4)
#
#  # Ex2 Program Python care ia două numere de la tastatură
#  si afișează rezultatul înmulțirii lor. (input())
#
# num1 = float(input("Primul numar: "))
# num2 = float(input("Al doilea numar: "))
# print("Rezultatul inmultirii:", num1 * num2)
#
# # Ex3 Program Python care afișează: adunarea, scăderea, înmulțirea,
# împărțirea și restul împărțirii pentru două numere. (input())
#
# num1 = float(input("Primul numar: "))
# num2 = float(input("Al doilea numar: "))
# print("Rezultatul adunarii:", num1 + num2)
# print("Rezultatul scaderii:", num1 - num2)
# print("Rezultatul inmultirii:", num1 * num2)
# print("Rezultatul impartirii:", num1 / num2)
# print("Rezultatul restul impartirii:", num1 % num2)

# Ex 4 Program Python care compară 2 numere și spune care e mai mic și care e mai mare. (if/else)

# num1 = int(input("Primul numar: "))
# num2 = int(input("Al doilea numar: "))
# if (num1 > num2):
#     print(f'Numarul {num1} este mai mare ca {num2}')
# else:
#     print(f'Numarul {num2} este mai mare ca {num1}')

# Ex 5 Program Python în care utilizatorul scrie o parolă, iar programul o afișează la output.
#
# Exemplu:
## Input password:
## Password was: qwerty123123 (nu complicați)

# password = input('Introduceti parola: ')
# print(f'Parola introdusa este: {password}')

# Ex 6 Afișați toate numerele pare de la 1 la 100.

# for i in range(1, 100):
#     if i % 2 == 0:
#         print(i)

# ex 7 Program Python: utilizatorul introduce un număr, programul spune dacă e par sau impar.

# numarIntrodus = int(input('Introduceti un numar: '))
# if numarIntrodus % 2 == 0:
#     print(f'Numarul {numarIntrodus} este un numar par.')
# if numarIntrodus % 2 != 0:
#     print(f'Numarul {numarIntrodus} este un numar impar.')

# Ex 8 Program Python care primește o oră (0–23) și spune ce parte a zilei
# este (împărțiți 24h în minimum 4 părți).

# oraIntrodusa = int(input('Introduceti (in format 0-24h) ora zilei: '))
# if 5 <= oraIntrodusa < 12:
#     print('Este dimineata')
# elif 12 <= oraIntrodusa < 17:
#     print('Este amiaza')
# elif 17 <= oraIntrodusa < 21:
#     print('Este seara')
# elif (21 <= oraIntrodusa <= 24) or (0 <= oraIntrodusa < 5):
#     print('Este noapte')

# Ex 9 Program Python care primește numărul lunii (1–12) și
# afișează anotimpul: iarna / primăvara / vara / toamna.

# luna = int(input("Introduceti numarul lunii (1-12): "))
# if luna in [12, 1, 2]:
#     print("Iarna")
# elif 3 <= luna <= 5:
#     print("Primavara")
# elif 6 <= luna <= 8:
#     print("Vara")
# elif 9 <= luna <= 11:
#     print("Toamna")

# Ex 10 Program Python care transformă toate literele în majuscule pentru textul: "eu astazi scriu examen".

# text_pentru_modificare = 'eu astazi scriu examen'
# print(text_pentru_modificare.upper())

# Ex 11 Program Python care primește un string și afișează:
## indexul maxim (adică ultimul index)
## cantitatea de caractere (lungimea)

# un_string = ("That course was a wonderful experience")
# indexul_maxim = un_string[-1]
# print(indexul_maxim)
# cantitatea_caracterelor = len(un_string)
# print(cantitatea_caracterelor)

# EX 12 Clasificare vârstă:
# # până la 12: copil
# # 12–18: adolescent
# # peste 18: adult
# Atenție: valori ca 0 sau >135 nu se acceptă. (input() + if/elif/else)

# varsta = int(input('Introduceti varsta: '))
# if varsta <= 0 or varsta > 135:
#     print('Varsta incorecta.')
# elif varsta < 12 and varsta != 0:
#     print('Sunteti copil')
# elif 12 <= varsta <= 18:
#     print('Sunteti adolescent')
# else:
#     print('Sunteti adult')


# Ex 13 „Eu sunt un program. Număr până la 20, dar când ajung la 14 mă opresc.” (folosiți break)
# for i in range(20):
#     print(f'Eu sunt un program si numar pina la 20. Acum este {i}')
#     if i == 14:
#         print(f'Am ajuns la {i} si eu am obosit. PA-PA')
#         break

# Ex 14 „Eu sunt un program. Număr până la 20. Când ajung la 14 mă opresc,
# iau o gustare și continui drumul.” (folosiți continue ca să sari peste 14, dar să continui până la 20)

# for i in range(21):
#     if i == 14:
#         print(f'Am ajuns la {i} si fac o pauza, nu te superi? De fapt nu conteaza, continuam.')
#         continue
#     print(f'Eu sunt un program si numar pina la 20. Acum este {i}')


# Ex 15 Creați o listă) de numere întregi care să ocupe cel mai mic spațiu (după tip).
# # afișați lista
# # schimbați valoarea elementului de pe poziția 4 (după index)
# # afișați din nou lista

