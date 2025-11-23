Problem Statement- The project fills the demand for a flexible and interactive tool that makes it simple for users to convert numerical data between widely used units of measurement in several categories (such as temperature, mass, and distance). Implementing a reliable, menu-driven command-line interface that accurately applies different conversion formulas and factors based on user selections is the challenge.

Scope of the Project- Supported Conversion Types: comprises mass, distance, and temperature at the moment.
                       Specific Conversions:
                                         Temperature: Celsius to Fahrenheit (C_to_F) and Fahrenheit to Celsius (F_to_C).
                                         Distance: Kilometers to Miles (km_to_miles), Miles to Kilometers (miles_to_km), Meters to Feet (m_to_feet), and Feet to Meters (feet_to_m).
                                         Mass: Kilograms to Pounds (kg_to_lbs) and Pounds to Kilograms (lbs_to_kg).
                                         User Interface: Numerical input for conversion values is accepted by a sequence of tiered menus for category and unit selection.
                                        Error Handling: Simple error handling for non-numerical value inputs and faulty menu selections.

Target Users- Students: Students enrolled in scientific, math, or engineering programs who must quickly convert units for assignments or projects.
             Professionals who frequently need to convert measurements in their work include engineers and technicians.
             Developers and Novice Programmers: Those who use the code as a straightforward, useful example to learn Python functions, dictionaries, loops, and fundamental user input processing.
             General Users: Anyone in need of a quick and easy-to-use solution for routine unit conversion chores.

High-Level Features- Categorized Conversions: Sorts conversions into discrete categories such as Mass, Temperature, and Distance.
                     Interactive Menu System: Users can choose a category from a looping main menu, then choose the particular conversion pair from a subsequent menu.
                     Dynamic Conversion Logic: To effectively handle various mathematical rules, it uses a dictionary structure to store both lambda functions (for temperature) and direct conversion factors (for distance/mass).
                     Input Validation: Encourages the user to submit a proper number by catching ValueError exceptions for both menu option and the value to be converted.
                     Result Formatting: Rounds the conversion result to two decimal places (.2f) for a clear, legible output that includes both the original and final units.
