# PegaNotasGINFES
Automatização do download de notas fiscais de serviços nos municípios que utilizam o sistema GINFES

Script em Python que busca e baixa as notas em HTML apenas com o número e o código de identificação listados em linhas de um excel

# Requisitos

Python3
Módulo openpyxl, para leitura do excel
Módulo requests para obter os dados do site GINFES

Se estiver utilizando linux, basta digitar "pip install openpyxl" e "pip install requests". Para demais sistemas operacionais, seguem sites oficiais.
https://openpyxl.readthedocs.io/en/stable/
https://requests.readthedocs.io/en/master/

# Útilização

Dentro do script há comentários do que deverá ser alterado antes de sua execução. Repetindo que os números das notas deverão estar na Coluna A e os Códigos de verificação na coluna B, considerando a linha 1 o cabeçalho.

# No que você pode ajudar

Adicionar a possibilidade de baixar as notas em .pdf
Excluir/Não baixar notas que não forem encontradas.
Facilitar o uso a ponto de pessoas que não conhecem a utilização de um script consigam utiliza-lo.
