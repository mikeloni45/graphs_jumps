class graph:

    def __init__(self):
        self.cities = {}

    def addcity(self,key):
        if key not in self.cities:
            self.cities[key] = []

    def add_citylist(self,cities_list):
        for item in cities_list:
            self.cities[item]=[]

    def addconnection(self,city_from,city_to):

        if not isinstance(city_from, str) or not isinstance(city_to, str):
            raise TypeError
        else:
            if city_from not in self.cities:
                raise NameError("Source City not present")
            else:
                if city_to not in self.cities:
                    raise NameError("Destination City not present")
                else:
                    if city_to not in self.cities[city_from]:
                        self.cities[city_from].append(city_to)


    def all_cities_and_connections(self):
        print("List of all cities and connections")
        for item in self.cities.keys():
            print (item, self.cities[item])

    def all_cities(self):
        print("Items of this graph")
        for item in self.cities.keys():
            print (item, sep=" ")

    def find_all_paths(self, start_city, end_city, current_path=[]):
        current_path = current_path +  [start_city]
        if start_city not in self.cities:
            return []
        if start_city == end_city:
            return [current_path]
        allpaths = []
        for city in self.cities[start_city]:
            if city not in current_path:
                full_path = self.find_all_paths(city, end_city, current_path)
                for pth in full_path:
                    allpaths.append(pth)
        return allpaths


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

    def find_better_path(self,city_source,city_destination):
        stringpath = self.find_all_paths(city_source, city_destination)
        min_jumps, string_less_path = self.min_path(stringpath)
        print("List of paths: ", stringpath)
        print("Min. Jumps = %s .Path = %s " % (min_jumps, string_less_path))


if __name__=="__main__":

    g=graph()
    list_of_cities = ["Malaga", "Murcia", "Madrid", "Barcelona", "Sevilla","Cadiz"]
    g.add_citylist(list_of_cities)
    g.addconnection("Malaga", "Murcia")
    g.addconnection("Murcia", "Madrid")
    g.addconnection("Madrid", "Barcelona")
    g.addconnection("Murcia", "Sevilla")
    g.addconnection("Sevilla", "Madrid")
    g.addconnection("Malaga", "Barcelona")
    g.addconnection("Sevilla", "Cadiz")
    g.addconnection("Sevilla", "Cadiz")
    g.all_cities_and_connections()
    g.find_better_path("Murcia","Madrid")
