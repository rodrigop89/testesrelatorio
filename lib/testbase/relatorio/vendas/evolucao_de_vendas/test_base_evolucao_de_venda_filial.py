"""Teste base relatório evolução de vendas com sistema filial"""
# pylint: disable=E0401

from pytest import mark
from lib.dados.dados_sistema import LOJA
from lib.dados.sistema import (
    digitar_nome_relatorio,
    login_sistema,
)
from lib.dados.lista_relatorios import COD_1
from lib.dados.tempo import TEMPO_ESPERA
from lib.formulario.generico.f_generico import (
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo_apenas_mes_e_ano,
    sair_relatorio,
    selecionar_empresas,
    selecionar_periodo,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_evolucao_filial
def test_rel_evolucao_vendas_filial():
    """Teste sistema filial"""
    login_sistema()
    digitar_nome_relatorio(COD_1)
    selecionar_empresas(LOJA)
    selecionar_periodo()
    informar_periodo_apenas_mes_e_ano()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
