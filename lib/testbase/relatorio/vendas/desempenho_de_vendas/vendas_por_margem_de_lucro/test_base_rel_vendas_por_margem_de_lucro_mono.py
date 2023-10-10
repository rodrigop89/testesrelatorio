"Teste base para o relatório vendas por margem de lucro sistema mono"
# pylint: disable=E0401
# pylint: disable=R0801
# pylint: disable=C0301

from pytest import mark
from lib.dados.lista_relatorios import COD_5
from lib.dados.sistema import digitar_codigo_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    apertar_enter,
    fechar_abaimpressao,
    fechar_sistemarelatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_periodo,
    selecionar_sintetico,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_margem_de_lucro.f_rel_vendas_por_margem_de_lucro import (
    selecionar_margem_especifica,
    selecionar_todas_margens_de_lucro,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_vendas_margem_lucro_mono
def test_base_vendas_por_margem_lucro_todas_margens_de_lucro_analitico_mono():
    "Filtro todas as margens de lucro com impressão analitico"
    login_sistema()
    digitar_codigo_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todas_margens_de_lucro()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()


@mark.emitir_rel_vendas_margem_lucro_mono
def test_base_vendas_por_margem_lucro_todas_margens_de_lucro_sintetico_mono():
    "Filtro todas as margens de lucro com impressão sintético"
    login_sistema()
    digitar_codigo_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todas_margens_de_lucro()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()


@mark.emitir_rel_vendas_margem_lucro_mono
def test_base_vendas_por_margem_lucro_seleciona_margem_analitico_mono():
    "Filtro magrem de lucro específica com impressão analitico"
    login_sistema()
    digitar_codigo_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_margem_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()


@mark.emitir_rel_vendas_margem_lucro_mono
def test_base_vendas_por_margem_lucro_seleciona_margem_sintetico_mono():
    "Filtro magrem de lucro específica com impressão sintético"
    login_sistema()
    digitar_codigo_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_margem_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
