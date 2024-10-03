from collections import deque

class Node():
    def __init__(self, name, is_mango_seller):
        self.name = name
        self.is_mango_seller = is_mango_seller

graph = { "you": [Node("bob", False), Node("claire", False), Node("alice", False)], "claire": [Node("jonny", False), Node("thom", True)], "alice": [Node("peggy", False)], "bob": [Node("peggy", False), Node("anuj", False)]}


def bfs():
    queue = deque(graph["you"])
    searched = []

    while queue:
        person = queue.popleft()
        if person.name not in searched:
            if person.is_mango_seller:
                return person.name
            elif person.name in graph:
                queue += graph[person.name]
                searched.append(person.name)
        print("Not a seller:", person.name)

print("mango seller:", bfs())

