import requests
from time import sleep

preco_paozinho = 0.80
preco_broa = 2.50

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

dolar = any

try:
    dolar = requests.get(url).json()
    valorDolar = round(float(dolar['USDBRL']['bid']),2)

except requests.exceptions.RequestException as error:
    print(error)



paozinho_vendidos = int(input('Informe quantos pães foram vendidos hoje: \n'))
broas_vendidas = int(input('Informe quantas broas foram vendidas hoje: \n'))

ganho_paozinho = preco_paozinho * paozinho_vendidos
ganho_broa = preco_broa * broas_vendidas
ganho_total = ganho_paozinho + ganho_broa


print(f'Uau! Hoje você teve um ganho de R${ganho_total}')
sleep(0.4)
print('='*53)
sleep(0.4)
print('Agora vamos ver quanto foi o custo de sua fabricação')

custo_fabricacao = ganho_total * 0.43

print(f'Seu custo de fabricação foi de R${custo_fabricacao:.2f} \n')
sleep(0.3)
print('Certo! Agora vamos pegar isso tudo e ver o quanto vamos por na poupança e o quanto vamos converter para a nossa viagem anual!')
print('='*125)
sleep(0.3)

restante = ganho_total - custo_fabricacao  

print(f'Ok! Nos sobraram R${restante:.2f}, agora vamos repartir para a viagem anual e para a nossa poupança \n')
sleep(0.3)
valor = restante*0.15 
conversaoDolar = valor/valorDolar

print(f'Legal, você depositou R${valor:.2f} na sua poupança e converteu R${valor:.2f} em USD{conversaoDolar:.2f}')
print('='*125)
