import random
import argparse
import time


random.seed(0)


class Player:
    score = 0
    wins = 0

    def __init__(self, name):
        self.name = f"Player {name}"

    def player_input(self, is_initial) -> str:
        if is_initial:
            return input(f"{self.name}'s turn. {self.name}'s score is {self.score}. Type 'r' to roll.\n")
        else:
            return input(f"{self.name}'s turn. {self.name}'s score is {self.score}. Type 'r' to roll or 'h' to hold.\n")


class ComputerPlayer(Player):
    def __init__(self, num):
        super().__init__(f"{num} (Computer)")

    def strategy(self, current_turn_total, winning_score) -> bool:
        if ((1/4) * winning_score) <= (winning_score - self.score):
            if current_turn_total >= ((1/4) * winning_score):
                time.sleep(.3)
                print(f"{self.name} holds")
                return False
            else:
                time.sleep(.3)
                return True
        elif (winning_score - self.score) <= ((1/4) * winning_score):
            if current_turn_total >= (winning_score - self.score):
                print(f"{self.name} holds")
                time.sleep(.3)
                return False
            else:
                time.sleep(.3)
                return True
        else:
            time.sleep(.3)
            return True


class PlayerFactory:

    def __init__(self, humans, computers):
        self.humans = humans
        self.computers = computers
        self.players = []

    def create_players(self) -> list:
        comp_player_num = 0
        for num in range(1, (self.humans + 1)):
            comp_player_num += 1
            player = Player(num)
            self.players.append(player)
        for num in range(1, (self.computers + 1)):
            comp_player_num += 1
            player = ComputerPlayer(comp_player_num)
            self.players.append(player)
        return self.players


class Die:
    dice = []

    def __init__(self, sides):
        self.sides = int(sides)
        Die.dice.append(self)

    def roll(self) -> int:
        roll = random.randint(1, self.sides)
        return roll


def sort_winner(player_list) -> None:
    player_list.sort(key=lambda player: player.score, reverse=True)


class Game:
    # b/c the player can't hold at the start of their turn, each turn is split into 2 "phases"
    # the is_initial_phase variable is a flag to determine which phase of the player turn it is
    is_initial_phase = False
    current_turn_total = 0
    winning_score = 100

    def __init__(self):
        self.die = Die(6)
        self.players = []

    @classmethod
    def set_winning_score(cls, score) -> None:
        cls.winning_score = score

    def initialize_game(self, humans, computers) -> None:
        pf = PlayerFactory(humans, computers)
        self.players = pf.create_players()

    def parse_input(self, player) -> bool:
        while True:
            if self.is_initial_phase:
                choice = player.player_input(self.is_initial_phase)
                if choice != 'r':
                    print(f"Invalid input.")
                    continue
                else:
                    self.is_initial_phase = False
                    return True
            else:
                choice = player.player_input(self.is_initial_phase)
                if choice == 'h':
                    print(f"{player.name} holds. {player.name}'s score is {player.score}.")
                    return False
                elif choice == 'r':
                    return True
                else:
                    print(f"Invalid input.")
                    continue

    def turn(self, player) -> None:
        self.current_turn_total = 0
        self.is_initial_phase = True
        is_continue = True
        if isinstance(player, ComputerPlayer):
            is_valid = player.strategy(self.current_turn_total, self.winning_score)
        else:
            is_valid = self.parse_input(player)
        while is_continue:
            self.is_timed(player)
            if is_valid:
                self.is_initial_phase = False
                is_good_roll = self.scoring(player)
                if is_good_roll:
                    if isinstance(player, ComputerPlayer):
                        is_continue = player.strategy(self.current_turn_total, self.winning_score)
                    else:
                        is_continue = self.parse_input(player)
                else:
                    is_continue = False

    def scoring(self, player) -> bool:
        roll = self.die.roll()
        if roll == 1:
            self.rolled_one(player)
            print(f"{player.name} rolled a {roll}, too bad. {player.name}'s score is {player.score}")
            return False
        else:
            self.add_score(player, roll)
            if player.score >= self.winning_score:
                print(f"{player.name} rolled a {roll}.")
                return False
            else:
                print(f"{player.name} rolled a {roll}.")
                print(f"{player.name}'s score is {player.score}. The current score for this turn is "
                      f"{self.current_turn_total}")
            return True

    def add_score(self, player, roll) -> None:
        self.current_turn_total += roll
        player.score += roll

    def rolled_one(self, player) -> None:
        player.score -= self.current_turn_total
        self.current_turn_total = 0

    def play_game(self, humans, computers) -> None:
        self.initialize_game(humans, computers)
        for player in self.players:
            player.score = 0
        no_winner = True
        while no_winner:
            for player in self.players:
                self.turn(player)
                if player.score >= self.winning_score:
                    print(f"{player.name} has scored {player.score}. {player.name} won!")
                    player.wins += 1
                    no_winner = False
                    break
                if not no_winner:
                    break

    def is_timed(self, player) -> None:
        if isinstance(self, TimedGameProxy):
            times_up = self.check_time(time.time())
            if times_up:
                self.players.sort(key=lambda plyr: player.score, reverse=True)
                sort_winner(self.players)
                print(f"Time's up! The winner is {self.players[0].name} with a score of {self.players[0].score}.")
                quit()


class TimedGameProxy(Game):
    def __init__(self, timed):
        super().__init__()
        self.start_time = time.time()
        self.timed = timed
        self.timer = 60

    def check_time(self, current_time) -> bool:
        if self.timed:
            if current_time - self.start_time >= self.timer:
                return True
            else:
                return False


def main():
    parser = argparse.ArgumentParser(description="Program to play the game of Pig.")
    parser.add_argument("-p", "--numPlayers",
                        help="How many human players you would like to play with, in integer format. The default is 1, "
                             "the minimum is 1, and the maximum is 10. You must enter a value within that range.",
                        type=int, choices=range(1, 11),
                        default=1)
    parser.add_argument("-c", "--numComputers",
                        help="How many computer players you would like to play with, in integer format. The default is "
                             "1, the minimum is 0, and the maximum is 10. You must enter a value within that range.",
                        type=int, choices=range(0, 11),
                        default=1)
    parser.add_argument("-t", "--timed",
                        help="Whether or not you want to play a timed game. Timed games end after 1 minute, "
                             "highest score wins.",
                        action="store_true")
    args = parser.parse_args()

    total_players = args.numPlayers + args.numComputers

    if total_players == 1:
        player_text = f"There is currently only {total_players} player."
    else:
        player_text = f"There are currently {total_players} players."

    print(f"Welcome to Pig! The rules are simple: each player repeatedly rolls a die until they roll a one or they "
          f"decide to hold. If they roll a one they score nothing and must pass the die to the next player.\nIf they "
          f"roll any other number they add it to their score and can decide to roll again or hold and pass the die to "
          f"the next player. Remember, if you roll a one at any point, your score reverts to what it was when the turn "
          f"started. {player_text} The points needed to win is {Game.winning_score}. Player 1 rolls first."
          f"\nGood luck!\n")

    game = TimedGameProxy(args.timed)
    game.play_game(args.numPlayers, args.numComputers)


if __name__ == '__main__':
    main()
