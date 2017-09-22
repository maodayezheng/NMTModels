import collections


def get_frequency(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        tokens = word.split(" ")
        for i in range(len(tokens) - 1):
            pairs[tokens[i], tokens[i+1]] += freq
    return pairs


def merge(pair, v_in):
    v_out = {}
    old_token = " ".join(pair)
    new_token = "".join(pair)
    for w, freq in v_in.items():
        w_out = w.replace(old_token, new_token)
        v_out[w_out] = freq
    return v_out
