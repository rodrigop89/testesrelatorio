"Formulario genérico"
# pylint: disable=E0401
import time

import pyautogui
from lib.dados.dados_sistema import CEST, NCM, PRODUTO
from lib.dados.data import MES_ANO, PERIODO_FINAL, PERIODO_INICIAL, periodo

from lib.dados.teclado import (
    A,
    ALT,
    C,
    CTRL,
    ENTER,
    F,
    F2,
    F4,
    H,
    L,
    M,
    N,
    O,
    P,
    S,
    SHIFT,
    D,
    E,
    G,
    I,
    R,
    SPACE,
    T,
    TAB,
    W,
)
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.python.python_doc import esperar_tempo


def selecionar_todas_empresas():
    "Atalho selecionar o filtro todas as empresas"
    pyautogui.hotkey(ALT, T)


def selecionar_empresas(texto):
    "Atalho selecionar o filtro de empresa"
    pyautogui.hotkey(ALT, E)
    pyautogui.press(F4)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(F2)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.typewrite(texto)
    pyautogui.press(ENTER)


def selecionar_analitico():
    "Emitir analitico e periodo cancelamento"
    pyautogui.hotkey(ALT, A)


def selecionar_sintetico():
    "Emitir analitico e periodo cancelamento"
    pyautogui.hotkey(ALT, S)


def selecionar_periodo():
    "Atalho selecionar o campo do período"
    pyautogui.hotkey(ALT, D)


def informar_periodo_apenas_mes_e_ano():
    "Digitar apenas o mes e ano"
    periodo(MES_ANO)


def informar_periodo():
    "Digitar o período no relatório"
    periodo(PERIODO_INICIAL)
    dar_tab()
    periodo(PERIODO_FINAL)


def dar_tab():
    "Dar tab nos campos"
    pyautogui.press(TAB)


def apertar_enter():
    "Apertar Enter nos campos"
    pyautogui.press(ENTER)


def confirmar_selecao():
    "Confirmar filtros selecionados"
    pyautogui.hotkey(ALT, C)


def imprimir_relatorio():
    "Imprimir o relatório"
    pyautogui.hotkey(ALT, I)
    esperar_tempo(TEMPO_IMPRESSAO)


def gerar_planilha():
    "Gerar planilha excel"
    pyautogui.hotkey(ALT, G)
    esperar_tempo(TEMPO_IMPRESSAO)


def fechar_abaimpressao():
    "Fechar aba de impressão no navegador"
    pyautogui.hotkey(CTRL, SHIFT, W)
    time.sleep(3)


def sair_relatorio():
    "Sair do relatório selecionado"
    pyautogui.hotkey(ALT, R)
    time.sleep(2)


def fechar_sistemarelatorio():
    "Fechar sistema de relatórios"
    pyautogui.hotkey(ALT, F4)
    pyautogui.press(ENTER)


def selecionar_produto_especifico():
    "Selecionar a opção para informar um produto especifico"
    esperar_tempo(TEMPO_ESPERA)
    # pyautogui.click(COORD_X, COORD_Y, clicks=2, interval=0.1)
    pyautogui.hotkey(ALT, D)
    pyautogui.hotkey(ALT, P)
    esperar_tempo(TEMPO_ESPERA)
    dar_tab()
    pyautogui.typewrite(PRODUTO)
    pyautogui.press(ENTER)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(ENTER)
    esperar_tempo(TEMPO_ESPERA)
    sair_relatorio()
    confirmar_selecao()


def selecionar_demais_filtros():
    "Selecionar demais filtros"
    pyautogui.hotkey(ALT, D)


def selecionar_fabricante():
    "Filtro por fabricante"
    pyautogui.hotkey(ALT, F)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_linha():
    "Filtro por linha"
    pyautogui.hotkey(ALT, H)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_secao():
    "Filtro por seção"
    pyautogui.hotkey(ALT, S)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_lista_sngpc():
    "Filtro por lista SNGPC"
    pyautogui.hotkey(ALT, L)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_principio_ativo():
    "Filtro por principio ativo"
    pyautogui.hotkey(ALT, A)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_categoria():
    "Filtro por categoria"
    pyautogui.hotkey(ALT, T)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_margem_lucro():
    "Filtro por margem de lucro"
    pyautogui.hotkey(ALT, M)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_grupo_produto():
    "Filtro por grupo de produtos"
    pyautogui.hotkey(ALT, G)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_grupo_comissao():
    "Filtro por grupo de comissão"
    pyautogui.hotkey(ALT, O)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_grupo_remarcacao():
    "Filtro por grupo de remarcação de preços"
    pyautogui.hotkey(ALT, R)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_grupo_icms():
    "Filtro por grupo de icms"
    pyautogui.hotkey(ALT, I)
    pyautogui.press(SPACE)
    pyautogui.press(ENTER)


def selecionar_codigo_ncm():
    "Filtro por código NCM"
    pyautogui.hotkey(ALT, N)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.write(NCM)


def selecionar_codigo_cest():
    "Filtro por código CEST"
    pyautogui.hotkey(ALT, E)
    esperar_tempo(TEMPO_ESPERA)
    pyautogui.typewrite(CEST)
