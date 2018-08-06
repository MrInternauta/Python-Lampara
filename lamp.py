# -*- coding: UTF-8 -*-


class LampDeEscritorio:
    #Variable (Lista) de clase
    _LAMPS = ['''
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
        '''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|

    ''']
    #Metodo principal (contructor)
    def __init__(self, _is_turned_on):
        #VARIABLE privada
        self._is_turned_on = _is_turned_on #Variable privada
        self._display_image()
    #Metodos publicos
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    #Metodo privado
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
