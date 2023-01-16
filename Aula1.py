# adiciona
def add(x, y):
  return x + y
# subtrai
def subtract(x, y):
  return x - y
# multiplica
def multiply(x, y):
  return x * y
# divide
def divide(x, y):
  return x / y

print("Select operation")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

choice = input("Esolha a opção: ")
if choice in ('1', '2', '3', '4'):
  while True:
  
    num1 = float(input("Escolha o primeiro número: "))
    num2 = float(input("Escolha o segundo número: "))

    if choice == '1':
      print(num1, " + ", num2, " = ", add(num1, num2))
    elif choice == '2':
      print(num1, " - ", num2, " = ", subtract(num1, num2))
    elif choice == '3':
      print(num1, " * ", num2, " = ",  multiply(num1, num2))
    elif choice == '4':
      print(num1, " / ", num2, " = ", divide(num1, num2))
    break
else:
    print("Escolha inexistente")