# Abrir uma janela com números e operções dsponíveis
from tkinter import *


def _on_key_pressed(event):
    """
    Função que captura a tecla pressionada e atualiza a calculadora com o número ou símbolo digitado
    """
    # armazenando a tecla digitada
    tecla = repr(event.char).replace('/', '÷').replace("'", "").replace('*', 'x')
    global t

    # escrevendo a tecla
    if tecla in '1234567890,':
        escrever_num(t, tecla)

    elif tecla in '+-x÷':
        escrever_simb(t, f' {tecla} ')

    elif tecla == '(':
        abrir_parenteses(t)

    elif tecla == ')':
        fechar_parenteses(t)
                        # tecla enter pressionada
    elif tecla == '=' or ('r' in tecla and len(tecla) > 1):
        # print('resolvendo a expressao')
        igual(t)

    elif 'x08' in tecla and len(tecla) == 4:
        apaga()

def check_virgula(n):
    """
    Função que checa se pode por vírgula ou não no número
    """
    numeros = 1
    # contagem de quantos numeros tem na string
    for i in n:
        if i in '+-x÷':
            numeros += 1
    
    v = n.count(',') # numero de virgulas

    if v >= numeros: # retorna falso se tem mais virgula q numero
        return  False
    else:
        return True
    
def criar_janela():
    """
    Função que cria a janela
    """
    janela = Tk()
    janela.title('Calculadora em python!')
    janela.grid()
    janela.geometry('214x339')
    return janela

def escrever_simb(t,símbolo):
    'Escreve um símbolo de uma operação matemática'
    global valores
    try:
        if valores[-1] not in ' ':
            valores += símbolo
            t.set(valores)
    except(IndexError):
        pass

def igual(t):
    'Calcula o resultado da operação'
    global valores
    if len(valores) > 0 and valores[-1].isnumeric():
        # substituição dos simbolos para o calculo da operacao
        valores =valores.replace('x', '*')
        valores =valores.replace('÷', '/')
        valores = valores.replace(",",".")
        
        # calculo e atualizacao do resultado na tela
        valores = float(eval(valores))
        if  not (valores).is_integer():
            casas_virgula = len(str(valores)) - 1 - str(valores).find('.') # calculo para descobrir o numero de casas apos a virgula

            if casas_virgula < 8:
                match casas_virgula:
                    case 1:
                        valores = f'{valores:.1f}'
                    case 2:
                        valores = f'{valores:.2f}'
                    case 3:
                        valores = f'{valores:.3f}'
                    case 4:
                        valores = f'{valores:.4f}'
                    case 5:
                        valores = f'{valores:.5f}'
                    case 6:
                        valores = f'{valores:.6f}'
                    case 7:
                        valores = f'{valores:.7f}'
            
            else:                   
                valores = f'{valores:.5f}'
                
            valores = str(valores)
        
        else:
            valores = str(valores)
            valores = valores.replace('.0','')

        valores = valores.replace(".",",")
        t.set(valores)

def abrir_parenteses(t):
    'Abre parênteses na operação'
    global valores
    global np

    if valores != '0':
        valores += '('
        np += 1
        t.set(valores)
    elif valores == '0':
        valores = '('
        np += 1
        t.set(valores)
        
def fechar_parenteses(t):
    'Fecha parênteses na operação'
    global valores
    global np
    # verificamos se tem parenteses aberto na operação antes de fechar
    if np > 0:
        valores+=')'
        np -= 1
        t.set(valores)
        
def escrever_num(t, simbolo):
    'Escreve um número'
    global valores
    if simbolo != ',':
        if valores == '0':
            valores = simbolo
        elif valores == '' or valores[-1]  in '1234567890,( ':
            valores += simbolo
    else:
        if check_virgula(valores) and valores != '':
            valores += simbolo

    t.set(valores)
