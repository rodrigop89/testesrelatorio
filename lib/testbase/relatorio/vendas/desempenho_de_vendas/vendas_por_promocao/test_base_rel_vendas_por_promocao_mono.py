"Teste base para o relatório vendas por promoção sistema mono"
# pylint: disable=E0401
# pylint: disable=R0801
# pylint: disable=C0301


from pytest import mark
from lib.dados.sistema import digitar_nome_relatorio, login_sistema
from lib.dados.lista_relatorios import COD_3
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    apertar_enter,
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_periodo,
    selecionar_sintetico,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_por_promocao.f_rel_vendas_por_promocao import (
    desmarcar_vendas_sem_promocao,
    listar_promocao_especifica,
    listar_todas_promocoes,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_todas_promocoes_analitico_incluir_vendas_mono():
    "Filtro todas promoções, analitico e incluindo vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_todas_promocoes()
    selecionar_analitico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_todas_promocoes_analitico_sem_incluir_vendas_mono():
    "Filtro todas promoções, analitico e retirando vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_todas_promocoes()
    selecionar_analitico()
    desmarcar_vendas_sem_promocao()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_seleciona_promocao_analitico_incluir_vendas_mono():
    "Filtro com uma promoção especifica, analitico e incluindo vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_promocao_especifica()
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


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_seleciona_promocao_analitico_sem_incluir_vendas_mono():
    "Filtro com uma promoção especifica, analitico e retirando vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_promocao_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_analitico()
    desmarcar_vendas_sem_promocao()
    esperar_tempo(TEMPO_ESPERA)
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_todas_promocoes_sintetico_incluir_vendas_mono():
    "Filtro todas promoções, sintetico e incluindo vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_todas_promocoes()
    selecionar_sintetico()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_todas_promocoes_sintetico_sem_incluir_vendas_mono():
    "Filtro todas promoções, sintético e retirando vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_todas_promocoes()
    selecionar_sintetico()
    desmarcar_vendas_sem_promocao()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_seleciona_promocao_sintetico_incluir_vendas_mono():
    "Filtro com uma promoção especifica, sintetico e incluindo vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_promocao_especifica()
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


@mark.emitir_rel_vendas_promocao_mono
def test_rel_vendas_por_promocao_seleciona_promocao_sintetico_sem_incluir_vendas_mono():
    "Filtro com uma promoção especifica, sintetico e retirando vendas sem promoção"
    login_sistema()
    digitar_nome_relatorio(COD_3)
    esperar_tempo(TEMPO_ESPERA)
    listar_promocao_especifica()
    esperar_tempo(TEMPO_ESPERA)
    apertar_enter()
    selecionar_sintetico()
    desmarcar_vendas_sem_promocao()
    esperar_tempo(TEMPO_ESPERA)
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
