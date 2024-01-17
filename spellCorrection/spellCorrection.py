from spellCorrection.spellcorrection_core.spellCorrection import SpellCorrectionHandler
from Constants import output_spellCorrection


class SpellCorrection:
    def __init__(self):
        self.spell_correction = SpellCorrectionHandler()

    def spell_correction(self):
        probabilities = self.spell_correction.spell_correction()
        with open(output_spellCorrection, "w") as f:
            f.writelines(f.writelines(f'{i}:{probabilities[i]}\t') for i in probabilities.keys())
        print(f"output written into {output_spellCorrection}")
