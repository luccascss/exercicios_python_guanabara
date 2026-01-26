# Como saber a data atual da máquina
from datetime import date
data = int(input('Digite 0 para saber a data atual da máquina: '))
data_atual = date.today()
print(data_atual) if data == 0 else print('Tente novamente digitando 0.')

