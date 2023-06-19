# Вывод и ввод
import text
def prinytie_chisla():
    while True:
      print("=" * 110)
      print(text.menu_1)
      print("=" * 110)
      chislo = input(text.vvod_chisla)
      if chislo.isdigit() and 0 < int(chislo) < 3:
         return int(chislo)
      else:
         print("\n" + "=" * 110)
         print(text.chislo_false)
         print("=" * 110 + "\n")

def prinytie_chisla_vibor():
    while True:
      print("=" * 110)
      print(text.menu_2)
      print("=" * 110)
      chislo = input(text.vvod_boica)
      if chislo.isdigit() and 0 < int(chislo) < 3:
         return int(chislo)
      else:
         print("\n" + "=" * 110)
         print(text.chislo_false)
         print("=" * 110 + "\n")

def prinytie_chisla_fight_1():
    while True:
      print("=" * 110)
      print(text.menu_3)
      print("=" * 110)
      chislo = input(text.vvod_udar)
      if chislo.isdigit() and 0 < int(chislo) < 5:
         return int(chislo)
      else:
         print("\n" + "=" * 110)
         print(text.chislo_false)
         print("=" * 110 + "\n")

def prinytie_chisla_fight_2():
    while True:
      print("=" * 110)
      print(text.menu_4)
      print("=" * 110)
      chislo = input(text.vvod_udar)
      if chislo.isdigit() and 0 < int(chislo) < 5:
         return int(chislo)
      else:
         print("\n" + "=" * 110)
         print(text.chislo_false)
         print("=" * 110 + "\n")

def vihod():
   print("\n" + "=" * 110)
   print(text.vihod_menu)
   print("=" * 110 + "\n")

def sdatsy():
   print("\n" + "=" * 110)
   print(text.vihod_sdatsy)
   print("=" * 110 + "\n")

