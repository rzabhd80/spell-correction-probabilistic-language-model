class _EditDistance:
    def __int__(self):
        pass

    @classmethod
    def min_edit_distance(cls, word1, word2):
        len_word1 = len(word1)
        len_word2 = len(word2)

        dp = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]
        operations = [[""] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        for i in range(len_word1 + 1):
            dp[i][0] = i
            operations[i][0] = 'D'
        for j in range(len_word2 + 1):
            dp[0][j] = j
            operations[0][j] = 'I'

        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                cost = 1
                dp[i][j] = min(
                    dp[i - 1][j] + cost,  # Deletion
                    dp[i][j - 1] + cost,  # Insertion
                    dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else cost)  # Substitution
                )
                if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost)

                # print(i,j,dp[i][j])
                if dp[i][j] == dp[i - 1][j] + cost:
                    operations[i][j] = "D"  # Deletion
                elif dp[i][j] == dp[i][j - 1] + cost:
                    operations[i][j] = "I"  # Insertion
                elif dp[i][j] == dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else cost):
                    operations[i][j] = "S" if word1[i - 1] != word2[j - 1] else ""  # Substitution

                if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost)
                    if dp[i][j] == dp[i - 2][j - 2] + cost:
                        operations[i][j] = "T"
        i, j = len_word1, len_word2
        distance = dp[i][j]
        if distance > 1:
            return [2, '']
        changes = {}

        while i > 0 or j > 0:
            operation = operations[i][j]

            if operation == "D":
                if i != 1:
                    changes["insert"] = f'{word1[i - 2]}|{word1[i - 1]}'
                else:
                    changes["insert"] = f'{word1[i]}|{word1[i - 1]}'
                i -= 1
            elif operation == "I":
                if j != 1:
                    changes["delete"] = f'{word2[j - 2]}|{word2[j - 1]}'
                else:


                    changes["delete"] = f'{word2[j]}|{word2[j - 1]}'

                j -= 1
            elif operation == "S":
                changes["sub"] = f'{word1[i - 1]}|{word2[i - 1]}'
                i -= 1
                j -= 1
            elif operation == "T":
                changes["trans"] = f'{word1[i - 2:i]}'
                i -= 2
                j -= 2
            else:
                i -= 1
                j -= 1

        return [distance, changes]
