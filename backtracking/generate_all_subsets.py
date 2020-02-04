def find_all_subsets(mother_set):
    subset = [None for i in range(len(mother_set))]
    find_subsets(mother_set, subset, 0)


def find_subsets(mother_set, subset, i):
    if i == len(mother_set):
        print_subset(subset, mother_set)
    else:
        subset[i] = True
        find_subsets(mother_set, subset[:], i+1)
        subset[i] = False
        find_subsets(mother_set, subset[:], i+1)


def print_subset(subset, mother_set):
    print([mother_set[i] for i in range(len(mother_set)) if subset[i]])

