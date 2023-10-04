#criar uma calculadora pra calcular o bmi de uma pessoa usando a formula
# bmi = peso(em kg) / altura^2(m^2)

bmi = 0

# obtendo a altura e o peso do usuário
height = float(input("Type your height in m:\n"))
weight = int(input("Type your weight in kg:\n"))

bmi = weight / height ** 2

# convertendo o bmi para int
bmi = int(bmi)

print("Your bim is " + str(bmi))
