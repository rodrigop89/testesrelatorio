"""Teste base para o relatório custo médio de vendas sistema mono com os filtros
Fabricante, Linha, Seção, Lista SNGPC e Principio Ativo"""


from pytest import mark
from lib.dados.lista_relatorios import COD_4
from lib.dados.sistema import digitar_nome_relatorio, login_sistema
from lib.dados.tempo import TEMPO_ESPERA, TEMPO_IMPRESSAO
from lib.formulario.generico.f_generico import (
    confirmar_selecao,
    fechar_aba_impressao,
    fechar_sistema_relatorio,
    imprimir_relatorio,
    informar_periodo,
    sair_relatorio,
    selecionar_demais_filtros,
    selecionar_fabricante,
    selecionar_linha,
    selecionar_lista_sngpc,
    selecionar_periodo,
    selecionar_principio_ativo,
    selecionar_secao,
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


## FILTRO SOMENTE FABRICANTE ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_preco_custo_medio_mono():
    "Filtro fabricante e preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_preco_fabrica_mono():
    "Filtro fabricante e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_preco_custo_mono():
    "Filtro fabricante e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_preco_bruto_compra_mono():
    "Filtro fabricante e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_preco_liquido_compra_mono():
    "Filtro fabricante e preço liquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_fabricante
def test_rel_custo_medio_filtro_fabricante_nao_incluir_produtos_sem_compra_mono():
    "Filtro fabricante e não incluir produtos sem compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
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


# FILTRO LINHA ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_preco_custo_medio_mono():
    "Filtro linha e por preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_linha()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_preco_fabrica_mono():
    "Filtro linha e por preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_linha()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_preco_custo_mono():
    "Filtro linha e por preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_linha()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_preco_bruto_compra_mono():
    "Filtro linha e por preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_linha()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_preco_liquido_compra_mono():
    "Filtro linha e por preço liquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
    selecionar_linha()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_linha
def test_rel_custo_medio_filtro_linha_nao_incluir_produtos_sem_compra_mono():
    "Filtro linhae não incluir produtos sem compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_linha()
    esperar_tempo(TEMPO_ESPERA)
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


## FILTRO SEÇÃO ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_preco_custo_medio_mono():
    "Filtro seção e preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_secao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_preco_fabrica_mono():
    "Filtro seção e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_secao()
    esperar_tempo(TEMPO_ESPERA)
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_preco_custo_mono():
    "Filtro seção e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_secao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_preco_bruto_compra_mono():
    "Filtro seção e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_secao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_preco_liquido_compra_mono():
    "Filtro seção e preço liquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
    selecionar_secao()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_secao
def test_rel_custo_medio_filtro_secao_nao_incluir_produtos_sem_compra_mono():
    "Filtro seção e não incluir produtos sem compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_secao()
    esperar_tempo(TEMPO_ESPERA)
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


## FILTRO LISTA SNGPC ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_preco_custo_medio_mono():
    "Filtro lista sngpc e preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_lista_sngpc()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_preco_fabrica_mono():
    "Filtro lista sngpc e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_lista_sngpc()
    esperar_tempo(TEMPO_ESPERA)
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_preco_custo_mono():
    "Filtro lista sngpc e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_lista_sngpc()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_preco_bruto_compra_mono():
    "Filtro lista sngpc e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_lista_sngpc()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_preco_liquido_compra_mono():
    "Filtro lista sngpc e preço liquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
    selecionar_lista_sngpc()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_lista_sngpc
def test_rel_custo_medio_filtro_lista_sngpc_nao_incluir_produtos_sem_compra_mono():
    "Filtro lista sngpc e não incluir produtos sem compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_lista_sngpc()
    esperar_tempo(TEMPO_ESPERA)
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


## FILTRO PRINCIPIO ATIVO ##


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_preco_custo_medio_mono():
    "Filtro principio ativo e preço de custo médio"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_principio_ativo()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_preco_fabrica_mono():
    "Filtro principio ativo e preço de fábrica"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_principio_ativo()
    esperar_tempo(TEMPO_ESPERA)
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_preco_custo_mono():
    "Filtro principio ativo e preço de custo"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_principio_ativo()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_preco_bruto_compra_mono():
    "Filtro principio ativo e preço bruto da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_principio_ativo()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_preco_liquido_compra_mono():
    "Filtro principio ativo e preço liquido da ultima compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_fabricante()
    selecionar_principio_ativo()
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


@mark.emitir_rel_custo_medio_vendas_mono_filtro_principio_ativo
def test_rel_custo_medio_filtro_principio_ativo_nao_incluir_produtos_sem_compra_mono():
    "Filtro princpio ativo e não incluir sem produtos sem compra"
    login_sistema()
    digitar_nome_relatorio(COD_4)
    esperar_tempo(TEMPO_ESPERA)
    selecionar_filtro_especifico()
    selecionar_demais_filtros()
    selecionar_principio_ativo()
    esperar_tempo(TEMPO_ESPERA)
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
