# -*- coding: UTF-8 -*-
from lamp import LampDeEscritorio #import lamp

def main():
    #Declarar instancia de la clase
    lamp = LampDeEscritorio(_is_turned_on = False)
    while True:
        comando = str(raw_input('''
        ¿Que haras?
        [p]render
        [a]pagar
        [s]alir
        '''))
        if comando == 'p':
            lamp.turn_on()
        elif comando == 'a':
            lamp.turn_off()
        elif comando == 's':
            break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    main()
