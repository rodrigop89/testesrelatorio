"""Teste base para o relatório custo médio de vendas sistema filial com os filtros
categoria, margem de lucro, grupo de produtos, grupo de comissão, 
grupo de remarcação de preços e grupo de icms """
# pylint: disable=C0301

from pytest import mark
from lib.dados.dados_sistema import LOJA
from lib.dados.lista_relatorios import COD_4
from lib.dados.sistema import digitar_codigo_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    confirmar_selecao,
    fechar_abaimpressao,
    fechar_sistemarelatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_categoria,
    selecionar_demais_filtros,
    selecionar_empresas,
    selecionar_grupo_icms,
    selecionar_grupo_produto,
    selecionar_grupo_remarcacao,
    selecionar_margem_lucro,
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

## FILTRO CATEGORIA ##


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_preco_custo_medio_filial():
    "Filtro categoria e preço custo médio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_preco_fabrica_filial():
    "Filtro categoria e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_preco_custo_filial():
    "Filtro categoria e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_preco_bruto_compra_filial():
    "Filtro categoria e preço bruto última compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_preco_liquido_compra_filial():
    "Filtro categoria e preço liquido última compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_categoria
def test_rel_custo_medio_filtro_categoria_nao_incluir_produtos_sem_compra():
    "Filtro categoria e não incluir produtos sem compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_categoria()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO MARGEM DE LUCRO


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_preco_custo_medio_filial():
    "Filtro margem de lucro e preço de custo médio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_preco_fabrica_filial():
    "Filtro margem de lucro e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_preco_custo_filial():
    "Filtro margem de lucro e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_preco_bruto_compra_filial():
    "Filtro margem de lucro e preço bruto da última compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_preco_liquido_compra_filial():
    "Filtro margem de lucro e preço liquido da ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_margem_de_lucro
def test_rel_custo_medio_filtro_margem_lucro_nao_incluir_produtos_sem_compra_filial():
    "Filtro margem de lucro e não incluir produto sem compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_margem_lucro()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO GRUPO DE PRODUTO


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_preco_custo_medio_filial():
    "Filtro grupo de produto e preço de custo médio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_preco_fabrica_filial():
    "Filtro grupo de produto e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_preco_custo_filial():
    "Filtro grupo de produto e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_preco_bruto_compra_filial():
    "Filtro grupo de produto e preço bruto última compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_preco_liquido_compra_filial():
    "Filtro grupo de produto e preço líquido da ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_produto
def test_rel_custo_medio_filtro_grupo_produto_nao_incluir_produtos_sem_compra_filial():
    "Filtro grupo de produto e não incluir produto sem compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO GURPO COMISSÃO


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_preco_custo_medio_filial():
    "Filtro grupo de comissão e preço de custo médio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_preco_fabrica_filial():
    "Filtro grupo de comissão e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_preco_custo_filial():
    "Filtro grupo de comissão e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_preco_bruto_compra_filial():
    "Filtro grupo de comissão e preço bruto da última compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_preco_liquido_compra_filial():
    "Filtro grupo de comissão e preço liquido da ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_comissao
def test_rel_custo_medio_filtro_grupo_comissao_nao_incluir_produtos_sem_compra_filial():
    "Filtro grupo de comissão e não incluir produtos sem compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_produto()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO GRUPO DE REMARCAÇÃO DE PREÇO


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_preco_custo_medio_filial():
    "Flitro gurpo de remarcação e preço de custo medio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_preco_fabrica_filial():
    "Flitro gurpo de remarcação e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_preco_custo_filial():
    "Flitro gurpo de remarcação e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_preco_bruto_compra_filial():
    "Flitro gurpo de remarcação e preço bruto ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_preco_liquido_compra_filial():
    "Flitro gurpo de remarcação e preço bruto liquido ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_remarcacao
def test_rel_custo_medio_filtro_grupo_remarcacao_nao_incluir_produto_sem_compra_filial():
    "Flitro gurpo de remarcação e não incluir produtos sem compra no período"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_remarcacao()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


# FILTRO GRUPO DE ICMS


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_preco_custo_medio_filial():
    "Filtro grupo de icms e preço de custo médio"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_preco_fabrica_filial():
    "Filtro grupo de icms e preço de fábrica"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_preco_custo_filial():
    "Filtro grupo de icms e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_preco_bruto_compra_filial():
    "Filtro grupo de icms e preço bruto da ultima compra"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_preco_liquido_compra_filial():
    "Filtro grupo de icms e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
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
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)


@mark.emitir_rel_custo_medio_vendas_filial_filtro_grupo_icms
def test_rel_custo_medio_filtro_grupo_icms_nao_incluir_produto_sem_compra_filial():
    "Filtro grupo de icms e preço de custo"
    login_sistema()
    digitar_codigo_relatorio(COD_4)
    selecionar_empresas(LOJA)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_grupo_icms()
    confirmar_selecao()
    selecionar_custo_medio_baseado_nas_compras()
    informar_periodo()
    selecionar_filtro_nao_incluir_produtos_nao_possuem_compra_periodo()
    selecionar_periodo()
    informar_periodo()
    esperar_tempo(TEMPO_ESPERA)
    imprimir_relatorio()
    esperar_tempo(TEMPO_IMPRESSAO)
    fechar_abaimpressao()
    sair_relatorio()
    fechar_sistemarelatorio()
    esperar_tempo(TEMPO_ESPERA)
