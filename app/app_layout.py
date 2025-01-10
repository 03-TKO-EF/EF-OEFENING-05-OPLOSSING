import FreeSimpleGUI as sg
from bin.imagetkhelper import ImageTKHelper

sg.theme('Default1')

def appLayout():

    return [
        # -- RIJ 1
        [
            sg.Push(),
            sg.Image(source=f'assets/logo.png'),
            sg.Text(text='SLOTMACHINE', font=('Calibri', 24, 'bold')),
            sg.Push()
        ],
        # -- RIJ2
        [
            sg.Image(
                key = '-IMG-0-',
                size = (200,200),
                pad = (30,30)
            ),
            sg.Image(
                key = '-IMG-1-',
                size = (200,200),
                pad = (30,30)
            ),
            sg.Image(
                key = '-IMG-2-',
                size = (200,200),
                pad = (30,30)
            )
        ],
        # -- RIJ 3
        [
            sg.HorizontalSeparator(
                pad = (0, 10)
            )
        ],
        # -- RIJ4
        [
            sg.Text(text = 'Punten',
                    size = (7, 1),
                    pad = (0, 10),
                     justification = 'right',
                    font = ('Calibri', 16)),
            sg.Input(default_text = '',
                     size = (5,1),
                     font = ('Calibri', 16, 'bold'),
                     justification = 'right',
                     key = '-INP-PUNTEN-',
                     readonly = True),
            sg.Text(text = 'Score',
                    size = (7, 1),
                    pad = (0, 10),
                     justification = 'right',
                    font = ('Calibri', 16)),
            sg.Input(default_text = '',
                     size = (5,1),
                     font = ('Calibri', 16, 'bold'),
                     justification = 'right',
                     key = '-INP-SCORE-',
                     readonly = True),
            sg.Text(text = 'Beurten',
                    size = (7, 1),
                    pad = (0, 10),
                     justification = 'right',
                    font = ('Calibri', 16)),
            sg.Input(default_text = '',
                     size = (5,1),
                     font = ('Calibri', 16, 'bold'),
                     justification = 'right',
                     key = '-INP-BEURTEN-',
                     readonly = True),
            sg.Push(),
            sg.Button(button_text = 'Spin',
                      size = (12, 2),
                      key = '-BTN-SPIN-')
        ]
    ]