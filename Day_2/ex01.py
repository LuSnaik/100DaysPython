# escreve um programa que pega um número de dois dígitos
# e faz a soma dos dois dígitos que o constituem

# receber os números e manter eles como uma string
two_dig = input("Insert a two digits number\n")

# usando o index notation pra obter os dois digitos e também os converter pra integer
dig_one = int(two_dig[0])
dig_two = int(two_dig[1])

# fazendo a soma
total = dig_one + dig_two

print(str(dig_one) + " + " + str(dig_two) + " = " + str(total))
