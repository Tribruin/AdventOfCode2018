#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from datetime import datetime
from AOC import AOC


testing = False


class Guard:
    def __init__(self, id) -> None:

        self.id = id
        self.days = dict()
        self.total_sleep_time = 0
        self.sleepist_minute = 0
        self.sleepist_minute_total = 0

    def _add_day(self, date) -> None:
        times = [False] * 60
        self.days[date] = times

    def add_sleep(self, month, day, start, stop):
        date = f"{month:02}-{day:02}"
        found_dates = [x for x in self.days.keys()]
        if date not in found_dates:
            self._add_day(date)
        self.days[date][start:stop] = [True] * (stop - start)

    def sleep_time(self):
        total_time = 0
        for times in self.days.values():
            total_time += sum(times)
        self.total_sleep_time = total_time
        return self.total_sleep_time

    def find_sleepist_minute(self):
        times = np.asarray([x for x in self.days.values()])
        # times_array = np.asarray(times)
        sleep_minute = total_min_time = 0
        for i in range(60):
            total = sum(times[:, i])
            if total > total_min_time:
                sleep_minute = i
                total_min_time = total

        self.sleepist_minute = sleep_minute
        self.sleepist_minute_total = total_min_time
        return sleep_minute


def parse_input(time_stamps):

    chrono_line = list()
    for time_stamp in time_stamps:
        entry = dict()
        date_time = datetime.strptime(time_stamp[1:17], "%Y-%m-%d %H:%M")
        entry["time"] = date_time
        action = time_stamp[19:24]
        entry["action"] = action
        if action == "Guard":
            guard_num = int(time_stamp[26:].split()[0])
            entry["id"] = guard_num

        chrono_line.append(entry)
    chrono_lines = sorted(chrono_line, key=lambda x: x["time"])

    guards = list()
    i = 0
    while i < len(chrono_lines):
        # This is always a new Guard Day by design
        found_guard_ids = [guard.id for guard in guards]
        current_id = chrono_lines[i]["id"]
        if current_id in found_guard_ids:
            current_guard = [guard for guard in guards if guard.id == current_id][0]
        else:
            new_guard = Guard(chrono_lines[i]["id"])
            guards.append(new_guard)
            current_guard = new_guard

        end_of_day = False
        i += 1
        while not end_of_day:
            current_month = chrono_lines[i]["time"].month
            current_day = chrono_lines[i]["time"].day
            start_sleep = chrono_lines[i]["time"].minute
            stop_sleep = chrono_lines[i + 1]["time"].minute

            current_guard.add_sleep(current_month, current_day, start_sleep, stop_sleep)
            i += 2
            if i >= len(chrono_lines) or chrono_lines[i]["action"] == "Guard":
                end_of_day = True

    return guards


def print_guard_pattern(guards):

    calendar = list()
    for guard in guards:
        for date, times in guard.days.items():
            x = {"day": date, "id": guard.id, "times": times}
            calendar.append(x)
    calendar = sorted(calendar, key=lambda x: x["day"])

    print("Date   ID     Minute")
    print("              000000000011111111112222222222333333333344444444445555555555")
    print("              012345678901234567890123456789012345678901234567890123456789")

    for date in calendar:
        print(f"{date['day']:>5}  #{date['id']:>4}  ", end="")
        for minute in date["times"]:
            if minute:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(guards):
    # Get the guard sleepin the most

    most_sleep_time = 0
    for guard in guards:
        sleep_time = guard.sleep_time()
        if sleep_time > most_sleep_time:
            most_sleep_time = sleep_time
            sleepy_guard = guard

    minute = sleepy_guard.find_sleepist_minute()
    print(minute * sleepy_guard.id)


def part2(guards):
    sleep_minute_total = sleep_minute = guard_id = 0

    for guard in guards:
        guard.find_sleepist_minute()
        if guard.sleepist_minute_total > sleep_minute_total:
            sleep_minute_total = guard.sleepist_minute_total
            sleep_minute = guard.sleepist_minute
            guard_id = guard.id

    print(guard_id * sleep_minute)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    data = AOC(codeDate, codeYear, test=testing)
    time_stamps = data.read_lines()
    results = parse_input(time_stamps)
    # print_guard_pattern(results)

    part1(results)
    part2(results)


if __name__ == "__main__":
    main()
