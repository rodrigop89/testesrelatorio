"""Teste base relatório listagem de vendas produtos controlados
e lotes sistema mono"""

from pytest import mark
from lib.dados.lista_relatorios import COD_10
from lib.dados.sistema import digitar_nome_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_periodo,
)
from lib.formulario.vendas.desempenho_de_vendas.listagem_vendas_produtos_controlados_e_lotes.f_rel_listagem_vendas_produtos_controlados_e_lotes import (
    ordenar_por_data_da_venda,
    ordenar_por_produto,
    selecionar_todas_listas_sngpc,
    selecionar_todas_vendas_lotes,
    selecionar_todas_vendas_receituario,
    selecionar_todos_produtos,
    selecionar_vendas_com_lotes,
    selecionar_vendas_com_receituario,
    selecionar_vendas_sem_receituario,
)
from lib.python.python_doc import esperar_tempo


# Filtro todos os produtos, todas listas sngpc e ordenado por data da venda
@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_data_mono():
    """Filtro todos produtos, todas vendas com e sem lotes, todas vendas com e sem receituario"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_todas_vendas_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_com_receituario_data_mono():
    """Filtro todos produtos, todas vendas com e sem lotes e vendas com receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_vendas_com_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_sem_receituario_data_mono():
    """Filtro todos produtos, todas vendas com e sem lotes e vendas sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_vendas_sem_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


# Filtro todos os produtos, todas listas sngpc e ordenado por produto(descrição de venda)
@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_produto_mono():
    """Filtro todos produtos, todas vendas com e sem lotes, todas vendas com e sem receituario"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_todas_vendas_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_com_receituario_produto_mono():
    """Filtro todos produtos, todas vendas com e sem lotes e vendas com receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_vendas_com_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_todas_vendas_sem_receituario_produto_mono():
    """Filtro todos produtos, todas vendas com e sem lotes e vendas sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_todas_vendas_lotes()
    selecionar_vendas_sem_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


# Filtro todos os produtos, todas listas sngpc, somente vendas com lotes
# e ordenado por data da venda
@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_data_mono():
    """Filtro todos os produtos, somente vendas com lote, com e sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_todas_vendas_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_receituario_data_mono():
    """Filtro todos os produtos, somente vendas com lote e com receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_vendas_com_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_sem_receituario_data_mono():
    """Filtro todos os produtos, somente vendas com lote e sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_vendas_sem_receituario()
    ordenar_por_data_da_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


# Filtro todos os produtos, todas listas sngpc, somente vendas com lotes
# e ordenado por produto
@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_produto_mono():
    """Filtro todos os produtos, somente vendas com lote, com e sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_todas_vendas_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_receituario_produto_mono():
    """Filtro todos os produtos, somente vendas com lote e com receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_vendas_com_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_listagem_produtos_controlados_e_lotes_mono
def test_rel_list_prod_controlados_lotes_todos_prod_vendas_com_lote_sem_receituario_produto_mono():
    """Filtro todos os produtos, somente vendas com lote e sem receituário"""
    login_sistema()
    digitar_nome_relatorio(COD_10)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_todas_listas_sngpc()
    selecionar_vendas_com_lotes()
    selecionar_vendas_sem_receituario()
    ordenar_por_produto()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)
