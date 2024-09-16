# Parte 1: Variáveis, constantes e complexidade de código
"""
Constante = "Váriaveis" que não mudam, geralmente são escritas em maiusculo
Muitas condições são ruim trazem complexidade.
"""
velocidade_carro = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar_!
LOCAL_1 = 100 #local onde o radar_! está
RADAR_RANGE = 1 #a distância onde o radar chega

range_radar_menos = LOCAL_1 - RADAR_RANGE
range_radar_mais = LOCAL_1 + RADAR_RANGE
passou_no_radar_1 = local_carro >= range_radar_menos and local_carro <= range_radar_mais

if passou_no_radar_1:
    if velocidade_carro > RADAR_1:
        print("O carro passou da velocidade do radar e foi mutado.")
    else:
        print('O carro não passou a velocidade do radar.')
