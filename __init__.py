import random
import unittest


def find_maximum_helper(array):
	if array and len(array) == 1:
		return array[0], 1

	division = int(len(array) / 2)
	l_array = array[:division]
	r_array = array[division:]
	elem_l, times_l = find_maximum_helper(l_array)
	elem_r, times_r = find_maximum_helper(r_array)

	if not elem_l:
		if not elem_r:
			return None, None
		else:
			return elem_r, times_r
	elif not elem_r:
		return elem_l, times_l
	else:
		if times_l == times_r:
			if elem_l == elem_r:
				return elem_l, times_l + times_r
			else:
				return None, None
		elif times_l > times_r:
			return elem_l, times_l
		else:
			return elem_r, times_r


def find_majority(array):
	if not array or len(array) <= 2:
		return None

	n_array = len(array)
	if n_array % 2 != 0 and n_array > 4:
		pseudo_half = int(n_array / 2)
		if array[pseudo_half] == array[pseudo_half + 1]:
			swapper = array[pseudo_half - 1]
			array[pseudo_half - 1] = array[pseudo_half + 1]
			array[pseudo_half + 1] = swapper
		elif array[pseudo_half] == array[pseudo_half - 1]:
			swapper = array[pseudo_half]
			array[pseudo_half] = array[pseudo_half + 1]
			array[pseudo_half + 1] = swapper

	elem, times = find_maximum_helper(array)
	if elem and len([0 for i in array if i == elem]) >= len(array) / 2:
		return elem
	else:
		return None


class Test(unittest.TestCase):
	def setUp(self):
		super().setUp()

	def test_find_majority(self):
		array = [1, 1, 1, 2, 2]
		elem = find_majority(array)
		self.assertEqual(1, elem)

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
