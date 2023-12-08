def traverse_graph(graph, instructions):
    graph_start = 'AAA'
    graph_end = 'ZZZ'

    # Traverse the graph using the instructions.
    # The instruction are only the letters "L" and "R", indicating which direction to go in the graph.
    current_vertex = graph_start
    traversed_steps = 0

    def one_traversal(current_vertex, traversed_steps):
        for instruction in instructions:
            if current_vertex == graph_end:
                break
            if instruction == 'L':
                current_vertex = graph[current_vertex][0]
                traversed_steps += 1
            elif instruction == 'R':
                current_vertex = graph[current_vertex][1]
                traversed_steps += 1

        return current_vertex, traversed_steps

    current_vertex, traversed_steps = one_traversal(current_vertex, traversed_steps)
    while current_vertex != graph_end:
        current_vertex, traversed_steps = one_traversal(current_vertex, traversed_steps)

    print(f'Reached the end of the graph in {traversed_steps} steps.')


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
