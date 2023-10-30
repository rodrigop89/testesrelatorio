"""Funções para iniciar o sistema de relatório """
# pylint: disable=E0401
import pyautogui

from lib.dados.janela import LOGIN
from lib.dados.dados_sistema import RELATORIO, SENHA
from lib.dados.teclado import ALT, ENTER, S, WIN, R
from lib.dados.tempo import TEMPO_ESPERA
from lib.python.pyautogui_doc import returntowindow
from lib.python.python_doc import esperar_tempo


def inicializar_sistema():
    """Inicia"""
    pyautogui.hotkey(WIN, R)
    pyautogui.typewrite(RELATORIO)
    pyautogui.press(ENTER)
    esperar_tempo(TEMPO_ESPERA)


def login_sistema():
    "Login"
    # for numero in range(5):
    # numero = 0
    inicializar_sistema()
    returntowindow(LOGIN)
    pyautogui.typewrite(SENHA)
    pyautogui.press(ENTER)
    esperar_tempo(TEMPO_ESPERA)


def digitar_codigo_relatorio(texto):
    """Função para obter o código do relatório"""
    pyautogui.hotkey(ALT, S)
    pyautogui.typewrite(texto)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(ENTER)
