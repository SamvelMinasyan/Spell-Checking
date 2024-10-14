from textblob import TextBlob
from symspellpy import SymSpell, Verbosity
import os
import openai


def initialize_symspell():
    sym_spell = SymSpell(max_dictionary_edit_distance=2)
    sym_spell.load_dictionary("frequency_dictionary_en_82_765.txt", 0, 1)
    return sym_spell


def textblob_correct(text):
    blob = TextBlob(text)
    return str(blob.correct())


def symspell_correct(text, sym_spell):
    corrected_text = []
    for word in text.split():
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        corrected_word = suggestions[0].term if suggestions else word
        corrected_text.append(corrected_word)
    return " ".join(corrected_text)


def evaluate_spell_checkers():
    with open("data/raw/synthetic.txt", "r") as f:
        test_data = f.read()

    sym_spell = initialize_symspell()

    corrected_text_textblob = textblob_correct(test_data)
    corrected_text_symspell = symspell_correct(test_data, sym_spell)

    os.makedirs("results", exist_ok=True)
    with open("results/textblob_correction.txt", "w") as f:
        f.write(corrected_text_textblob)
    with open("results/symspell_correction.txt", "w") as f:
        f.write(corrected_text_symspell)

    print("Evaluation completed and results saved in the results directory.")


if __name__ == "__main__":
    evaluate_spell_checkers()
