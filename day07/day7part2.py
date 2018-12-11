from day07.day7part1 import *


OFFSET = 64


def get_next_topo_options(steps):
    """
    Returns the next steps available to be completed in topological order
    """
    return sorted(get_starters(steps))


def get_step_time(step):
    """
    Returns the time required to complete the given step
    """
    return TIME + ord(step) - OFFSET


def main():
    input_file = os.path.join(os.getcwd(), "input")
    steps = read_input(input_file)

    workers = [False for _ in range(WORKERS)]
    tasks = ["" for _ in range(WORKERS)]
    schedule = {}

    topo = []

    current_time = 0
    while steps:
        for i in range(WORKERS):
            if current_time in schedule and i not in schedule[current_time]:
                workers[i] = False
                remove_mappings(tasks[i], steps)
            elif current_time not in schedule:
                workers[i] = False
                if tasks[i] != "":
                    remove_mappings(tasks[i], steps)

        next_steps = get_next_topo_options(steps)
        if not next_steps or False not in workers:
            current_time += 1
            continue

        for next_step in next_steps:
            step_time = get_step_time(next_step)
            if False not in workers:
                continue

            worker = workers.index(False)
            workers[worker] = True
            tasks[worker] = next_step
            for sec in range(current_time, current_time + step_time):
                if sec not in schedule:
                    schedule[sec] = []
                schedule[sec].append(worker)

            steps.pop(next_step)
            topo.append(next_step)

        current_time += 1

    print("Total time taken is {}".format(len(schedule)))


if __name__ == '__main__':
    main()
