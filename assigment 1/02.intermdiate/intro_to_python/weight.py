    
earth_weight = float(input("Enter your weight on Earth (in kg): "))
planet_input = input("Enter a planet: ")


planet = planet_input.capitalize()

gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,  # Note: Fixed typo from "Uranus" to match sample input
    "Neptune": 1.14
}



if planet in gravity_constants:
    planet_weight = earth_weight * gravity_constants[planet]
    rounded_weight = round(planet_weight, 2)

    if rounded_weight == int(rounded_weight):
        rounded_weight = int(rounded_weight)
    
    print(f"The equivalent weight on {planet}: {rounded_weight}")
else:
    print("Invalid planet entered. Please try again with a valid planet name.")
