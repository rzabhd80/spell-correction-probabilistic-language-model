class _EditDistance:
    def __int__(self):
        pass

    @classmethod
    def min_edit_distance(cls, wrong_words, correct_word):
        len_word1 = len(wrong_words)
        len_word2 = len(correct_word)

        med_table = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        for i in range(len_word1 + 1):
            med_table[i][0] = i
        for j in range(len_word2 + 1):
            med_table[0][j] = j

        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                cost = 1  # Uniform cost for all operations
                med_table[i][j] = min(
                    med_table[i - 1][j] + cost,  # Deletion
                    med_table[i][j - 1] + cost,  # Insertion
                    med_table[i - 1][j - 1] + (0 if wrong_words[i - 1] == correct_word[j - 1] else cost)  # Substitution
                )
                if i > 1 and j > 1 and wrong_words[i - 1] == correct_word[j - 2] and wrong_words[i - 2] == correct_word[
                    j - 1]:
                    med_table[i][j] = min(med_table[i][j], med_table[i - 2][j - 2] + cost)  # Transposition

        return med_table[len_word1][len_word2]
