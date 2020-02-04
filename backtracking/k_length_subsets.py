# The program below finds all k-element subsets

def find_all_subsets(mother_set, k):
    subset = [None for i in range(len(mother_set))]
    find_subsets(mother_set, subset, 0, k, 0)


def find_subsets(mother_set, subset, i, k, true_count):
    if true_count == k:
        print_subset(subset, mother_set)
    elif i == len(mother_set):
        return None
    else:
        subset[i] = True
        find_subsets(mother_set, subset[:], i+1, k, true_count+1)
        subset[i] = False
        find_subsets(mother_set, subset[:], i+1, k, true_count)


def print_subset(subset, mother_set):
    print([mother_set[i] for i in range(len(mother_set)) if subset[i]])

