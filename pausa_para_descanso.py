
import webbrowser
import time

intervalos = 2
contador = 0

print('O programa de controle de descanso foi ativado')

while contador < intervalos:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=kjPQJpRvoeo')
    contador = contador + 1