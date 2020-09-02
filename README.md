# PegaNotasGINFES
<br/>Automatização do download de notas fiscais de serviços nos municípios que utilizam o sistema GINFES

<br/>Script em Python que busca e baixa as notas em HTML apenas com o número e o código de verificação listados em linhas de um excel

# Requisitos

<br/>Python3
<br/>Módulo openpyxl, para leitura do excel
<br/>Módulo requests para obter os dados do site GINFES

<br/>Se estiver utilizando linux, basta digitar "pip install openpyxl" e "pip install requests". Para demais sistemas operacionais, seguem sites oficiais.
<br/>https://openpyxl.readthedocs.io/en/stable/
<br/>https://requests.readthedocs.io/en/master/

# Utilização

<br/>Dentro do script há comentários do que deverá ser alterado antes de sua execução. Repetindo que os números das notas deverão estar na Coluna A e os Códigos de verificação na coluna B, considerando a linha 1 o cabeçalho.

# No que você pode ajudar

<br/>Adicionar a possibilidade de baixar as notas em .pdf
<br/>Excluir/Não baixar notas que não forem encontradas.
<br/>Facilitar o uso a ponto de pessoas que não conhecem a utilização de um script consigam utiliza-lo.
