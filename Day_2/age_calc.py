# Criar uma calculadora, que recebe a idade do usuário e calcula
# quantos dias, semanas, meses e anos restam até ele ter 90 anos
# 1 ano tem 365 dias, 52 semanas e 12 meses

# declarar variaveis dias, meses e semanas
days_a_year = 365
weeks_a_year = 52
months_a_year = 12

# calcular dias, semanas e meses passados em 90 anos
days_in_90_years = days_a_year * 90
weeks_in_90_years = weeks_a_year * 90
months_in_90_years = months_a_year * 90

# obter dados do user
user_age = int(input("Type your age\n"))

# calculares os dias, semanas e meses vividos pelo
# usuário
days_a_year *= user_age
weeks_a_year *= user_age
months_a_year *= user_age

# calcular os dias, semanas e meses que faltam pra o usuario ter 90 anos
days_left_to_90 = days_in_90_years - days_a_year
weeks_left_to_90 = weeks_in_90_years - weeks_a_year
months_left_to_90 = months_in_90_years - months_a_year

# fazer o print da mensagem
message = f"You have {days_left_to_90} days, {weeks_left_to_90} weeks, {months_left_to_90} months left to 90"
print(message)

