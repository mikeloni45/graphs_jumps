class graph:

    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def addnode(self,key):
        self.nodes[key] = {}
        self.num_nodes += 1

    def addnodelist(self,nodelist):
        for item in nodelist:
            self.nodes[item]={}

    def addconnection(self,key,neighbour):
        """
        Make a connection between two nodes (vertices) of the graph
        """
        if not isinstance(key, str) or not isinstance(neighbour, str):
            #print("no vale")
            raise TypeError
        else:
            if key in self.nodes:
                if self.nodes[key]=={}:
                    self.nodes[key]=[neighbour]
                else:
                    self.nodes[key].append(neighbour)


    def connections(self,key):
        return self.nodes[key]

    def all_nodes_and_connections(self):
        print("List of all nodes and connections")
        for item in self.nodes.keys():
            print (item, self.connections(item))

    def all_nodes(self):
        print("Items of this graph")
        for item in self.nodes.keys():
            print (item, sep=" ")

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path +  [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.nodes:
            return []
        paths = []
        for vertex in self.nodes[start_vertex]:
            if vertex not in path:
                full_path = self.find_all_paths(vertex, end_vertex, path)
                for pth in full_path:
                    paths.append(pth)
        return paths


    def min_path(self,path):

        if len(path)>0:
            min_length=len(path[0])-1
            path_min=[]
            for item in path:
                if (len(item)-1)<=min_length:
                    min_length=len(item)-1
                    path_min=item.copy()
            return min_length,path_min
        else:
            return 0,[]

    def find_better_path(self,source,destination):
        stringpath = self.find_all_paths(source, destination)
        min_jumps, string_less_path = self.min_path(stringpath)
        print("List of paths: ", stringpath)
        print("Min. Jumps = %s .Path = %s " % (min_jumps, string_less_path))


if __name__=="__main__":

    g=graph()
    list_of_cities = ["Malaga", "Murcia", "Madrid", "Barcelona", "Sevilla"]
    g.addnodelist(list_of_cities)
    g.addconnection("Malaga", "Murcia")
    g.addconnection("Murcia", "Madrid")
    g.addconnection("Madrid", "Barcelona")
    g.addconnection("Murcia", "Sevilla")
    g.addconnection("Sevilla", "Madrid")
    g.addconnection("Malaga", "Barcelona")
    g.addconnection("Sevilla", "Cadiz")
