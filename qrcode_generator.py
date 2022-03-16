import qrcode as qc
import os
import PySimpleGUI as sg

# Criar diretório na máquina do usuário
dir_qrcode = os.environ['USERPROFILE'] + r'\My QR Codes'
if not os.path.exists(dir_qrcode):
    os.mkdir(dir_qrcode)
else:
    pass

# Criar layout para tela inicial
sg.theme('BrownBlue')
layout = [
    [sg.Text('Bem-vind@ ao QR Code Generator',justification='center', font=('Times New Roman', 18, 'bold'), key='text_welcome', expand_x=True)],
    [sg.Text('Selecione um nome para o seu QR Code: ', font=('Times New Roman', 14), key='text_name'), sg.Input(font=('Times New Roman', 14), key='name', expand_x=True)],
    [sg.Text('Insira a URL desejada: ', font=('Times New Roman', 14), key='text_url'), sg.Input(font=('Times New Roman', 14), key='url', expand_x=True)],
    [sg.Button('Gerar QR Code', key='generate'), sg.Button('Cancel', key='cancel')]
]
# Criar a tela inicial
window = sg.Window('QR Code Generator - Crie seu QR Code', layout=layout, icon='qrcode_icon.ico', auto_size_text=True, auto_size_buttons=True , resizable=True, finalize=True)
window.BringToFront()

# Ler os eventos da tela
while True:
    events,values = window.read()
    if events == 'generate':
        img = qc.make(values['url'])
        img.save(os.path.join(dir_qrcode, f"qr_code_{values['name']}.png"))
        sg.popup(f'Cheque na pasta--> {dir_qrcode}',title='QR Code salvo com sucesso!', auto_close_duration=5, icon='qrcode_icon.ico', grab_anywhere=True)
    if events == sg.WINDOW_CLOSED or events == 'cancel':
        break


window.close()
