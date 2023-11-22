"""Funções com python"""
# pylint: disable=E0401
import time
from datetime import datetime

from lib.dados.teclado import NUM_1, NUM_7


def esperar_tempo(texto):
    """tempo de espera"""
    time.sleep(texto)


def obter_mes_atual():
    """Função obter mes e ano"""
    data_atual = datetime.now()
    mes = str(data_atual.month).zfill(2)
    ano = str(data_atual.year)
    data_formatada = mes + ano
    return data_formatada


def obter_periodo_inicial():
    """periodo inicial"""
    data_atual = datetime.now()
    dia = str(NUM_1).zfill(2)
    mes = str(NUM_1).zfill(2)
    ano = str(data_atual.year)
    periodo_inicial = dia + mes + ano
    return periodo_inicial


def obter_periodo_final():
    """periodo inicial"""
    data_atual = datetime.now()
    dia = str(NUM_7).zfill(2)
    mes = str(NUM_1).zfill(2)
    ano = str(data_atual.year)
    periodo_final = dia + mes + ano
    return periodo_final