def apaga():
    'Apaga valores já escritos'
    global t
    global valores
    try:
        if valores[-1] in '1234567890,()':
            valores = valores[:-1]
        elif valores[-1] in ' ':
            valores = valores[:-3]
        t.set(valores)
    except(IndexError):
        print()

def escrever0():
    'Escreve o número 0 assim que a calculadora é iniciada.'
    t.set('0')
    return  t


janela =criar_janela() # Criação da janela aonde a calculadora será executada
t = StringVar() # Variável que armazena o texto exibido na calculadora
valores = '0' # Variável para auxiliar na exibição do código
np = 0 # Variável para contabilizar o número de parênteses abertos e fechados
frame1 = Frame(janela, width=212, height=50,bg='gray90').grid(row=0,column=0)
frame2 = Frame(janela, width=214, height=268).grid(row=1, column=0)
nmros_digitados = Label(frame1,textvariable=t, width=14,height=1,padx=4,pady=13, relief=FLAT,anchor='e',bg='gray90'
                        ,justify=RIGHT, font='Ivy 18').place(x=0,y=0)


# Botões das operações
soma = Button(frame2, text='+', command=lambda :escrever_simb(t,' + '), height=3, width=6, bg='#fa954d').place(x=0,y=50)
subtracao = Button(frame2, text='-', command=lambda :escrever_simb(t,' - '), height=3, width=6, bg='#fa954d').place(x=54, y=50)
multiplicacao = Button(frame2, text='x', command=lambda :escrever_simb(t,' x '), height=3, width=6, bg='#fa954d').place(x= 108,y=50)
apagar = Button(frame2, text='⌫', command=lambda :apaga(), height=3, width=6, bg='#fa594d').place(x=162,y=50)
divisao = Button(frame2, text='÷', command=lambda :escrever_simb(t,' ÷ '), height=3, width=6, bg='#fa954d').place(x=162,y=108)
resultado = Button(frame2, text='=', command=lambda :igual(t), height=3, width=6,bg='#4162f2').place(x=162,y=224+58)

# Números e dígitos
sete = Button(frame2, text='7', command=lambda:escrever_num(t,'7'), height=3, width=6).place(x=0,y=108)
oito = Button(frame2, text='8', command=lambda:escrever_num(t,'8'), height=3, width=6).place(x=54,y=108)
nove = Button(frame2, text='9', command=lambda:escrever_num(t,'9'), height=3, width=6).place(x=108,y=108)
quatro = Button(frame2, text='4', command=lambda:escrever_num(t,'4'), height=3, width=6).place(x=0,y=166)
cinco = Button(frame2, text='5', command=lambda:escrever_num(t,'5'), height=3, width=6).place(x=54,y=166)
seis = Button(frame2, text='6', command=lambda:escrever_num(t,'6'), height=3, width=6).place(x=108,y=166)
um = Button(frame2, text='1', command=lambda:escrever_num(t,'1'), height=3, width=6).place(x=0,y=224)
dois = Button(frame2, text='2', command=lambda:escrever_num(t,'2'), height=3, width=6).place(x=54,y=224)
tres = Button(frame2, text='3', command=lambda:escrever_num(t,'3'), height=3, width=6).place(x=108,y=224)
zero = Button(frame2, text='0', command=lambda:escrever_num(t,'0'), height=3, width=6).place(x=54,y=282)
virgula = Button(frame2, text=',', command=lambda:escrever_num(t,','), height=3, width=6).place(x=108,y=282)

# botao de sair
sair = Button(frame2, text='Exit', command=lambda:exit(t), height=3, width=6, bg='#fa594d').place(x=0, y=282)

# Parênteses
abre_prts = Button(frame2, text='(', command=lambda:abrir_parenteses(t), height=3, width=6, bg='#fa954d').place(x=162,y=166)
fecha_prts = Button(frame2, text=')', command=lambda:janela.destroy, height=3, width=6, bg='#fa954d').place(x=162,y=224)

escrever0()

janela.bind(sequence="<Key>", func=_on_key_pressed)
janela.mainloop()