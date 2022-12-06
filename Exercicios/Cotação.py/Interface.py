import PySimpleGUI as sg
from Cotação import pegar_cotacoes

sg.theme('DarkPurple1')

layout = [
[sg.Text('Cotação de moedas')],
[sg.InputText(key= 'nome_cotação')],
[sg.Button('Pegar cotação'), sg.Button('Cancelar')],
[sg.Text('', key='texto_cotação')],
]

janela = sg.Window('Sistema de cotações!!!', layout)

while True: 
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento ==  'Cancelar':
        break
    if evento == 'Pegar cotação':
        codigo_cotação = valores['nome_cotação']
        cotacao = pegar_cotacoes(codigo_cotação)
        janela['texto_cotação'].update(f'A cotação do {codigo_cotação} é de R${cotacao}')
    

janela.close()