from difflib import SequenceMatcher
from sklearn.metrics import precision_score, recall_score, f1_score


def calculate_metrics(original, corrected):
    original_words = original.split()
    corrected_words = corrected.split()

    matches = sum(1 for o, c in zip(original_words, corrected_words) if o == c)
    accuracy = matches / len(original_words)

    precision = precision_score(original_words, corrected_words, average='weighted', zero_division=0)
    recall = recall_score(original_words, corrected_words, average='weighted', zero_division=0)
    f1 = f1_score(original_words, corrected_words, average='weighted', zero_division=0)

    edit_distance = SequenceMatcher(None, original, corrected).ratio()

    return accuracy, precision, recall, f1, edit_distance

def evaluate_all_metrics():
    with open("data/raw/original.txt", "r") as f:
        original_text = f.read()
    with open("results/textblob_correction.txt", "r") as f:
        corrected_text_textblob = f.read()
    with open("results/symspell_correction.txt", "r") as f:
        corrected_text_symspell = f.read()

    results = {
        "TextBlob": calculate_metrics(original_text, corrected_text_textblob),
        "SymSpell": calculate_metrics(original_text, corrected_text_symspell),
    }

    for method, (accuracy, precision, recall, f1, edit_distance) in results.items():
        print(f"{method} - Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}, Edit Distance: {edit_distance:.2f}")


if __name__ == "__main__":
    evaluate_all_metrics()
