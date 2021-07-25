segundos_totais = input("Por favor, entre com o número de segundos que deseja converter: ")
num_total = int(segundos_totais)

dias = num_total // 86400
segundos_dif = num_total % 86400
horas = segundos_dif // 3600
segundos_rest = segundos_dif % 3600
minutos = segundos_rest // 60
segundos = segundos_rest % 60

print(dias, "dias,", horas, "horas,", minutos,"minutos e", segundos, "segundos.")
