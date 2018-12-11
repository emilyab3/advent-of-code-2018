import os
from day04.day4part1 import read_input, get_guard_movements


def most_consistently_sleepy_guard(shifts_worked):
    """
    Determines which guard is the most frequently asleep at the same minute from those
    given in the shifts record
    :param shifts_worked: the record of the shifts
    :return: the guard who slept the most frequently at a single given minute, along
        with which minute this was
    """
    best_minute = -1
    best_guard = 0
    best_count = 0
    for guard in shifts_worked:
        entries = shifts_worked[guard]
        for minute in entries:
            if entries[minute] > best_count:
                best_count = entries[minute]
                best_minute = minute
                best_guard = guard

    return best_guard, best_minute


def main():
    input_file = os.path.join(os.getcwd(), "input")
    shifts = read_input(input_file)

    total_time, shifts_worked = get_guard_movements(shifts)
    best_guard, best_minute = most_consistently_sleepy_guard(shifts_worked)

    result = best_guard * best_minute

    print("The ID multiplied by the minute is {}".format(result))


if __name__ == '__main__':
    main()
