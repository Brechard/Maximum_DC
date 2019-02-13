import random
import unittest


def find_maximum(array):
	if array and len(array) == 1:
		return array[0], 1

	division = int(len(array) / 2)
	l_array = array[:division]
	r_array = array[division:]
	elem_l, times_l = find_maximum(l_array)
	elem_r, times_r = find_maximum(r_array)

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


class Test(unittest.TestCase):
	def setUp(self):
		super().setUp()

	def test_find_maximum(self):
		for n in range(1000):
			n_elem = random.randint(3, 10000)
			r = random.random()
			extra = r if r > 0.5 else r + 0.5
			n_times_winner = int(extra * n_elem)
			array = [1] * n_times_winner
			array.extend([random.randint(2, 10000) for i in range(n_elem - n_times_winner)])
			random.shuffle(array)

			elem, times = find_maximum(array)
			self.assertEqual(elem, 1)
