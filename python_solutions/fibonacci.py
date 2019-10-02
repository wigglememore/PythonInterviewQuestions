# create the fibonacci sequence
sequence = [0, 1]


def fibonacci(number_of_terms):
    for i in range(2, number_of_terms):
        sequence.append(sequence[i-1] + sequence[i-2])
    iteration = range(1, number_of_terms+1)
    return(list(zip(iteration, sequence)))


print(fibonacci(10))
