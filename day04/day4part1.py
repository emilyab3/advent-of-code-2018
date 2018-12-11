import os
import datetime
from parse import *
from typing import Tuple, Dict


FALLS_ASLEEP = -1
WAKES_UP = 0


def decode_time(encoded: str) -> Tuple:
    """
    Takes an encoded string of the format "[yyyy-mm-dd hh:mm] some_message" and decodes
    it into a datetime object and the message
    :param encoded: the string to be decoded
    :return: a datetime object extracted from the string and its corresponding message
    """
    parsed = parse("[{year:d}-{month:d}-{day:d} {hour:d}:{minute:d}] {message}",
                   encoded)
    date_time = datetime.datetime(parsed["year"], parsed["month"], parsed["day"],
                                  parsed["hour"], parsed["minute"])

    if parsed["message"] == "wakes up":
        detail = WAKES_UP
    elif parsed["message"] == "falls asleep":
        detail = FALLS_ASLEEP
    else:
        detail = parse("Guard #{guard_id:d} begins shift", parsed["message"])["guard_id"]

    return date_time, detail


def read_input(filename: str) -> Dict:
    """
    Reads input from the given file and returns a mapping from the datetimes in the
    file to their corresponding messages
    :param filename: the file to read
    :return: the mapping from datetimes to messages
    """
    shifts = {}
    with open(filename, 'r') as file:
        for line in file:
            date_time, detail = decode_time(line.strip())
            shifts[date_time] = detail

    return shifts


def get_guard_movements(shifts: Dict) -> Tuple[Dict, Dict[int, Dict]]:
    """
    Parses the given raw shifts to return useful mappings
    :param shifts: the shifts to parse
    :return: a tuple of two different dictionary representations of the data -
        1. Guard ID mapped to total time that guard spent sleeping
        2. Guard ID mapped to {minute : number of times sleeping that minute}
    """
    # to ensure that the shifts are in order
    chronological = sorted(shifts.keys())

    total_time = {}
    shifts_worked = {}

    current_guard = None
    sleep_time = None
    for date in chronological:
        detail = shifts[date]

        if detail == WAKES_UP:
            # mark each minute in the range before waking up as being asleep
            for minute in range(sleep_time.minute, date.minute):
                if minute not in shifts_worked[current_guard]:
                    shifts_worked[current_guard][minute] = 0

                shifts_worked[current_guard][minute] += 1
                total_time[current_guard] += 1

        elif detail == FALLS_ASLEEP:
            # record that the guard is sleeping
            sleep_time = date

        else:
            current_guard = detail
            if current_guard not in shifts_worked:
                shifts_worked[current_guard] = {}
            if current_guard not in total_time:
                total_time[current_guard] = 0

    return total_time, shifts_worked


def sleepiest_guard(total_time: Dict[int, int]) -> int:
    """
    Finds the guard who spent the most time sleeping in total
    :param total_time: a mapping from guards to the time they spent sleeping
    :return: the guard who slept the longest overall
    """
    longest_guard = None
    current_best = 0
    for guard in total_time:
        if total_time[guard] > current_best:
            current_best = total_time[guard]
            longest_guard = guard

    return longest_guard


def sleepiest_minute(guard: int, shifts_worked: Dict) -> int:
    """
    Determines which minute (between 00:00 and 00:23) the given guard slept for the
    longest overall
    :param guard: the guard to examine
    :param shifts_worked: the record of shifts worked
    :return: the minute which the given guard slept the most at
    """
    best_minute = -1
    best_count = 0
    entries = shifts_worked[guard]
    for minute in entries:
        if entries[minute] > best_count:
            best_count = entries[minute]
            best_minute = minute

    return best_minute


def main():
    input_file = os.path.join(os.getcwd(), "input")
    shifts = read_input(input_file)

    total_time, shifts_worked = get_guard_movements(shifts)
    longest_guard = sleepiest_guard(total_time)
    best_minute = sleepiest_minute(longest_guard, shifts_worked)

    result = longest_guard * best_minute

    print("The ID multiplied by the minute is {}".format(result))


if __name__ == '__main__':
    main()
