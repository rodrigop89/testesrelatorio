"""Formulario Relatório Cancelamento de Vendas"""
# pylint: disable=E0401
import pyautogui

from lib.dados.teclado import ALT, C, V


# def selecionar_analitico():
#     """Emitir analitico e periodo cancelamento"""
#     pyautogui.hotkey(ALT, A)


# def selecionar_sintetico():
#     """Emitir analitico e periodo cancelamento"""
#     pyautogui.hotkey(ALT, S)


def selecionar_cancelamento():
    """Emitir analitico e periodo vendas"""
    pyautogui.hotkey(ALT, C)


def selecionar_venda():
    """Emitir sintetico e periodo cancelamento"""
    pyautogui.hotkey(ALT, V)
