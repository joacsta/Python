QTD_COMB = 12


tempo_gasto = input()
vel_media = input()

tempo_gasto = int(tempo_gasto)
vel_media = float(vel_media)

calc = (vel_media/QTD_COMB) * tempo_gasto 
calc = float(calc)

print('%.3f' % calc)


