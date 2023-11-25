"""Teste base para o relatório custo médio de vendas sistema filial 
com filtros todos os produtos e produto especifico"""
# pylint: disable=C0301

from pytest import mark
from lib.dados.dados_sistema import LOJA
from lib.dados.lista_relatorios import COD_4
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
    selecionar_empresas,
    selecionar_periodo,
    selecionar_produto_especifico,
)
from lib.formulario.vendas.desempenho_de_vendas.custo_medio_de_vendas.f_rel_custo_media_de_vendas import (
    selecionar_custo_medio_baseado_nas_compras,
    selecionar_filtro_especifico,
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo,
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo,
    selecionar_preco_bruto_ultima_compra,
    selecionar_preco_custo,
    selecionar_preco_custo_medio,
    selecionar_preco_fabrica,
    selecionar_preco_liquido_ultima_compra,
    selecionar_todos_produtos,
)
from lib.python.python_doc import esperar_tempo


# FILTRO TODOS OS PRODUTOS


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_incluir_produtos_sem_compras_preco_custo_medio_filial():
    """Filtro todos os produtos por preço de custo médio"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_custo_medio()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_incluir_produtos_sem_compras_preco_fabrica_filial():
    """Filtro todos os produtos por preço de fábrica"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_fabrica()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_incluir_produtos_sem_compras_preco_custo_filial():
    """Filtro todos os produtos por preço de custo"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_custo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_incluir_produtos_sem_compras_preco_bruto_compra_filial():
    """Filtro todos os produtos por preço bruto da ultima compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_bruto_ultima_compra()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_incluir_produtos_sem_compras_preco_liquido_compra_filial():
    """Filtro todos os produtos por preço liquido da ultima compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_preco_liquido_ultima_compra()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_todos_produtos
def test_rel_custo_medio_todos_produtos_nao_incluir_produtos_sem_compras_filial():
    """Filtro todos os produtos sem incluir produtos sem compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_todos_produtos()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


## FILTRO SOMENTE UM PRODUTO ESPECIFICO ##


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_incluir_produtos_sem_compras_preco_custo_medio_filial():
    """Filtro produto especifico , incluir produtos sem compras e preço de custo médio"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_custo_medio()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_incluir_produtos_sem_compras_preco_fabrica_filial():
    """Filtro produto especifico , incluir produtos sem compras e preço de fabrica"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_fabrica()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_incluir_produtos_sem_compras_preco_custo_filial():
    """Filtro produto especifico , incluir produtos sem compras e preço de custo"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_custo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_incluir_produtos_sem_compras_preco_bruto_filial():
    """Filtro produto especifico , incluir produtos sem compras e preço bruto da ultima compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_bruto_ultima_compra()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_incluir_produtos_sem_compras_preco_liq_compra_filial():
    """Filtro produto especifico , incluir produtos sem compras e preço liquido da ultima compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_preco_liquido_ultima_compra()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_produto_especifico
def test_rel_custo_medio_produto_especifico_nao_incluir_produtos_sem_compras_filial():
    """Filtro produto especifico não incluir produtos sem compra"""
    login_sistema()
    digitar_nome_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_produto_especifico()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_aba_impressao()
    sair_relatorio()
    fechar_sistema_relatorio()
    esperar_tempo(TEMPO_ESPERA)
