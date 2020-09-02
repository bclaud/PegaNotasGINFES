
import requests, os, openpyxl

#abertura do excel
excel = openpyxl.load_workbook('caminho para o excel contendo os dados') #insira o caminho do excel com os dados de NF e cod. de verificacao

sheet = excel.get_sheet_by_name('nome da aba') #insira o nome da aba com os dados, é importante que os números das notas estejam na coluna A e do Cod. de verificação na Coluna B, sendo a linha 1 o cabeçalho


for i in range (2, sheet.max_row + 1):
    NnotaFiscal = int(sheet['A'+ str(i)].value)  # buscando o numero da nota fiscal no arquivo excel

    NcodVerificacao = sheet['B'+ str(i)].value   # buscando o codigo de verificacao correspondente a NF no excel

    url = 'http://visualizar.ginfes.com.br/report/consultarNota?__report=nfs_ver13&cdVerificacao=' + NcodVerificacao + '&numNota=' + str(NnotaFiscal) + '&cnpjPrestador=' #URL da nota fiscal, contendo o conteudo em HTML

    NF = open('caminho onde deseja que as notas sejam salvas' + str(NnotaFiscal) +'.html', 'wb') # escolhendo o caminho para a criação e abertura do arquivo em binário
    
    res = requests.get(url) # metodo GET para a url
    NF.write(res.content) # escreve em binário o conteúdo no arquivo aberto
    NF.close() # fecha arquivo aberto