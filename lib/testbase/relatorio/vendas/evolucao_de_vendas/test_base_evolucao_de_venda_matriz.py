"Teste base relatório evolução de vendas com sistema matriz"
# pylint: disable=E0401


from pytest import mark
from lib.dados.sistema import digitar_codigo_relatorio, login_sistema
from lib.dados.lista_relatorios import COD_1
from lib.dados.tempo import TEMPO_ESPERA
from lib.formulario.generico.f_generico import (
    fechar_abaimpressao,
    fechar_sistemarelatorio,
    imprimir_relatorio,
    informar_periodo_apenas_mes_e_ano,
    sair_relatorio,
    selecionar_periodo,
    selecionar_todas_empresas,
)
from lib.python.python_doc import esperar_tempo


@mark.emitir_rel_evolucao_matriz
def test_relatorio_evolucao_vendas_matriz():
    "Teste sistema matriz"
    login_sistema()
    digitar_codigo_relatorio(COD_1)
    selecionar_todas_empresas()
    selecionar_periodo()
    informar_periodo_apenas_mes_e_ano()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
