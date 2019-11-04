import unittest

from py_ai_sdk.core.disjoint_set import DisjointSet

class DisjointSetTest(unittest.TestCase):
    def test_element(self):
        element1 = DisjointSet.Element(3)
        self.assertEqual(element1.parent, element1)
        self.assertEqual(element1.id_, 3)
        self.assertEqual(element1.size, 1)
        self.assertEqual(element1.rank, 0)
        self.assertEqual("Rank: 0, Id: 3, Size: 1", str(element1))
        self.assertEqual("Rank: 0, Id: 3, Size: 1", repr(element1))
        element2 = DisjointSet.Element("element")
        self.assertEqual("Rank: 0, Id: element, Size: 1", str(element2))

    def test_disjoint_set_logic(self):
        disjoint_set = DisjointSet()
        for id_ in range(4):
            disjoint_set.make_set(DisjointSet.Element(id_))
        self.assertEqual(len(disjoint_set.set), 4)
        disjoint_set.union(0, 1)
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 0, Id: 2, Size: 1", str(disjoint_set.get_element(2)))
        self.assertEqual("Rank: 0, Id: 3, Size: 1", str(disjoint_set.get_element(3)))
        disjoint_set.union(2, 3)
        disjoint_set.union(3, 2) # Ineffective
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 1, Id: 2, Size: 2", str(disjoint_set.get_element(2)))
        self.assertEqual("Rank: 0, Id: 3, Size: 1", str(disjoint_set.get_element(3)))
        disjoint_set.union(3, 1)
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 2, Id: 2, Size: 4", str(disjoint_set.get_element(2)))
        self.assertEqual("Rank: 0, Id: 3, Size: 1", str(disjoint_set.get_element(3)))
        disjoint_set.union(0, 2) # Ineffective
        disjoint_set.union(1, 2) # Ineffective
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 2, Id: 2, Size: 4", str(disjoint_set.get_element(2)))
        self.assertEqual("Rank: 0, Id: 3, Size: 1", str(disjoint_set.get_element(3)))

    def test_disjoint_set_already_or_never_exists(self):
        disjoint_set = DisjointSet()
        for id_ in range(4):
            disjoint_set.make_set(DisjointSet.Element(id_))
        does_not_exist_element = DisjointSet.Element("unknown")
        self.assertIsNone(disjoint_set.get_element(does_not_exist_element.id_))
        disjoint_set.union(0, does_not_exist_element.id_)
        already_added_element = DisjointSet.Element(0)
        disjoint_set.make_set(already_added_element)
        self.assertEqual(len(disjoint_set.set), 4)

    def test_disjoint_set_rank_comparison(self):
        disjoint_set = DisjointSet()
        for id_ in range(3):
            disjoint_set.make_set(DisjointSet.Element(id_))
        disjoint_set.union(0, 1)
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 0, Id: 2, Size: 1", str(disjoint_set.get_element(2)))
        disjoint_set.union(0, 2)
        self.assertEqual("Rank: 1, Id: 0, Size: 3", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 0, Id: 2, Size: 1", str(disjoint_set.get_element(2)))
        disjoint_set = DisjointSet()
        for id_ in range(3):
            disjoint_set.make_set(DisjointSet.Element(id_))
        disjoint_set.union(0, 1)
        self.assertEqual("Rank: 1, Id: 0, Size: 2", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 0, Id: 2, Size: 1", str(disjoint_set.get_element(2)))
        disjoint_set.union(2, 0)
        self.assertEqual("Rank: 1, Id: 0, Size: 3", str(disjoint_set.get_element(0)))
        self.assertEqual("Rank: 0, Id: 1, Size: 1", str(disjoint_set.get_element(1)))
        self.assertEqual("Rank: 0, Id: 2, Size: 1", str(disjoint_set.get_element(2)))

if __name__ == "__main__":
    unittest.main()
