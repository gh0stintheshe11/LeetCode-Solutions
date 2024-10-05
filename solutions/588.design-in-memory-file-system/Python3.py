class FileSystem:
    
    def __init__(self):
        self.fs = {"": {}}
    
    def ls(self, path: str) -> [str]:
        components = path.split('/')
        node = self.fs['']
        for component in components:
            if component:
                node = node[component]
        
        if type(node) == str:
            return [components[-1]]
        return sorted(node.keys())
    
    def mkdir(self, path: str) -> None:
        components = path.split('/')
        node = self.fs['']
        for component in components:
            if component:
                if component not in node:
                    node[component] = {}
                node = node[component]
    
    def addContentToFile(self, filePath: str, content: str) -> None:
        components = filePath.split('/')
        node = self.fs['']
        for component in components[:-1]:
            if component:
                if component not in node:
                    node[component] = {}
                node = node[component]
        if components[-1] in node:
            node[components[-1]] += content
        else:
            node[components[-1]] = content
    
    def readContentFromFile(self, filePath: str) -> str:
        components = filePath.split('/')
        node = self.fs['']
        for component in components:
            if component:
                node = node[component]
        return node