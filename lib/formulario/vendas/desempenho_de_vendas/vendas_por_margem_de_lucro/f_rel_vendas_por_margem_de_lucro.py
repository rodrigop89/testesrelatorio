"""Formulário Relatório Vendas por Margem de Lucro"""
# pylint: disable=E0401

import pyautogui

from lib.dados.teclado import ALT, M, O, SPACE
from lib.dados.tempo import TEMPO_ESPERA
from lib.python.python_doc import esperar_tempo


def selecionar_todas_margens_de_lucro():
    """Listar todas margens de lucro"""
    pyautogui.hotkey(ALT, O)


def selecionar_margem_especifica():
    """Selecionar somente uma margem especifica"""
    pyautogui.hotkey(ALT, M)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
