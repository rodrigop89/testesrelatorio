""""Teste base para o relatório Vendas Por Cartão sistema Mono"""

from pytest import mark
from lib.dados.lista_relatorios import COD_7
from lib.dados.sistema import digitar_codigo_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    fechar_abaimpressao,
    fechar_sistemarelatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_linha_alternativo,
    selecionar_opcao_vendas,
    selecionar_periodo,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_cartao.f_rel_vendas_por_cartao import (
    selecionar_cartao,
    selecionar_todos_cartoes,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_vendas_por_cartao_mono_filtro_todos_cartoes
def test_rel_vendas_por_cartao_todos_cartoes_ordenar_por_venda_mono():
    "Filtro todos cartões e ordando por vendas"
    login_sistema()
    digitar_codigo_relatorio(COD_7)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_cartoes()
    selecionar_opcao_vendas()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_cartao_mono_filtro_todos_cartoes
def test_rel_vendas_por_cartao_todos_cartoes_ordenar_por_linha_mono():
    "Filtro todos cartões e ordenado por linha"
    login_sistema()
    digitar_codigo_relatorio(COD_7)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_cartoes()
    selecionar_linha_alternativo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_cartao_mono_filtro_cartao_especifico
def test_rel_vendas_por_cartao_especifico_ordenar_por_venda_mono():
    "Filtro cartão específico e ordenado por vendas"
    login_sistema()
    digitar_codigo_relatorio(COD_7)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_cartao()
    selecionar_opcao_vendas()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_cartao_mono_filtro_cartao_especifico
def test_rel_vendas_por_carta_especifico_ordernar_por_linha_mono():
    "Filtro cartão específico  ordenado por linha"
    login_sistema()
    digitar_codigo_relatorio(COD_7)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_cartao()
    selecionar_linha_alternativo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)
