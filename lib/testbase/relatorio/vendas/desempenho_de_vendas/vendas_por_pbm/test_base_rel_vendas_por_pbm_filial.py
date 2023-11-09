"Teste base para o relatório Vendas por PBM utilizando sistema mono"

from pytest import mark
from lib.dados.dados_sistema import FARMACIA_POPULAR, LOJA
from lib.dados.lista_relatorios import COD_6
from lib.dados.sistema import digitar_codigo_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    fechar_abaimpressao,
    fechar_sistemarelatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_empresas,
    selecionar_periodo,
    selecionar_sintetico,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_pbm.f_rel_vendas_por_pbm import (
    seleciona_opcao_apresentar_informaceos_adicionais,
    seleciona_pbm,
    seleciona_todos_pbms,
)
from lib.python.python_doc import esperar_tempo


# FILTRO TODOS OS PBMs


@mark.emitir_rel_vendas_por_pbm_todos_filial
def test_rel_vendas_por_pbm_todos_pbms_analitico_mono():
    "Filtro todos PBMs de forma analitica"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_todos_mono
def test_rel_vendas_por_pbm_todos_pbms_analitico_apresenta_informacoes_adicionais_mono():
    "Filtro todos PBMs de forma analitica com informações adicionais da venda"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_analitico()
    seleciona_opcao_apresentar_informaceos_adicionais()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_todos_mono
def test_rel_vendas_por_pbm_todos_pbms_sintetico_mono():
    "Filtro todos PBMs de forma sintética"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO PBM ESPECIFICO


@mark.emitir_rel_vendas_por_pbm_especifico_mono
def test_rel_vendas_por_pbm_especifico_analitico_mono():
    "Filtro PBM específico de forma analitica"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_especifico_mono
def test_rel_vendas_por_pbm_especifico_analitico_apresenta_informacoes_adicionais_mono():
    "Filtro PBM específico de forma analitica com informacoes adicionais"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_analitico()
    seleciona_opcao_apresentar_informaceos_adicionais()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_especifico_mono
def test_rel_vendas_por_pbm_especifico_sintetico_mono():
    "Filtro PBM específico de forma sintético"
    login_sistema()
    digitar_codigo_relatorio(COD_6)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)
