import  time
import pyautogui
import random
import pyperclip

def bot():
    caixatexto = pyautogui.locateOnScreen('caixa-comentario.png')
    left, top = caixatexto.left, caixatexto.top
    print(left, top)
    pyautogui.click(left +10, top +10)
    time.sleep(3)
    nome = nomes_aleatorios()
    pyperclip.copy(nome)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(left, top)

def nomes_aleatorios():
    nomes = ['Manda salve!', 'Ai sim', 'Que loco', 'kkkkkkk']
    nome = random.choice(nomes)
    
    return nome

while True:
    bot()