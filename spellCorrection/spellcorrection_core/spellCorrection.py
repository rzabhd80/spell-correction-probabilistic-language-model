from spellCorrection.spellcorrection_core.EditDistance import _EditDistance
from spellCorrection.spellcorrection_core.noisyChannel import NoisyChannel
import enchant


class SpellCorrectionHandler:
    def __init__(self):
        self.noisy_channel = NoisyChannel()
        self.datasets_instance = self.noisy_channel.datasets_instance
        self.edit_distance_calculator = _EditDistance().min_edit_distance
        self.candidate_words = None

    def preprocess_matrix(self, matrix):
        return matrix.replace("'", '"')

    def filter_candidates(self, word, suggestions, punctuation):
        return [candid.lower() for candid in suggestions if not any(p in candid for p in punctuation)]

    def language_model(self, given_word: str):
        count = 0
        for word in self.datasets_instance.spell_channel_dataset:
            if given_word == word:
                count += 1
        return count / len(self.datasets_instance.spell_channel_dataset)

    def calculate_probability(self, key, values):
        return {
            key: max((value for value in values if self.edit_distance_calculator(key, value)[0] <= 1),
                     key=lambda value: self.noisy_channel.channel_model(
                         self.edit_distance_calculator(key, value)[1]) * self.language_model(value) * (10 ** 9),
                     default=None)
        }

    def spell_correction(self):
        candidates = {}
        d = enchant.Dict("en_US")
        for word in self.datasets_instance.spell_test_set:
            suggestions = d.suggest(word)
            filtered_candidates = self.filter_candidates(word, suggestions, [' ', "'", '-'])
            candidates[word] = filtered_candidates
        probs = {key: self.calculate_probability(key, values)
                 for key, values in candidates.items()}

        return probs
