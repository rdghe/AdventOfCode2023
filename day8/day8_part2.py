import math


def traverse_graph(graph, instructions):
    graph_start = [key for key in graph.keys() if key[-1] == 'A']
    print(f'Starting at {graph_start}')
    graph_end = [key for key in graph.keys() if key[-1] == 'Z']
    print(f'Ending at {graph_end}')

    # Traverse the graph using the instructions.
    # The instruction are only the letters "L" and "R", indicating which direction to go in the graph.
    traversed_steps = 0
    answers = []

    def one_traversal(current_vertex, traversed_steps):
        for instruction in instructions:
            if current_vertex in graph_end:
                break
            if instruction == 'L':
                current_vertex = graph[current_vertex][0]
                traversed_steps += 1
            elif instruction == 'R':
                current_vertex = graph[current_vertex][1]
                traversed_steps += 1

        return current_vertex, traversed_steps

    for current_vertex in graph_start:
        print(f'Starting at {current_vertex}')
        current_vertex, traversed_steps = one_traversal(current_vertex, traversed_steps)
        while current_vertex not in graph_end:
            current_vertex, traversed_steps = one_traversal(current_vertex, traversed_steps)
        print(f'Reached the end of the graph in {traversed_steps} steps.')
        answers.append(traversed_steps)
        traversed_steps = 0

    print(f'Answers: {answers}')
    print(f'LCM: {math.lcm(*answers)}')


def main():
    with open('input.txt', 'r') as f:
        # Read the file line by line
        data = f.readlines()

    instructions = data[0].strip()

    graph = {}

    for line in data[2:]:
        vertex, connections = [v.strip() for v in line.split('=', 1)]
        connections = [c.strip() for c in connections[1:-1].split(',')]
        graph[vertex] = connections

    print(graph)

    traverse_graph(graph, instructions)


if __name__ == '__main__':
    main()
