# def calculator():
#     while True:
#         try:
#             num1 = float(input("Enter the first number (or 'q' to quit): "))
#             num2 = float(input("Enter the second number: "))
#         except ValueError:
#             print("Invalid input. Please enter numbers only.")
#             continue

#         operation = input("Enter operation (+, -, *, /, %, //, ** or 'q' to quit): ")

#         if operation == 'q':
#             print("Calculator exited.")
#             break
#         elif operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 print("Error: Division by zero.")
#                 continue
#         elif operation == '%':
#             result = num1 % num2
#         elif operation == '//':
#             if num2 != 0:
#                 result = num1 // num2
#             else:
#                 print("Error: Division by zero.")
#                 continue
#         elif operation == '**':
#             result = num1 ** num2
#         else:
#             print("Invalid operation.")
#             continue

#         print("Result:", result)

# # Run the calculator
# calculator()
# for i in range(10):
#     print("Iteration:", i)


# fruits = ["apple", "banana", "mango", "orange", "guava", "peach", "apricot", "plum", "pear", "pomegranate", "grapes", "watermelon", "melon", "cherry", "date", "fig", "kiwi", "lemon", "lime", "lychee", "papaya", "persimmon", "pineapple", "strawberry", "tangerine", "custard apple", "jamun", "loquat", "mulberry", "peach", "phalsa", "sapodilla", "sweet lime", "wood apple", "blackberry", "coconut", "dragonfruit", "grapefruit", "jackfruit", "muskmelon", "olive", "passion fruit", "quince", "raspberry", "soursop", "tamarind", "ugli fruit", "white mulberry", "zucchini flower", "karonda"]
# for fruit in fruits:
#     print("fruits names :  "+fruit)



# # Multiplication table
# for outer in range(1, 10): # outer loop
#     print(f"Multiplication table for {outer}:")
#     for inner in range(1, 11): # nested inner loop
#         print(f"{outer} * {inner} = {outer * inner}")
#     print()  # Add a blank line after each row


# for i in range(5000, -1, -1):
#     print(i)

for i in [1, 2, 4, 5]:
   if i == 3:
       break
   else:
         print("only executed when no item is equal to 3")

furniture:list = ['table', 'chair', 'rack', 'shelf']
print(len(furniture))