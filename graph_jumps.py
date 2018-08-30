class graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def addnode(self,key):
        self.nodes[key] = {}
        self.num_nodes += 1

    def addconnection(self,key,neighbour):

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

    def find_all_partialpaths(self, start_vertex, end_vertex, partialpath=[]):
        partialpath = partialpath +  [start_vertex]
        if start_vertex == end_vertex:
            return [partialpath]
        if start_vertex not in self.nodes:
            return []
        fullpath = []
        for vertex in self.nodes[start_vertex]:
            if vertex not in partialpath:
                fullpath = self.find_all_partialpaths(vertex, end_vertex, partialpath)
                for pth in fullpath:
                    fullpath.append(pth)
        return fullpath

    def min_partialpath(self,partialpath):
        if len(partialpath)>0:
            min_length=len(partialpath[0])-1
            partialpath_min=[]
            for item in partialpath:
                if (len(item)-1)<=min_length:
                    min_length=len(item)-1
                    partialpath_min=item.copy()
            return min_length,partialpath_min
        else:
            return 0,"No partialpath"

    def find_better_partialpath(self,source,destination):
        stringpartialpath = self.find_all_partialpaths(source, destination)
        min_jumps, string_less_partialpath = self.min_partialpath(stringpartialpath)
        print("List of partial paths: ", stringpartialpath)
        print("Min. Jumps = %s .better path = %s " % (min_jumps, string_less_partialpath))

g = graph()
g.addnode("Malaga")
g.addnode("Murcia")
g.addnode("Madrid")
g.addnode("Barcelona")
g.addnode("Sevilla")
g.addconnection("Malaga","Murcia")
g.addconnection("Murcia","Madrid")
g.addconnection("Madrid","Barcelona")
g.addconnection("Murcia","Sevilla")
g.addconnection("Sevilla","Madrid")
g.addconnection("Malaga","Barcelona")
g.addconnection("Sevilla","Barcelona")
g.all_nodes()
print("-"*60)
g.all_nodes_and_connections()
g.find_better_partialpath("Murcia","Madrid")

