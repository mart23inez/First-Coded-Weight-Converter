# Second project being a weight converter.
while True:
    weight_input = input("Enter your weight: ").strip()
    try:
        weight = float(weight_input)
        break
    except ValueError:
        print(f"Error: '{weight_input}' is not a valid number!")

while True:
    unit_input = input(f"Kilograms or Pounds?: (K or P): ").strip().upper()
    if unit_input == "K":
        weight = weight * 2.20462
        unit = "Lbs."
        break
    elif unit_input == "P":
        weight = weight / 2.20462
        unit = "Kgs."
        break
    else:
        print(f"Error: '{unit_input}' is not a valid unit!")

print(f"Your new weight is {round(weight, 1)} {unit}")

# This project only took me 2 - 3 hours to complete. I used the body of BroCode's weight converter
# code as outline to make my own. Pretty much the same thing I did with the calculator project, but 
# with my own improvements.
# Improvements over the original:
# - Input validation on both numbers using try/except (ValueError), so
#   non-numeric input (e.g. "banana") no longer crashes the program.
# - Unit input (K/P) validated with if/else in a while loop, re-asking
#   until valid — no crash, just re-prompts on bad input.
# - Input normalized with .strip().upper() so " k " and "K" both work.
# - Verified conversion factor (2.20462) against known values for accuracy.
