def top_sort(graph: nx.DiGraph):

    white_nodes = list(graph.nodes())

    visited = set()
    stack = Stack()
    output = []
    for current in list(graph.nodes()):
        if current not in white_nodes:
            if current not in stack.nodes and current not in visited:
                print(f"node '{current} - already black'")
                continue
            else:
                print('cycle was found')
                return False

        white_nodes.remove(current)
        if set(graph.neighbors(current)).intersection(set(white_nodes)):
            stack.put(current)
            visited.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor in visited:
                return False, 'Cycle was found'
            if neighbor in white_nodes:
                stack.put(neighbor)
                white_nodes.remove(neighbor)

        while not stack.empty():
            node = stack.get()
            if set(graph.neighbors(node)).intersection(set(white_nodes)):
                stack.put(node)
                visited.add(node)
                stack
            elif set(graph.neighbors(node)).intersection(stack.nodes):
                visited.add(node)
                stack.put(node)
            if node in visited:
                print(f'return this: {node}')
                visited.remove(node)
            elif node not in stack.nodes and node not in visited:
                print(f"node '{current} - already black'")
                continue