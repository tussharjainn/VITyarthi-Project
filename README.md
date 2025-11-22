Project Title- Python Universal Unit Converter

Overview of the Project- The project.py file contains a Python script that implements an interactive, command-line-based universal unit converter. It allows users to convert numerical values between common units across different measurement categories such as Temperature, Distance, and Mass. The application uses a menu-driven interface to guide the user through selecting a category and a specific conversion, and it performs calculations using pre-defined conversion formulas (as lambda functions) or factors.

Features- The converter is structured to handle various types of conversions:Temperature Conversions (Non-Linear):Celsius to Fahrenheit (C to F) Fahrenheit to Celsius (F to C) Distance Conversions (Linear):Kilometers to Miles (km to miles) Miles to Kilometers (miles to km) Meters to Feet (m to feet) Feet to Meters (feet to m) Mass Conversions (Linear):Kilograms to Pounds (kg to lbs)Pounds to Kilograms (lbs to kg)

Steps to Install- Save the provided code content into a file named project.py.

Running the Project- Open your terminal or command prompt.
                     Navigate to the directory where you saved project.py.
                     Execute the script using the Python interpreter
                     The application will start, displaying the main conversion category menu.

Instructions for Testing- 1. Test Menu Navigation
                                               Main Menu:
                                                 Enter 1, 2, or 3 to check if the correct category submenu (Temperature, Distance, Mass) loads.
                                                 Enter 4 or exit to confirm the program terminates gracefully.
                                                
.                                               Submenu:
                                                  Within any category (e.g., Distance), select a unit conversion (e.g., 1 for Km To Miles).
                                                  Enter the "Back to Main Menu" choice (e.g., 5 for Distance) to ensure it returns to the category menu.
                        
.                          2. Test Conversion Accuracy
                                               Conversion          Input Value          Expected Formula/Factor          Expected Result (approx.)
                                               C to F                  25                    (25*9/5) + 32                      77.00 F
                                               F to C                  68                     (68-32)*5/9                       20.00 C
                                               km to miles              5                      5*0.621371                      3.11 miles
                                               kg to lbs               15                      15*2.20462                      33.07 lbs
                        
 .                         3. Test Error Handling
                                               Invalid Menu Choice: At any menu, enter a non-existent number or a string
                                               Expected: It should output "Invalid input. Please enter a valid number for the menu choice." or a similar error
                                                         message, and return to the menu.
                                               Invalid Value Input: When prompted to enter the value to convert, enter a non-numerical string
                                               Expected: It should output " Invalid input. Please enter a valid numerical value." and prompt for input again or 
                                               return to the menu loop.
