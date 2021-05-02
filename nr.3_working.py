licznik = input('input a number: ')
mianownik = input('input a second number: ')
licznik_int = int(licznik)
mianownik_int = int(mianownik)

if mianownik_int == 0:
    print('dzielenie przez zero')
else:
    result = licznik_int/mianownik_int
    print(f"""wynik to: {result} """)
