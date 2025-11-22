def convert_unit():
    """Main function to run the comprehensive unit converter."""
    
    
    conversions = {
        'temperature': {
            'C_to_F': lambda c: (c * 9/5) + 32,
            'F_to_C': lambda f: (f - 32) * 5/9,
        },
        'distance': {
            'km_to_miles': 0.621371,
            'miles_to_km': 1 / 0.621371,
            'm_to_feet': 3.28084,
            'feet_to_m': 1 / 3.28084,
        },
        'mass': {
            'kg_to_lbs': 2.20462,
            'lbs_to_kg': 1 / 2.20462,
        }
    }

    print(" Python Universal Unit Converter ")
    
    while True:
        print("\n--- Available Conversion Types ---")
        categories = list(conversions.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category.capitalize()}")
        print(f"{len(categories) + 1}. Exit")
        print("---------------------------------")

        try:
            category_choice = input("Enter your choice (number) or 'Exit': ")
            
            if category_choice.lower() == 'exit' or category_choice == str(len(categories) + 1):
                print("Exiting converter. Goodbye!")
                break
            
            category_index = int(category_choice) - 1
            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                unit_options = conversions[selected_category]
                
                print(f"\n--- {selected_category.capitalize()} Conversions ---")

                unit_names = list(unit_options.keys())
                for i, unit_name in enumerate(unit_names, 1):
                    display_name = unit_name.replace('_', ' ').title()
                    print(f"{i}. {display_name}")
                print(f"{len(unit_names) + 1}. Back to Main Menu")
                print("---------------------------------")

                unit_choice = input("Enter your unit choice (number): ")
                
                if unit_choice == str(len(unit_names) + 1):
                    continue 

                unit_index = int(unit_choice) - 1
                if 0 <= unit_index < len(unit_names):
                    selected_unit_key = unit_names[unit_index]
                    
                    try:
                        value = float(input(f"Enter the value to convert: "))
                        conversion_rule = unit_options[selected_unit_key]
                        
                        result = 0
                        if callable(conversion_rule):
                            result = conversion_rule(value)
                            from_unit = selected_unit_key.split('_')[0].upper()
                            to_unit = selected_unit_key.split('_')[2].upper()
                            print(f"\n Result: {value}{from_unit} is equal to {result:.2f}{to_unit}")
                        else:
                            result = value * conversion_rule
                            from_unit = selected_unit_key.split('_')[0].upper()
                            to_unit = selected_unit_key.split('_')[2].upper()
                            print(f"\n Result: {value} {from_unit} is equal to {result:.2f} {to_unit}")

                    except ValueError:
                        print(" Invalid input. Please enter a valid numerical value.")
                    except IndexError:
                        print(" Error parsing unit key.")
                        
                else:
                    print(" Invalid unit choice. Please try again.")
            else:
                print(" Invalid category choice. Please try again.")

        except ValueError:
            print(" Invalid input. Please enter a valid number for the menu choice.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_unit()