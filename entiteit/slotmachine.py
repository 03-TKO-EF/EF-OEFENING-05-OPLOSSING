from entiteit.afbeelding import Afbeelding

class SlotMachine:
    def __init__(self) -> None:
        '''
        constructor
        '''
        self._afbeelding = Afbeelding()
        self._aantal = 0
        self._punten = 0
        self._score = 0
        self._afbeeldingen = []

    def spin(self) -> None:
        '''
        voert een nieuwe spin uit
        - selecteert drie willekeurige afbeelding
        - berekent het behaalde aantal punten
        - verhoogd de score met het aantal behaalde punten
        - verhoogd het aantal beurten met 1
        '''
        self._aantal += 1
        self._afbeeldingen = []
        for i in range(3):
            self._afbeeldingen.append(self._afbeelding.kies())
        self._punten = 0
        if self._afbeeldingen[0] == self._afbeeldingen[1] == self._afbeeldingen[2]:
            self._punten = 3
        elif self._afbeeldingen[0] == self._afbeeldingen[1] or self._afbeeldingen[1] == self._afbeeldingen[2] or self._afbeeldingen[0] == self._afbeeldingen[2]:
            self._punten = 1

        self._score += self._punten

    def afbeeldingen(self) -> list:
        '''
        levert de list met de drie willekeurig 
        geselecteerde afbeeldingen van de huidige spin

        :return list:
        '''
        return self._afbeeldingen
    
    def punten(self) -> int:
        '''
        levert het aantal punten van de huidige spin

        :return int:
        '''
        return self._punten
    
    def score(self) -> int:
        '''
        levert de score van de huidige spin

        :return int:
        '''
        return self._score
    
    def aantal(self) -> int:
        '''
        levert het aantal beurten

        :return int:
        '''
        return self._aantal