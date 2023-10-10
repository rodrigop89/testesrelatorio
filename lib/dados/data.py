"""Datas e períodos"""
# pylint: disable=E0401
import pyautogui
from lib.python.python_doc import (
    obter_mes_atual,
    obter_periodo_final,
    obter_periodo_inicial,
)

MES_ANO = obter_mes_atual()

PERIODO_INICIAL = obter_periodo_inicial()
PERIODO_FINAL = obter_periodo_final()


def periodo(texto):
    "Função para passar as datas do período"
    pyautogui.typewrite(texto)
