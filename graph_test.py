import unittest
import graph_jumps


class TestMyModule(unittest.TestCase):

    def setUp(self):
        self.graph= graph_jumps.graph()
        list_of_cities = ["Malaga", "Murcia", "Madrid", "Barcelona", "Sevilla"]
        self.graph.addnodelist(list_of_cities)
        self.graph.addconnection("Malaga", "Murcia")
        self.graph.addconnection("Murcia", "Madrid")
        self.graph.addconnection("Madrid", "Barcelona")
        self.graph.addconnection("Murcia", "Sevilla")
        self.graph.addconnection("Sevilla", "Madrid")
        self.graph.addconnection("Malaga", "Barcelona")
        self.graph.addconnection("Sevilla", "Cadiz")

    def test_min_path_malaga_madrid(self):
        self.assertEqual(self.graph.min_path(self.graph.find_all_paths("Malaga", "Madrid")), (2, ['Malaga', 'Murcia', 'Madrid']))
        # It will work FINE because the min path is correct

    def test_no_path_malaga_sevilla(self):
        self.assertEqual(self.graph.min_path(self.graph.find_all_paths("Malaga", "Sevilla")), (0, []))
        # It will FAIL because there are some paths beween Malaga and Sevilla

    def test_no_path_barcelona_madrid(self):
        self.assertEqual(self.graph.find_all_paths("Barcelona", "Madrid"), [])
        # It will work FINE because there's not any path between Barcelona and Madrid

    def test_min_path_murcia_cadiz(self):
        self.assertEqual(self.graph.min_path(self.graph.find_all_paths("Murcia", "Cadiz")), (2, ["Murcia","Sevilla","Cadiz"]))
        # It will work FINE because the min path is correct

    def test_path_between_malaga_madrid(self):
        self.assertEqual(self.graph.find_all_paths("Malaga", "Madrid"), [])
        #It will FAIL because there are two paths between Malaga and Madrid

    def test_types(self):
        self.assertRaises(TypeError,self.graph.addconnection("Sevilla",5))
        #It will cause an error: TypeError, because we are trying to connect Sevilla with a number 5.

if __name__ == "__main__" :
    unittest.main()