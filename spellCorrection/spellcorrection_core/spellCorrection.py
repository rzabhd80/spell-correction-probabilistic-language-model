import enchant
from spellCorrection.spellcorrection_core.EditDistance import _EditDistance
from spellCorrection.spellcorrection_core.noisyChannel import NoisyChannel


class SpellCorrectionHandler:
    def __int__(self):
        self.noisy_channel = NoisyChannel()
        self.datasets_instance = self.noisy_channel.datasets_instance
        self.edit_distance_calculator = _EditDistance().min_edit_distance
        self.candidate_words = None

    def language_model(self, given_word: str, dataset):
        count = 0
        for word in dataset:
            if given_word == word:
                count += 1
        return count / len(dataset)

    def spell_correction(self):
        candidates = {}
        d = enchant.Dict("en_US")
        for word in self.datasets_instance.spell_test_set:
            suggestions = d.suggest(word)
            filtered_candidates = [candid.lower() for candid in suggestions if
                                   not any(punctuation in candid for punctuation in [' ', '-', "'"])]
            candidates[word] = filtered_candidates
        probs = {key: max(
            (value for value in values if self.edit_distance_calculator(key, value)[0] <= 1),
            key=lambda value: self.noisy_channel.noisy_channel_model(key, value) * self.language_model(value,
                                                                                                       self.datasets_instance) * (
                                          0 ** 9), default='') for key, values in candidates.items()}

        return probs
