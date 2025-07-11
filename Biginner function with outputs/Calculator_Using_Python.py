import Calculator_Art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division,
}
#print(operations["*"](2, 3))
def calculator():
  print(Calculator_Art.logo())
  should_accumulate = True
  num1 = float(input("What is the first number? \n"))
  while should_accumulate:

   for symbol in operations:
     print(symbol)
   operation_symbol = input("pick an operation:")

   num2 = float(input("What is the second number? \n"))
   answer = operations[operation_symbol](num1, num2)
   print(f"{num1} {operation_symbol} {num2} = {answer}")

   choice = input(f"Type 'Y' to calculation with {answer}, or type 'N' to start a new calculation: ").lower()

   if choice == 'Y':
     num1 = answer
   else:
       should_accumulate = False
       print("\n" * 20)
       calculator()


calculator()



