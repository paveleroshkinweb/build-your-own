def find_hamming_distance(word1: int, word2: int):
    diff_word = word1 ^ word2
    count = 0
    while diff_word:
        count += 1
        diff_word = diff_word & (diff_word - 1)
    return count
