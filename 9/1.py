from collections import deque;

class Game(object):
    def __init__(self, numOfPlayers, lastMarble):
        self.lastMarble = lastMarble;
        self.numOfPlayers = numOfPlayers;
        self.current = 0;
        self.match = deque([0]);
        self.currentPlayer = 1;
        self.playerPoints = {i: 0 for i in range(1,numOfPlayers + 1)};

    def insert(self, number):
        if number % 23 == 0:
            self.playerPoints[self.currentPlayer] += number;
            self.match.rotate(7);
            self.playerPoints[self.currentPlayer] += self.match.popleft();
        else:
            self.current = number;
            self.match.rotate(-2);
            self.match.appendleft(number);

        self.nextPlayer();

    def nextPlayer(self):
        self.currentPlayer = ((self.currentPlayer) % self.numOfPlayers) + 1;

    def play(self):
        for number in range(1, self.lastMarble + 1):
            self.insert(number);
        
        return self.playerPoints;

def solution(numOfPlayers, lastMarble):
    game = Game(numOfPlayers, lastMarble);
    game.play();
    return max(game.playerPoints.values());

print(solution(418, 71339));
#Part 2
#print(solution(418, 71339 * 100));
