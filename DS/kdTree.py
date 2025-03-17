"""A classe KDTree implementa uma estrutura de dados de árvore K-dimensional (KD-Tree),
que é usada para particionar um espaço multidimensional. Cada nó da árvore contém
um ponto e divide o espaço de forma recursiva com base em um eixo alternado a cada
nível. A função `nearest_neighbor` é usada para encontrar o ponto mais próximo de um 
ponto de consulta em tempo eficiente."""

# zip = combina múltiplos iteráveis (como listas ou tuplas)
# self = é a instancia atual

class Node:
    def __init__(self, point, axis):
        self.point = point 
        self.axis = axis
        self.left = None
        self.right = None

class KDTree:
    def __init__(self, points):
        self.root = self.build_kdtree(points, axis=0)

    def build_kdtree(self, points, axis):
        if not points:
            return None
        
        # ordena os pontos pela coordenada do eixo atual
        points.sort(key=lambda x: x[axis])
        
        median_index = len(points) // 2 # seleciona o ponto do meio para ser a raiz
        median_point = points[median_index]

        node = Node(median_point, axis)

        # recursivamente constrói as subárvores à esquerda e à direita
        next_axis = (axis + 1) % len(points[0])  # alterna entre os eixos (0, 1, ...)
        node.left = self.build_kdtree(points[:median_index], next_axis)
        node.right = self.build_kdtree(points[median_index + 1:], next_axis)

        return node

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, point, float('inf'), None)

    def _nearest_neighbor(self, node, point, best_dist, best_node): # just a verification 
        if node is None:
            return best_node

        dist = self.distance(node.point, point)

        if dist < best_dist:
            best_dist = dist
            best_node = node

        axis = node.axis
        next_node = None
        opposite_node = None

        if point[axis] < node.point[axis]:
            next_node = node.left
            opposite_node = node.right
        else:
            next_node = node.right
            opposite_node = node.left

        best_node = self._nearest_neighbor(next_node, point, best_dist, best_node)

        if abs(point[axis] - node.point[axis]) < best_dist:
            best_node = self._nearest_neighbor(opposite_node, point, best_dist, best_node)
        
        return best_node

    def distance(self, point1, point2):
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5 

points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
kdtree = KDTree(points)

target = (9, 2)
nearest = kdtree.nearest_neighbor(target)

print(f"Ponto mais proximo de {target}: {nearest.point}")
