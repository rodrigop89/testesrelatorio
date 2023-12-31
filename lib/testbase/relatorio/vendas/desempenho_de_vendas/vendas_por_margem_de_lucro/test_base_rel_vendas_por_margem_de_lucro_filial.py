"""Teste base para o relatório vendas por margem de lucro sistema filial"""
# pylint: disable=C0301

from pytest import mark
from lib.dados.dados_sistema import LOJA
from lib.dados.lista_relatorios import COD_5
from lib.dados.sistema import (
    digitar_nome_relatorio,
    login_sistema,
)
from lib.dados.tempo import (
    TEMPO_ESPERA,
    TEMPO_IMPRESSAO,
)
from lib.formulario.generico.f_generico import (
    apertar_enter,
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_empresas,
    selecionar_periodo,
    selecionar_sintetico,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_margem_de_lucro.f_rel_vendas_por_margem_de_lucro import (
    selecionar_margem_especifica,
    selecionar_todas_margens_de_lucro,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_vendas_margem_lucro_filial
def test_rel_vendas_por_margem_lucro_todas_margens_de_lucro_analitico_filial():
    """Filtro todas as margens de lucro com impressão analitico"""
    login_sistema()
    digitar_nome_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_empresas(LOJA)
    selecionar_todas_margens_de_lucro()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_margem_lucro_filial
def test_rel_vendas_por_margem_lucro_todas_margens_de_lucro_sintetico_filial():
    """Filtro todas as margens de lucro com impressão sintético"""
    login_sistema()
    digitar_nome_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_empresas(LOJA)
    selecionar_todas_margens_de_lucro()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_margem_lucro_filial
def test_rel_vendas_por_margem_lucro_seleciona_margem_analitico_filial():
    """Filtro magrem de lucro específica com impressão analitico"""
    login_sistema()
    digitar_nome_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_empresas(LOJA)
    selecionar_margem_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_margem_lucro_filial
def test_rel_vendas_por_margem_lucro_seleciona_margem_sintetico_filial():
    """Filtro magrem de lucro específica com impressão sintético"""
    login_sistema()
    digitar_nome_relatorio(COD_5)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_empresas(LOJA)
    selecionar_margem_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
