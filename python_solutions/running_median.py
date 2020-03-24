"""
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
"""
sequence = [2, 1, 5, 7, 2, 0, 5]


def running_mean(sequence_list):
	median_store = []
	for index, value in enumerate(sequence_list):
		current_seq_ordered = sequence_list[:index+1]
		current_seq_ordered.sort()
		if len(current_seq_ordered) == 1:
			current_median = value
		elif len(current_seq_ordered) % 2 == 0:
			half_down = round(len(current_seq_ordered)/2 - 1)
			half_up = round(len(current_seq_ordered)/2)
			current_median = (current_seq_ordered[half_down] + current_seq_ordered[half_up])/2
		else:
			current_median = current_seq_ordered[round(len(current_seq_ordered)/2) - 1]
		median_store.append(current_median)
	return median_store


print(running_mean(sequence))
