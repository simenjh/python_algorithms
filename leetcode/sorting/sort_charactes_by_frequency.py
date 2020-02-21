# Sort a string based on character frequency

def frequency_sort(s):
    dict_char_freq = generate_freq_dict(s)
    list_char_freq = convert_char_freq_dict_to_list(dict_char_freq)
    sorted_char_freq_list = sort_by_char_freq(list_char_freq)
    sorted_string = recreate_string(sorted_char_freq_list)
    return sorted_string


def generate_freq_dict(s):
    freq_dict = {}
    for c in s:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1

            
def convert_char_freq_dict_to_list(d):
    return [[k, v] for k, v in d.items()]


def sort_by_char_freq(l):
    return sorted(l, reverse = True, key = lambda e: e[1])


def recreate_string(l):
    return "".join(c*n for c, n in l)
                
