# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:39:45 2021

@author: LisboaJ
"""
# auto-py-to-exe para criar executável

#Importa a biblioteca
import PySimpleGUI as sg


# Layouts das janelas
    
def faz_janela1():
        
    sg.theme('DarkBlue')
        
    layout = [[sg.Text('TCalc V1.2')],
              [sg.Text(' ')],
              [sg.Text('Selecione a opção desejada\n', key=('-TITULO-'))],     #Texto 
              [sg.Button('Converter mm/rot para mm/min', key=('-COMP-'), size=(35, 1))], #janela2
              [sg.Button('Calcular RPM', key=('-ROT-'), size=(35, 1))],  #janela3
              [sg.Button('Converter mm/min em mm/rot', key=('-AVA-'), size=(35, 1))],  #janela4
              [sg.Button('Tempo de corte', key=('-TEMPO-'), size=(35, 1))],  #janela5
              [sg.Button('Rugosidade teórica', key=('-RUG-'), size=(35, 1))],  #janela6
              [sg.Text(' ')],
              #[sg.Text('PIX: 039.479.240-89')],
              [sg.Button('Sair', key=('SAI'), size=(35, 1))]]  
    
    return sg.Window('Principal', layout, location=(800,600), finalize=True, no_titlebar=True, grab_anywhere=True)

def faz_janela2():
    layout = [[sg.Text('Converter avanço mm/rot para mm/min\n')],
              [sg.Text('Qual é o avanço(mm/rot)?')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text('Qual é a RPM(S)?')],
              [sg.Input(key='-IN2-', enable_events=True)],
              [sg.Text('Resultado')],
              [sg.Text(' ',size=(25,1), k='-OUTPUT-')],
              [sg.Text('')],
              [sg.Button('Calcular', key=('CalcularComprimento')),sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Comprimento', layout, finalize=True, no_titlebar=True, grab_anywhere=True)

def faz_janela3():  #Rotação do eixo principal
    layout = [[sg.Text('Rotação do eixo principal')],
              [sg.Text('Qual é a Velocidade de Corte (VC)?')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text('Qual é o Diâmetro?')],
              [sg.Input(key='-IN2-', enable_events=True)],
              [sg.Text('Resultado')],
              [sg.Text(' ',size=(25,1), k='-OUTPUT-')],
              [sg.Text(' ')],
              [sg.Button('Calcular', key=('CalcularRPM')),sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('RPM', layout, finalize=True, no_titlebar=True, grab_anywhere=True)

def faz_janela4():
    layout = [[sg.Text('Converter avanço mm/min em mm/rot')],
              [sg.Text('RPM do eixo principal (S)')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text('Avanço (mm/min)')],
              [sg.Input(key='-IN2-', enable_events=True)],
              [sg.Text('Resultado')],
              [sg.Text(' ',size=(25,1), k='-OUTPUT-')],
              [sg.Text(' ')],
              [sg.Button('Calcular', key=('CalcularAVA')),sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Avanço por rotação', layout, finalize=True, no_titlebar=True, grab_anywhere=True)

def faz_janela5():
    layout = [[sg.Text('Tempo de corte')],
              [sg.Text('Comprimento da peça (mm)')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text('Comprimento usinado por minuto (mm/min)')],
              [sg.Input(key='-IN2-', enable_events=True)],
              [sg.Text('Resultado')],
              [sg.Text(' ',size=(25,1), k='-OUTPUT-')],
              [sg.Text(' ')],
              [sg.Button('Calcular', key=('CalcularTC')),sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Tempo de corte', layout, finalize=True, no_titlebar=True, grab_anywhere=True)

def faz_janela6():
    layout = [[sg.Text('Rugosidade teórica')],
              [sg.Text('Qual é o avanço por rotação(mm/rot)?')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text('Qual é o raio do inserto(mm)?')],
              [sg.Input(key='-IN2-', enable_events=True)],
              [sg.Text('Resultado')],
              [sg.Text(' ',size=(25,1), k='-OUTPUT-')],
              [sg.Text(' ')],
              [sg.Button('Calcular', key=('CalcularRUG')),sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Rugosidade Teórica', layout, finalize=True, no_titlebar=True, grab_anywhere=True)
        

# Define a primeira janela a iniciar          
window1, window2 = faz_janela1(), None    
    
        
while True:                     
     
    janela, eventos, valores = sg.read_all_windows()     
            
    if eventos == 'SAI' or eventos == 'Sair': #Eventos que fecham a janela
        janela.close()
        if janela == window2:       # if closing win 2, mark as closed
            window2 = None
        elif janela == window1:     # if closing win 1, exit program
            break
    
    elif eventos == '-COMP-' and not window2:
        window2 = faz_janela2()
        
    elif eventos == 'CalcularComprimento':
            try:
                f = float(valores['-IN-'])
                n = float(valores['-IN2-'])
                res = float()
                
                res = (f * n)
                print(res)
                
                janela['-OUTPUT-'].update(f'A velocidade é de {res:.0f} mm/min')
                
            except:
                janela['-OUTPUT-'].update('Valor incorreto!')
                        
    elif eventos == '-ROT-' and not window2:
        window2 = faz_janela3()
        
    elif eventos == 'CalcularRPM':
            try:
                vc = float(valores['-IN-'])
                dia = float(valores['-IN2-'])
                res = float()
                
                res = ((vc * 318)/ dia)
                print(res)
                
                janela['-OUTPUT-'].update(f'{res:.0f} rpm')
            
            except:
                janela['-OUTPUT-'].update('Valor incorreto!')
                
    elif eventos == '-AVA-' and not window2:
        window2 = faz_janela4()
        
    elif eventos == 'CalcularAVA':
            try:
                n = float(valores['-IN-'])
                l = float(valores['-IN2-'])
                res = float()
                
                res = (l / n)
                print(res)
                
                janela['-OUTPUT-'].update(f'{res:.2f} mm/rot')
            
            except:
                janela['-OUTPUT-'].update('Valor incorreto!')
        
    elif eventos == '-TEMPO-' and not window2:
        window2 = faz_janela5()
        
    elif eventos == 'CalcularTC':
            try:
                lm = float(valores['-IN-'])
                l = float(valores['-IN2-'])
                res = float()
                
                res = (lm / l)
                seg = (res * 60)
                print(res)
                
                janela['-OUTPUT-'].update(f'{res:.2f} min ou {seg:.0f} seg\n')
            
            except:
                janela['-OUTPUT-'].update('Valor incorreto!')
    
    elif eventos == '-RUG-' and not window2:
        window2 = faz_janela6()
        
    elif eventos == 'CalcularRUG':
            try:
                f = float(valores['-IN-'])
                re = float(valores['-IN2-'])
                res = float()
                
                res = (((f*f)/(8*re))*1000)
                print(res)
                
                janela['-OUTPUT-'].update(f'A rugosidade teórica é de {res:.2f} µm')
            
            except:
                janela['-OUTPUT-'].update('Valor incorreto!')
        
    elif eventos == 'Limpar':
        janela['-OUTPUT-'].update('')
        janela['-IN-'].update('')
        janela['-IN2-'].update('')
                         
                 
janela.close() #Fechamento da aplicação
        

    

    
        

