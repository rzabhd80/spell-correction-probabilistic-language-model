from spellCorrection.spellcorrection_core.spellCorrectionDataExctractor import SpellCorrectionDataExtractor


class NoisyChannel:
    def __int__(self):
        self.datasets_instance = SpellCorrectionDataExtractor.extractData()
        self.confusion_matrices = self.datasets_instance.confusion_matrix

    def __num_different_letters_dp(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (26) for _ in range(2)]
        for i in range(len1):
            dp[0][ord(word1[i]) - ord('a')] += 1
        different_letters = 0
        for i in range(len2):
            index = ord(word2[i]) - ord('a')
            if dp[0][index] == 0:
                different_letters += 1
            else:
                dp[0][index] -= 1
            dp[0], dp[1] = dp[1], dp[0]
        different_letters += sum(dp[0])
        return different_letters

    def __calculate_confusion_for_sub_transpose(self, wrong_word, correct_word):
        return self.confusion_matrices["sub"][f'{wrong_word}{correct_word}'] if self.__num_different_letters_dp(
            wrong_word, correct_word) == 1 else self.confusion_matrices["Transposition"][f'{wrong_word}{correct_word}']

    def __calculate_confusion_for_insertion_deletion(self, wrong_word: str, correct_word: str):
        return self.confusion_matrices['ins'][f'{wrong_word}{correct_word}'] if len(wrong_word) > len(correct_word) else \
            self.confusion_matrices['del'][f'{wrong_word}{correct_word}']

    def noisy_channel_model(self, wrong_word: str, correct_word: str):
        confusion_value = self.__calculate_confusion_for_sub_transpose(wrong_word, correct_word) if len(
            wrong_word) == len(
            correct_word) else self.__calculate_confusion_for_insertion_deletion(wrong_word, correct_word)
        count = 1
        for word in self.datasets_instance.spell_channel_dataset:
            count += word.count(f'{wrong_word}{correct_word}')

        return confusion_value / count
