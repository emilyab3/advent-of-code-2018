import os


class Node:
    """
    Represents a Node with children and metadata
    """
    def __init__(self):
        self.meta = []
        self.children = []


def read_input(filename: str):
    """
    Reads input from the given file and returns a list of the Nodes contained therein
    """
    nodes = []
    with open(filename, 'r') as file:
        for line in file:
            nums = [int(x) for x in line.strip().split(" ")]
            nodes, _, _ = process(nums)

    return nodes


def process(line, existing_length=0):
    """
    Processes the given line, recursively finding any other nodes contained therein
    """
    nodes = []
    length = existing_length
    node = Node()

    num_children = line[length]
    num_meta = line[length + 1]
    length += 2

    # recursively processes any children Nodes
    for child in range(num_children):
        child_nodes, child_length, child_node = process(line, length)
        node.children.append(child_node)
        length = child_length
        nodes.extend(child_nodes)

    meta = line[length:length + num_meta]
    node.meta = meta
    length += num_meta

    nodes.append(node)

    return nodes, length, node


def main():
    input_file = os.path.join(os.getcwd(), "input")
    nodes = read_input(input_file)

    total_meta = 0
    for node in nodes:
        total_meta += sum(node.meta)

    print(total_meta)


if __name__ == '__main__':
    main()
