import FreeSimpleGUI as sg
from .app_layout import appLayout

from entiteit.slotmachine import SlotMachine

from bin.imagetkhelper import ImageTKHelper

class App:
    def __init__(self):
        self._slotmachine = SlotMachine()

    def toon(self):
        venster = sg.Window(
            title = 'SLOTMACHINE',
            icon = 'assets/favicon.ico',
            layout = appLayout(),
            return_keyboard_events = True,
            finalize = True
        )

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED:
                    break

                case '-BTN-SPIN-':
                    self._slotmachine.spin()
                    afbeeldingen = self._slotmachine.afbeeldingen()
                    punten = self._slotmachine.punten()
                    score = self._slotmachine.score()
                    aantal = self._slotmachine.aantal()

                    for ndx, afbeelding in enumerate(afbeeldingen):
                        pad = f'assets/{afbeelding}'
                        venster[f'-IMG-{ndx}-'].update(data=ImageTKHelper.schaal(pad))

                    venster['-INP-PUNTEN-'].update(punten)
                    venster['-INP-SCORE-'].update(score)
                    venster['-INP-BEURTEN-'].update(aantal)

                    venster.refresh()

        venster.close()