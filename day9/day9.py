from blist import blist

PLAYERS = 459
LAST_MARBLE = 72103
# LAST_MARBLE = LAST_MARBLE * 100  # part 2
MAGIC = 23


def main():
    game = blist()  # speedy boi for part 2
    game.append(0)

    scores = [0 for _ in range(PLAYERS)]

    current_marble = 1
    current_index = 0
    current_player = 0
    while current_marble <= LAST_MARBLE:
        if len(game) == 1:
            game.append(current_marble)
            current_index = 1

        elif current_marble % MAGIC == 0:
            scores[current_player] += current_marble
            to_remove = current_index - 7
            real = len(game) + to_remove if to_remove < 0 else to_remove
            removed = game.pop(to_remove)
            scores[current_player] += removed
            current_index = real

        else:
            new_position = (current_index + 2)
            if new_position != len(game):
                new_position %= len(game)

            game.insert(new_position, current_marble)
            current_index = new_position

        current_marble += 1
        current_player += 1
        current_player %= PLAYERS

    print(max(scores))


if __name__ == '__main__':
    main()
