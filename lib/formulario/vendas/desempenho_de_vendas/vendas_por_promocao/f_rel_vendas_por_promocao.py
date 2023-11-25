"""Formulario Relatório Vendas por Promoção"""
# pylint: disable=E0401

import pyautogui

from lib.dados.teclado import (
    ALT,
    O,
    P,
    SPACE,
    V,
)
from lib.dados.tempo import TEMPO_ESPERA
from lib.python.python_doc import esperar_tempo


def listar_todas_promocoes():
    """Listar todas promoções"""
    pyautogui.hotkey(ALT, O)


def listar_promocao_especifica():
    """Listar uma promoção especifica"""
    pyautogui.hotkey(ALT, P)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)


def desmarcar_vendas_sem_promocao():
    """Incluir vendas sem promoção nos filtros"""
    pyautogui.hotkey(ALT, V)
