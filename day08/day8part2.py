import os
from day08.day8part1 import read_input


def get_node_value(node):
    """
    Determines the value of the given Node
    """
    if not node.children:
        return sum(node.meta)

    total = 0
    for index in node.meta:
        if index > len(node.children) or index == 0:
            continue

        total += get_node_value(node.children[index - 1])

    return total


def main():
    input_file = os.path.join(os.getcwd(), "input")
    nodes = read_input(input_file)
    root = nodes[-1]

    print(get_node_value(root))


if __name__ == '__main__':
    main()
