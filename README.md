# Weight-Converter
A simple command-line weight converter that converts between kilograms and
pounds, with input validation so it won't crash on bad input.

**To run:** `python Weight_Converter.py`

## Features I built in
- Input validation using try/except so non-numeric input doesn't crash it
- while/break loops that re-ask until the input is valid
- Unit input (K/P) validated with if/else so anything other than K or P re-prompts
- Input normalized with .strip().upper() so " k " and "K" both work
- Verified conversion factor (2.20462) against known values for accuracy

## Notes
Was really happy how I was able to fit most of the code within lines 10 - 23.

This is the less formal and more of a "How it works" part section:
The way this weight converter works is by prompting the user to enter their weight
and it removes any spaces the user might've included. Before moving onto the part 
where it asks the user if their weight is in Kilograms or Pounds, it tries to convert 
the input to a number, and if that fails (like if they typed letters), it tells them 
the input is invalid and prompts them to try again. After receiving the correct 
input, the program then asks the user if their weight is in Kilograms or Pounds
by entering "K" or "P". It also removes any spaces while also making their input 
uppercase. If the user's weight is in Kilos, the program takes the weight/input
they entered earlier and multiplies it by 2.20462. The process is similar with pounds,
it just divides the weight instead of multiplying. If the user enters an invalid option,
"BANANA" for example, it prints an error message and prompts the user to try again.
If not, the program prints the converted weight. 


Built using Bro Code's weight converter code as an outline.

I used AI (Claude) as a tutor to help me understand concepts like
catch-vs-check (try/except vs. if/else) and DRY, and to point me toward
bugs by asking questions rather than handing me answers. But I wrote and
debugged the code myself. 

Today is July 10th, 2026. I plan on becoming a Software Developer or working
in Cybersecurity. — Derick S Martinez
