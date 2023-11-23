"Teste base para o relatório Vendas por PBM utilizando sistema matriz"

from pytest import mark
from lib.dados.dados_sistema import (
    FARMACIA_POPULAR,
)
from lib.dados.lista_relatorios import COD_6
from lib.dados.sistema import (
    digitar_nome_relatorio,
    login_sistema,
)
from lib.dados.tempo import (
    TEMPO_ESPERA,
    TEMPO_IMPRESSAO,
)
from lib.formulario.generico.f_generico import (
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_periodo,
    selecionar_sintetico,
    selecionar_todas_empresas,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_pbm.f_rel_vendas_por_pbm import (
    seleciona_opcao_apresentar_informaceos_adicionais,
    seleciona_pbm,
    seleciona_todos_pbms,
)
from lib.python.python_doc import esperar_tempo


# FILTRO TODOS OS PBMs


@mark.emitir_rel_vendas_por_pbm_todos_matriz
def test_rel_vendas_por_pbm_todos_pbms_analitico_matriz():
    "Filtro todos PBMs de forma analitica"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_todos_matriz
def test_rel_vendas_por_pbm_todos_pbms_analitico_apresenta_informacoes_adicionais_matriz():
    "Filtro todos PBMs de forma analitica com informações adicionais da venda"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_analitico()
    seleciona_opcao_apresentar_informaceos_adicionais()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_todos_matriz
def test_rel_vendas_por_pbm_todos_pbms_sintetico_matriz():
    "Filtro todos PBMs de forma sintética"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_todos_pbms()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO PBM ESPECIFICO


@mark.emitir_rel_vendas_por_pbm_especifico_matriz
def test_rel_vendas_por_pbm_especifico_analitico_matriz():
    "Filtro PBM específico de forma analitica"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_especifico_matriz
def test_rel_vendas_por_pbm_especifico_analitico_apresenta_informacoes_adicionais_matriz():
    "Filtro PBM específico de forma analitica com informacoes adicionais"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_analitico()
    seleciona_opcao_apresentar_informaceos_adicionais()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_por_pbm_especifico_matriz
def test_rel_vendas_por_pbm_especifico_sintetico_matriz():
    "Filtro PBM específico de forma sintético"
    login_sistema()
    digitar_nome_relatorio(COD_6)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    seleciona_pbm(FARMACIA_POPULAR)
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)
