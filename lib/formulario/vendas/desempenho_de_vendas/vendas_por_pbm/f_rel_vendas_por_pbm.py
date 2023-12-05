"""Formulario Relatório Vendas por PBM"""
# pylint: disable=E0401

import pyautogui


from lib.dados.teclado import (
    ALT,
    ENTER,
    ESC,
    F2,
    O,
    P,
    SPACE,
    TAB,
)
from lib.dados.tempo import TEMPO_ESPERA
from lib.python.pyautogui_doc import (
    informar_descricao,
)

from lib.python.python_doc import esperar_tempo


def seleciona_todos_pbms():
    """Selecionar todos PBMS"""
    pyautogui.hotkey(ALT, O)


def seleciona_opcao_apresentar_informaceos_adicionais():
    """Seleciona a opção de apresentar
    informações adicionais da venda"""
    pyautogui.press(TAB)
    pyautogui.press(SPACE)


def seleciona_pbm_especifico():
    """Selecionar PBM específico"""
    pyautogui.hotkey(ALT, P)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


# OUTRA FORMA DE FILTRAR O PBM, SELECIONANDO POR DESCRIÇÃO


def seleciona_pbm(texto):
    """Selecionar PBM por descrição"""
    pyautogui.hotkey(ALT, P)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(F2)
    # pyautogui.typewrite(texto)
    informar_descricao(texto)
    pyautogui.press(ESC)
    pyautogui.press(SPACE)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(ENTER)
