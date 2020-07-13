sal_mes = float(input("Informe o salário recebido: "))
dias_mes = float(input("Dias trabalhos no mês: "))
horas_dia = float(input("Horas trabalhadas por dia: "))
vHora = sal_mes/dias_mes/horas_dia
print("O valor da hora trabalhada é de %.2f" %vHora)