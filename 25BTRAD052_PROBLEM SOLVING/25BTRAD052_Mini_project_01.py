print("UNIT CONVERTER")
print("1. Kilometres to Metres")
print("2. Metres to Centimetres")
print("3. Kilograms to Grams")
print("4. Litres to Millilitres")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    result = value * 1000
    print(value, "kilometres =", result, "metres")

elif choice == 2:
    result = value * 100
    print(value, "metres =", result, "centimetres")

elif choice == 3:
    result = value * 1000
    print(value, "kilograms =", result, "grams")

elif choice == 4:
    result = value * 1000
    print(value, "litres =", result, "millilitres")

else:
    print("Invalid choice")