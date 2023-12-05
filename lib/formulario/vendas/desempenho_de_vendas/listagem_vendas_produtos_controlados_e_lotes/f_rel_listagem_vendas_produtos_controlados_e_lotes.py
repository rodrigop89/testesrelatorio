"""Formulário relatório listagem de vendas produtos controlados e lotes"""

import pyautogui

from lib.dados.teclado import (
    ALT,
    NUM_1,
    NUM_2,
    NUM_3,
    NUM_4,
    NUM_5,
    NUM_6,
    NUM_7,
    NUM_8,
    O,
    P,
    L,
    S,
)

# PRODUTO


def selecionar_todos_produtos():
    """Selecionar todos os produtos"""
    pyautogui.hotkey(ALT, O)


def selecionar_produto():
    """Selecionar somente um produto"""
    pyautogui.hotkey(ALT, P)


# LISTA SNGPC


def selecionar_todas_listas_sngpc():
    """Selecionar todas as Listas SNGPC"""
    pyautogui.hotkey(ALT, L)


def selecionar_lista_sngopc():
    """Selecionar lista sngpc"""
    pyautogui.hotkey(ALT, S)


# VENDAS COM LOTES


def selecionar_todas_vendas_lotes():
    """Selecionar todas as vendas com e sem lotes"""
    pyautogui.hotkey(ALT, NUM_1)


def selecionar_vendas_com_lotes():
    """Selecionar somente vendas com lotes"""
    pyautogui.hotkey(ALT, NUM_2)


def selecionar_vendas_sem_lotes():
    """Selecionar somente vendas sem lotes"""
    pyautogui.hotkey(ALT, NUM_3)


# VENDAS COM RECEITUÁRIO


def selecionar_todas_vendas_receituario():
    """Selecionar todas as vendas com e sem receituario"""
    pyautogui.hotkey(ALT, NUM_4)


def selecionar_vendas_com_receituario():
    """Selecionar somente vendas com receituario"""
    pyautogui.hotkey(ALT, NUM_5)


def selecionar_vendas_sem_receituario():
    """Selecionar somente vendas sem receituario"""
    pyautogui.hotkey(ALT, NUM_6)


# ORDENAÇÃO


def ordenar_por_data_da_venda():
    """Ordenação por data da venda"""
    pyautogui.hotkey(ALT, NUM_7)


def ordenar_por_produto():
    """Ordenação por produto(Descrição de Venda)"""
    pyautogui.hotkey(ALT, NUM_8)
