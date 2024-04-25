#!/usr/bin/python3
""" Finding Peak Function"""

def find_peak(list_of_integers):
	""" Finds the peak of a list of unsorted integers """

	# check if list is empty
	if list_of_integers is None or list_of_integers ==[]:
		return None

	def _find_peak_helper(low, high):
		if low == high:
			return list_of_integers[low]

		mid = (low + high) // 2

		# Check if mid is a peak
		if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
			return list_of_integers[mid]

		# Recurse into the half with a larger neighbor
		if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
			return _find_peak_helper(low, mid - 1)
		else:
			return _find_peak_helper(mid + 1, high)

	return _find_peak_helper(0, len(list_of_integers) - 1)

