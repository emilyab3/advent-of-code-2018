import os
import datetime
from parse import *


FALLS_ASLEEP = -1
WAKES_UP = 0


def decode_time(encoded: str):
    # [1518-08-21 00:39] wakes up
    parsed = parse("[{year:d}-{month:d}-{day:d} {hour:d}:{minute:d}] {message}", encoded)
    date_time = datetime.datetime(parsed["year"], parsed["month"], parsed["day"], parsed["hour"], parsed["minute"])

    if parsed["message"] == "wakes up":
        detail = WAKES_UP
    elif parsed["message"] == "falls asleep":
        detail = FALLS_ASLEEP
    else:
        detail = parse("Guard #{guard_id:d} begins shift", parsed["message"])["guard_id"]

    return date_time, detail


def read_input(filename: str):
    shifts = {}
    with open(filename, 'r') as file:
        for line in file:
            date_time, detail = decode_time(line.strip())
            shifts[date_time] = detail

    return shifts


def main():
    input_file = os.path.join(os.getcwd(), "input")
    shifts = read_input(input_file)

    dates = shifts.keys()
    chronological = sorted(dates)
    total_time = {}
    shifts_worked = {}
    current_guard = None
    sleep_time = None
    for date in chronological:
        detail = shifts[date]

        if detail == WAKES_UP:
            for minute in range(sleep_time.minute, date.minute):
                if minute not in shifts_worked[current_guard]:
                    shifts_worked[current_guard][minute] = 0

                shifts_worked[current_guard][minute] += 1
                total_time[current_guard] += 1
        elif detail == FALLS_ASLEEP:

            sleep_time = date
        else:
            current_guard = detail
            if current_guard not in shifts_worked:
                shifts_worked[current_guard] = {}
            if current_guard not in total_time:
                total_time[current_guard] = 0

    longest_guard = None
    current_best = 0
    for guard in total_time:
        if total_time[guard] > current_best:
            current_best = total_time[guard]
            longest_guard = guard

    best_minute = -1
    best_count = 0
    entries = shifts_worked[longest_guard]
    for minute in entries:
        if entries[minute] > best_count:
            best_count = entries[minute]
            best_minute = minute

    result = longest_guard * best_minute

    print("The ID multiplied by the minute is {}".format(result))

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

    result = best_guard * best_minute

    print("The ID multiplied by the minute is {}".format(result))


if __name__ == '__main__':
    main()
