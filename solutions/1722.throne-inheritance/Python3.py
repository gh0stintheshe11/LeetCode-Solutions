class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> [str]:
        order = []

        def dfs(person):
            if person not in self.dead:
                order.append(person)
            for child in self.children[person]:
                dfs(child)

        dfs(self.king)
        return order