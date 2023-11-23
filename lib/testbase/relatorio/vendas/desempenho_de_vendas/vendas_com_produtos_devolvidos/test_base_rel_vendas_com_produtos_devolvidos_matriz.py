"Teste base para o relatório Vendas com Produtos Devolvidos sistema matriz"
from pytest import mark
from lib.dados.lista_relatorios import COD_9

from lib.dados.sistema import digitar_nome_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_periodo,
    selecionar_todas_empresas,
)
from lib.formulario.vendas.desempenho_de_vendas.vendas_com_produtos_devolvidos.f_rel_vendas_com_produtos_devolvidos import (
    selecionar_periodo_devolucao,
    selecionar_periodo_venda,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_vendas_com_produtos_devolvidos_matriz
def test_rel_vendas_com_produtos_devolvidos_periodo_devolucao_matriz():
    "Filtro por período devolução"
    login_sistema()
    digitar_nome_relatorio(COD_9)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    selecionar_periodo_devolucao()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_vendas_com_produtos_devolvidos_matriz
def test_rel_vendas_com_produtos_devolvidos_periodo_vendas_matriz():
    "Filtro por vendas"
    login_sistema()
    digitar_nome_relatorio(COD_9)
    selecionar_todas_empresas()
    esperar_tempo(TEMPO_ESPERA)
    selecionar_periodo_venda()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)
