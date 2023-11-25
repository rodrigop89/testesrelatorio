"""Formulário relatório Vendas com Produtos Cancelados"""
# pylint: disable=E0401
import pyautogui

from lib.dados.teclado import ALT, O, V


def selecionar_periodo_devolucao():
    """Seleciona o período por devolução"""
    pyautogui.hotkey(ALT, O)


def selecionar_periodo_venda():
    """Seleciona o período por vendas"""
    pyautogui.hotkey(ALT, V)
