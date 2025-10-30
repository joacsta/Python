from datetime import datetime

data_atual = datetime.now()

dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year
dia = f'{dia_atual}/{mes_atual}/{ano_atual}'

horas_atual = data_atual.hour
minutos_atual = data_atual.minute
horario = f'{horas_atual}:{minutos_atual}'

def datetime_atual():
    print(f'{horario} | {dia}')

datetime_atual()