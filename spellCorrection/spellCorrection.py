from spellCorrection.spellcorrection_core.spellCorrection import SpellCorrectionHandler
from Constants import output_spellCorrection


class SpellCorrection:
    def __init__(self):
        self.spell_correction = SpellCorrectionHandler()

    def spell_correction(self):
        probabilities = self.spell_correction.spell_correction()
        with open(output_spellCorrection) as f:
            f.writelines(probabilities)
        print(f"output written into {output_spellCorrection}")
