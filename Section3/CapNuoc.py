# chúng ta biết rằng sẽ có chắc chắn từ 1 - N đỉnh hoặc đơn giản hơn là 12 đỉnh từ a tới k
# mở file để thử cho dễ

# f = open('sample_input.txt')
# lines = f.readlines()
# n,m = map(int,lines[0].split(' '))
# lines =lines[1:]


# đọc từ stdin

n, m = map(int, input().split())
lines = []
for i in range(0, m):
    lines.append(input())

# setup

edges = {x: [] for x in range(1, n + 1)}

for line in lines:
    line = line.replace('\n', '')
    vertex_original, vertex_destination = map(int, line.split(' '))
    #     print([vertex_original,vertex_destination])
    edges[vertex_destination].append(vertex_original)
    edges[vertex_original].append(vertex_destination)

# print(edges)


discover = []


def BFS(root):
    # return a cluster
    queue = []
    cluster = []
    if root in discover:
        return None
    queue.append(root)
    while queue:
        node = queue.pop()
        if node not in discover:
            if node not in cluster:
                cluster.append(node)
                discover.append(node)
            adjacents = edges[node]
            queue = queue + adjacents
    return cluster


def find_clusters(edges, vertexes):
    clusters = []
    for vertex in vertexes:
        cluster = BFS(vertex)
        if cluster is None:
            continue
        else:
            clusters.append(cluster)
    return clusters


clusters = find_clusters(edges, range(1, n + 1))
# print(clusters)
cluster_lengths = list(map(len, clusters))


def calculate(clusters, size):
    anw = 0
    if len(clusters) > 1:
        base = int(1e9 + 7)
        anw = 1
        anw2 = 1
        for _ in range(len(clusters) - 2):
            anw2 = (anw2 * size) % base
        for x in clusters:
            anw = (anw * x) % base
        anw = anw * anw2 % base
    return anw


print(len(clusters) - 1)
print(calculate(cluster_lengths, n))