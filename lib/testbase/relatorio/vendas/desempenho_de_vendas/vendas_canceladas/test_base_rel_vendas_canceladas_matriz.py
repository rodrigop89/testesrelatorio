"""Teste base relatório vendas cancaladas com sistema matriz"""

from pytest import mark
from lib.dados.sistema import (
    digitar_nome_relatorio,
    login_sistema,
)
from lib.dados.lista_relatorios import COD_8
from lib.formulario.generico.f_generico import (
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_analitico,
    selecionar_sintetico,
    selecionar_todas_empresas,
    selecionar_periodo,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_canceladas.f_rel_vendas_canceladas import (
    selecionar_cancelamento,
    selecionar_venda,
)


@mark.emitir_rel_vendas_canceladas_matriz
def test_rel_vendas_canceladas_analitico_cancelamento_matriz():
    """Filtro analitico por periodo de cancelamento"""
    login_sistema()
    digitar_nome_relatorio(COD_8)
    selecionar_todas_empresas()
    selecionar_analitico()
    selecionar_cancelamento()
    selecionar_periodo()
    informar_periodo()
    imprimir_relatorio()
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_canceladas_matriz
def test_rel_vendas_canceladas_analitico_vendas_matriz():
    """Filtro analitico por periodo de vendas"""
    login_sistema()
    digitar_nome_relatorio(COD_8)
    selecionar_todas_empresas()
    selecionar_analitico()
    selecionar_venda()
    selecionar_periodo()
    informar_periodo()
    imprimir_relatorio()
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_canceladas_matriz
def test_rel_vendas_canceladas_sintetico_cancelamento_matriz():
    """Filtro sintetico por periodo de cancelamento"""
    login_sistema()
    digitar_nome_relatorio(COD_8)
    selecionar_todas_empresas()
    selecionar_sintetico()
    selecionar_cancelamento()
    selecionar_periodo()
    informar_periodo()
    imprimir_relatorio()
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()


@mark.emitir_rel_vendas_canceladas_matriz
def test_rel_vendas_canceladas_sintetico_venda_matriz():
    """Filtro sintetico por periodo de vendas"""
    login_sistema()
    digitar_nome_relatorio(COD_8)
    selecionar_todas_empresas()
    selecionar_sintetico()
    selecionar_venda()
    selecionar_periodo()
    informar_periodo()
    imprimir_relatorio()
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
