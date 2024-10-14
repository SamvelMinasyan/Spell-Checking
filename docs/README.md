# Spell Checker Evaluation

## Project Overview
This project evaluates the performance of spell-checking tools: **TextBlob**, **SymSpell**. Each tool is tested on a dataset containing synthetic spelling errors, and metrics such as accuracy, precision, recall, F1 score, and edit distance are used to compare their effectiveness.

## Requirements
Before running the project, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```
### Then run the scripts in following order 
```bash
python data/data_preparation.py

python tools/evaluation.py

python tools/metrics.py
```