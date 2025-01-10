from random import choices

class Afbeelding:
    def __init__(self) -> None:
        '''
        constructor
        '''
        self._afbeeldingen = ['aardbei.png', 'appel.png', 'banaan.png', 'kers.png', 'peer.png']

    def kies(self) -> str:
        '''
        selecteert een willekeurige afbeelding

        :return: str
        >>> a = Afbeelding()
        >>> a.pikken() in ['aardbei.png', 'appel.png', 'banaan.png', 'kers.png', 'peer.png']
        True
        '''
        return choices(self._afbeeldingen, k=1)[0]
    
if __name__ == '__main__':
    from doctest import testmod
    testmod()