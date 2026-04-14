# Sentiment Analysis Introduction


This Python script provides a foundational framework for performing automated sentiment analysis on news headlines or sentences. By leveraging the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** lexicon, the program quantifies the emotional tone of text data and categorizes it into distinct sentiment labels based on varying sensitivity thresholds.


## Features


* **Automated Text Processing:** Loads and processes external CSV data using `pandas`, specifically targeting text columns for sentiment evaluation.

* **Dual-Threshold Labeling:** Implements two different scoring logic functions (`get_label_1` and `get_label_2`) to compare how "strict" or "lenient" thresholds affect sentiment classification.

* **VADER Integration:** Utilizes the `nltk` VADER intensity analyzer, which is specifically tuned for sentiments expressed in social media and short news bursts.

* **Statistical Summary:** Generates a distribution count of Positive, Negative, and Neutral labels for both threshold models to allow for quick data profiling.


## Built With


* **Python:** The core programming language used for logic and data manipulation.

* **Pandas:** Utilized for data frame management, CSV ingestion, and efficient column-wise operations.

* **NLTK (Natural Language Toolkit):** Provides the `vader_lexicon` and the `SentimentIntensityAnalyzer` engine required for linguistic analysis.

* **VADER Sentiment:** A specialized model used to calculate "compound" scores based on word intensity and context.


## Key Achievements in Code


* **Efficient Vectorization:** Uses the `.apply()` method to execute sentiment analysis across entire datasets efficiently, rather than relying on slower manual loops.

* **Dynamic Data Cleaning:** Incorporates `latin1` encoding and string conversion within the sentiment function to ensure the script can handle diverse character sets often found in news datasets.

* **Compound Score Optimization:** Successfully extracts the `compound` metric—a normalized, weighted composite score—to represent the overall sentiment polarity in a single numerical value (−1 to +1).
