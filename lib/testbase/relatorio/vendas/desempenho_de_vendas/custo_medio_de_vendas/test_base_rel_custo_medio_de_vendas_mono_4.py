"""Teste base para o relatório custo médio de vendas sistema mono 
com os filtros NCM e Código CEST"""
# pylint: disable=C0301

from pytest import mark
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
    confirmar_selecao,
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_codigo_cest,
    selecionar_codigo_ncm,
    selecionar_demais_filtros,
    selecionar_periodo,
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
)
from lib.python.python_doc import esperar_tempo

## FILTRO NCM ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_preco_custo_medio_mono():
    "Filtro NCM e preço custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_preco_fabrica_mono():
    "Filtro NCM e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_preco_custo_mono():
    "Filtro NCM e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_preco_bruto_compra_mono():
    "Filtro NCM e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_preco_liquido_mono():
    "Filtro NCM e preço liquido ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_ncm
def test_rel_custo_medio_filtro_ncm_nao_incluir_produto_sem_compra():
    "Filtro NCM e não incluir produtos sem compras"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_ncm()
    confirmar_selecao()
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


## FILTRO CEST ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_preco_custo_medio_mono():
    "Filtro código cest e preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_preco_fabrica_mono():
    "Filtro código cest e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_preco_custo_mono():
    "Filtro código cest e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_preco_compra_compra_mono():
    "Filtro código cest e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_preco_liquido_compra_mono():
    "Filtro código cest e preço líquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_codigo_cest
def test_rel_custo_medio_filtro_codigo_cest_nao_incluir_produto_sem_compra():
    "Filtro código cest e não incluir produto na compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_codigo_cest()
    confirmar_selecao()
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
