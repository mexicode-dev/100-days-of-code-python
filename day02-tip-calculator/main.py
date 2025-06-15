# Tip Calculator - Day 2 Project

# Powitanie użytkownika
print("Welcome to the tip calculator!")

# Pobranie danych wejściowych
bill = float(input("What was the total bill? $"))  # Całkowity rachunek
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))  # Procent napiwku
people = int(input("How many people to split the bill? "))  # Liczba osób dzielących rachunek

# Obliczenie napiwku jako ułamek dziesiętny
tip_as_percent = tip / 100

# Obliczenie całkowitej kwoty napiwku
total_tip_amount = bill * tip_as_percent

# Całkowita kwota rachunku z napiwkiem
total_bill = bill + total_tip_amount

# Obliczenie kwoty przypadającej na jedną osobę
bill_per_person = total_bill / people

# Zaokrąglenie wyniku do dwóch miejsc po przecinku
final_amount = round(bill_per_person, 2)

# Wyświetlenie ostatecznego wyniku
print(f"Each person should pay: ${final_amount}")