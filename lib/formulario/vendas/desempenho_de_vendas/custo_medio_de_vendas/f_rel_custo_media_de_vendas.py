"Formulário relatório custo médio de vendas"
import pyautogui


from lib.dados.teclado import (
    ALT,
    C,
    F,
    M,
    N,
    NUM_1,
    NUM_2,
    NUM_3,
    NUM_4,
    NUM_5,
    O,
)


def selecionar_todos_produtos():
    "Filtro todos os produtos"
    pyautogui.hotkey(ALT, O)


def selecionar_filtro_especifico():
    "Selecionar algum filtro especifico"
    pyautogui.hotkey(ALT, F)


def selecionar_custo_medio_baseado_nas_compras():
    "Custo medio baseado nas compras no periodo informado"
    pyautogui.hotkey(ALT, C)


def selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo():
    "Não inclui produtos que não possuem compras no período"
    pyautogui.hotkey(ALT, N)


def selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo():
    "Inclui produtos que não possuem compras no período"
    pyautogui.hotkey(ALT, M)


def selecionar_preco_custo_medio():
    "Filtro preço de custo médio"
    pyautogui.hotkey(ALT, NUM_1)


def selecionar_preco_fabrica():
    "Filtro preço de fabrica / compra referencial"
    pyautogui.hotkey(ALT, NUM_2)


def selecionar_preco_custo():
    "Filtro preço de custo"
    pyautogui.hotkey(ALT, NUM_3)


def selecionar_preco_bruto_ultima_compra():
    "Filtro preço bruto da ultima compra"
    pyautogui.hotkey(ALT, NUM_4)


def selecionar_preco_liquido_ultima_compra():
    "Filtro preço bruto da ultima compra"
    pyautogui.hotkey(ALT, NUM_5)
