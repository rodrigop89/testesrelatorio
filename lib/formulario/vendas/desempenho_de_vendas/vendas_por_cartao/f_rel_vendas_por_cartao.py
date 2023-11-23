"Formulário Relatório Vendas por Cartão"
import pyautogui

from lib.dados.teclado import (
    ALT,
    C,
    ENTER,
    O,
    SPACE,
)
from lib.dados.tempo import TEMPO_ESPERA
from lib.python.python_doc import esperar_tempo


def selecionar_todos_cartoes():
    "Filtro todos os cartões"
    pyautogui.hotkey(ALT, O)


def selecionar_cartao():
    "Filtro cartão específico"
    pyautogui.hotkey(ALT, C)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)
