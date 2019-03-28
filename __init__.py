import random
import unittest


def find_majority(array):
    if array and len(array) == 1:
        return array[0]

    division = int(len(array) / 2)
    l_array = array[:division]
    r_array = array[division:]
    elem_l = find_majority(l_array)
    elem_r = find_majority(r_array)

    elem_l_c = 0
    elem_r_c = 0

    for i in array:
        if i == elem_l:
            elem_l_c += 1
        if i == elem_r:
            elem_r_c += 1
    if elem_l_c > int(len(array) / 2):
        return elem_l
    elif elem_r_c > int(len(array) / 2):
        return elem_r
    else:
        return None


class Test(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_find_majority(self):
        array = ["a", "x", "a", "x", "a", "x", "a", "x", "a", "a", "a", "a", "a", "x", "a", "z", "a", "a", "a", "b", "b", "b",
         "b", "b", "a", "x", "a", "x", "a", "x", "a", "x", ]
        elem = find_majority(array)
        self.assertEqual("a", elem)

        array = ["a", "x", "a", "x", "a", "x", "a", "x", "a", "a", "a", "a", "a", "x", "a", "z", "a", "a", "a",
                 "b", "b", "b", "b", "b"]
        elem = find_majority(array)
        self.assertEqual("a", elem)

        array = [1, 1, 2, 2, 2]
        elem = find_majority(array)
        self.assertEqual(2, elem)

        array = [1, 2, 1, 3, 1, 4, 1, 5, 1]
        elem = find_majority(array)
        self.assertEqual(1, elem)

        array = [1, 2, 1]
        elem = find_majority(array)
        self.assertEqual(1, elem)

        array = [2, 1, 1]
        elem = find_majority(array)
        self.assertEqual(1, elem)

        for n in range(1000):
            n_elem = random.randint(3, 10000)
            r = random.random()
            extra = r if r > 0.5 else r + 0.5
            n_times_winner = int(extra * n_elem) + 1
            array = [1] * n_times_winner
            array.extend([random.randint(2, 10000) for i in range(n_elem - n_times_winner)])
            random.shuffle(array)

            elem = find_majority(array)
            self.assertEqual(1, elem)

        for n in range(1000):
            n_elem = random.randint(3, 10000)
            array = [random.randint(2, 10000) for i in range(n_elem)]

            elem = find_majority(array)
            self.assertEqual(None, elem)

        for n in range(1000):
            n_elem = random.randint(3, 100)
            r = random.random()
            extra = r if r > 0.5 else r + 0.5
            n_times_winner = int(extra * n_elem) + 1
            array = [1] * n_times_winner
            array.extend([random.randint(2, 4) for i in range(n_elem - n_times_winner)])
            random.shuffle(array)

            elem = find_majority(array)
            self.assertEqual(1, elem)

