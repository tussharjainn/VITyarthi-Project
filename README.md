# Project Title:
Python Universal Unit Converter

# Overview of the Project:
A Python script that provides an interactive, command-line-based universal unit converter may be found in the project.py file. It enables users to convert numerical quantities between standard units in many measurement categories, including mass, temperature, and distance. The program employs a menu-driven interface to help the user choose a category and a particular conversion, and it uses factors or pre-defined conversion formulas (as lambda functions) to carry out computations.

# Features:
The converter is designed to manage many kinds of conversions: Non-linear Temperature Conversions: Celsius to Fahrenheit (C to F) and Fahrenheit to Celsius (F to C) Linear Distance Conversions: Miles to Kilometres (km to miles) Kilometres to miles (km to miles) Feet to Meters (m to feet) Feet to meters (feet to m) Linear mass conversions: kilogrammes to pounds (kg to lbs)Kilogrammes to pounds (lbs to kg)

# Steps to Install:
The supplied code should be saved in a file called project.py.

# Running the Project:
Launch the command prompt or terminal.
                     Go to the directory in which project.py was saved.
                     Use the Python interpreter to run the script.
                     The primary conversion category menu will appear when the application launches.

Instructions for Testing- 

1. Test Menu Navigation
                                               Main Menu:
                                                 To see if the appropriate category submenu (Temperature, Distance, Mass) loads, enter 1, 2, or 3.
                                                 To ensure that the application ends smoothly, enter 4 or exit.
                                                 1.Submenu:
                                                 Choose a unit conversion (e.g., 1 for km to miles) within any category (e.g., Distance).
                                                 To make sure it goes back to the category menu, enter the "Back to Main Menu" option (for example, 5 for Distance).


  2. Test Conversion Accuracy
                                               Conversion          Input Value          Expected Formula/Factor          Expected Result (approx.)
                                               C to F                  25                    (25*9/5) + 32                      77.00 F
                                               F to C                  68                     (68-32)*5/9                       20.00 C
                                               km to miles              5                      5*0.621371                      3.11 miles
                                               kg to lbs               15                      15*2.20462                      33.07 lbs


  3. Test Error Handling
                                               Invalid Menu Choice: Enter a string or a non-existent number at any menu.
                                               Anticipated: "Invalid input" should be the output. Return to the menu after seeing an error warning like "Please enter a valid number for the menu choice."
                                               Invalid Value Input: Enter a non-numerical string when asked for the value to be converted.
                                               Anticipated: "Invalid input" should be the output. "Please enter a valid numerical value," followed by another input prompt or a return to the menu loop..
