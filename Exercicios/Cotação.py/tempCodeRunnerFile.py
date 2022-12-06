import PySimpleGUI as sg

layout = [
[sg.Text('Cotação de moedas')],
[sg.inputText()],
[sg.Button('Pegar cotação'), sg.Button('Cancelar')],
[sg.Text('A cotação foi de')]
]

janela = sg.Window('Titulo da janela', layout)

while True: 
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break

janela.close()