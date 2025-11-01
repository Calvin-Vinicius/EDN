"""Desenvolva um programa que calcula o consumo médio de combustível de uma veículo. Use os seguintes dados:
Distãncia percorrida 300km
Combustivel gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondando para duas casas decimais."""


distancia = 300.0
combustivel_gasto = 25.0

def _consumo_medio(distancia_km, combustivel_litros):
    consumo_por_litro = distancia/combustivel_litros
    print(f"A distância percorrida foi {distancia_km} km , combustivel gasto {combustivel_litros} litros O consumo médio (km/l) é : {consumo_por_litro:.2f} km/l")


_consumo_medio(distancia , combustivel_gasto)