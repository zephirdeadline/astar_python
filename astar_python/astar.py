class Astar:

    def __init__(self, matrix):
        self.mat = self.prepare_matrix(matrix)

    class Node:
        def __init__(self, x, y, weight=0):
            self.x = x
            self.y = y
            self.weight = weight
            self.heuristic = 0
            self.parent = None

        def __repr__(self):
            return str(self.weight)

    def print(self):
        for y in self.mat:
            print(y)

    def prepare_matrix(self, mat):
        matrix_for_astar = []
        for y, line in enumerate(mat):
            tmp_line = []
            for x, weight in enumerate(line):
                tmp_line.append(self.Node(x, y, weight=weight))
            matrix_for_astar.append(tmp_line)
        return matrix_for_astar

    def equal(self, current, end):
        return current.x == end.x and current.y == end.y

    def heuristic(self, current, other):
        return abs(current.x - other.x) + abs(current.y - other.y)

    def neighbours(self, matrix, current):
        neighbours_list = []
        if current.x - 1 >= 0 and current.y - 1 >= 0 and matrix[current.y - 1][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x - 1])
        if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x - 1])
        if current.x - 1 >= 0 and current.y + 1 < len(matrix) and matrix[current.y + 1][
            current.x - 1].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x - 1])
        if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x])
        if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x])
        if current.x + 1 < len(matrix[0]) and current.y - 1 >= 0 and matrix[current.y - 1][
            current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y - 1][current.x + 1])
        if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y][current.x + 1])
        if current.x + 1 < len(matrix[0]) and current.y + 1 < len(matrix) and matrix[current.y + 1][
            current.x + 1].weight is not None:
            neighbours_list.append(matrix[current.y + 1][current.x + 1])
        return neighbours_list

    def build(self, end):
        node_tmp = end
        path = []
        while (node_tmp):
            path.append([node_tmp.x, node_tmp.y])
            node_tmp = node_tmp.parent
        return list(reversed(path))

    def run(self, point_start, point_end):
        matrix = self.mat
        start = self.Node(point_start[0], point_start[1])
        end = self.Node(point_end[0], point_end[1])
        closed_list = []
        open_list = [start]

        while open_list:
            current_node = open_list.pop()

            for node in open_list:
                if node.heuristic < current_node.heuristic:
                    current_node = node

            if self.equal(current_node, end):
                return self.build(current_node)

            for node in open_list:
                if self.equal(current_node, node):
                    open_list.remove(node)
                    break

            closed_list.append(current_node)

            for neighbour in self.neighbours(matrix, current_node):
                if neighbour in closed_list:
                    continue
                if neighbour.heuristic < current_node.heuristic or neighbour not in open_list:
                    neighbour.heuristic = neighbour.weight + self.heuristic(neighbour, end)
                    neighbour.parent = current_node
                if neighbour not in open_list:
                    open_list.append(neighbour)

        return None

