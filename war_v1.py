import random

class Solution:
    def generate_cards(self):
        print(f'Generate Called')
        self.number_of_players = 2
        #array of cards, havent distributed yet
        self.array_of_cards= []

        count = 0

        #created array of cards
        while count < self.number_of_players:
            temp = []
            for swi in range(1, 14):
                temp.append(swi)
            self.array_of_cards.extend(temp)
            count += 1

        #Shuffling cards
        random.shuffle(self.array_of_cards)
        #print(array_of_cards)
        players = []

        #distributed array of cards
        pointer = 0
        for swi in range(self.number_of_players):
            temp = self.array_of_cards[pointer:pointer+13]
            players.append(temp)
            pointer += 13

        print(f'\nplayers: {players}')

        return players

    def play_game(self, players):

        #distribute the cards in 2 players
        self.player1 = players[0]
        self.player2 = players[1]

        #this is the temp collection of the cards played by the players
        self.player1_collection = []
        self.player2_collection = []

        #rounds
        round = 1

        #play till any of the players run out of the cards
        while self.player1 and self.player2:
            # playing the card by player1 and player 2
            self.player1_card = self.player1.pop()
            self.player2_card = self.player2.pop()

            print(f'Cards Played by: self.player1: {self.player1_card} & player2: {self.player2_card}')

            # war situation
            if self.player1_card == self.player2_card:
                #add the 3 cards + war card to the temp collection

                if not self.player1:
                    self.player1Wins()
                elif not self.player2:
                    self.player2Wins()
                else:
                    self.warCards()

            elif self.player1_card > self.player2_card and self.player2_card != 1:
                # player1's card wins
                self.player1Wins()

            elif self.player1_card > self.player2_card and self.player2_card == 1:
                # player2's card wins
                self.player2Wins()

            elif self.player1_card < self.player2_card and self.player1_card == 1:
                # player1's card wins
                self.player1Wins()
            
            else:
                # player2's card wins
                self.player2Wins()

            #displaying the statistics
            print('=====================================================================')
            print(f'Stats: Rounds: {round} \nPlayer1: {self.player1} \nPlayer2: {self.player2}')
            print('=====================================================================')
            round += 1


        #One of the player has ran out of the cards
        if self.player1:
            print(f'Player 1 is the Winner')
        else:
            print(f'Player 2 is the Winner')

    def player1Wins(self):
        self.player1 = [self.player1_card, self.player2_card] + self.player1_collection + self.player2_collection + self.player1
        self.player1_collection = []
        self.player2_collection = []

    def player2Wins(self):
        self.player2 = [self.player1_card, self.player2_card] + self.player1_collection + self.player2_collection + self.player2
        self.player1_collection = []
        self.player2_collection = []

    def warCards(self):
        #add the 3 cards + war card to the temp collection
        self.player1_collection.extend([self.player1_card]+self.player1[-3:])
        #change the top card pointer to new top
        self.player1 = self.player1[:-3]
        self.player1.append(self.player1_collection.pop())

        #add the 3 cards + war card to the temp collection
        self.player2_collection.extend([self.player2_card]+self.player2[-3:])
        #change the top card pointer to new top
        self.player2 = self.player2[:-3]
        self.player2.append(self.player2_collection.pop())



if __name__ == "__main__":
    obj = Solution()

    available_deck = obj.generate_cards()
    obj.play_game(available_deck)