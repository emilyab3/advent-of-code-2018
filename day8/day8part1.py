import os


class Node:
    def __init__(self):
        self.meta = []
        self.children = []


def read_input(filename: str):
    nodes = []
    with open(filename, 'r') as file:
        for line in file:
            nums = [int(x) for x in line.strip().split(" ")]
            nodes, length, node = process(nums)

    return nodes


def process(line, existing_length=0):
    nodes = []
    length = existing_length
    # while line:
    node = Node()

    num_children = line[length]
    num_meta = line[length + 1]
    length += 2

    # line = line[2:]

    for child in range(num_children):
        child_nodes, child_length, child_node = process(line, length)
        node.children.append(child_node)
        length = child_length
        nodes.extend(child_nodes)

    meta = line[length:length + num_meta]
    node.meta = meta
    length += num_meta

    # line = line[2:length]

    nodes.append(node)

    return nodes, length, node


def get_node_value(node):
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

    total_meta = 0
    for node in nodes:
        total_meta += sum(node.meta)

    print(total_meta)
    print(get_node_value(root))


if __name__ == '__main__':
    main()
