# Winter's Tale Text Analysis
This is a Python project that decodes a ciphered version of *The Winter's Tale* and performs detailed textual analysis on words, lines, characters, and scenes. The play text `lgm540_play.txt` must be downloaded for the script to run.

---

## The goal

The goal is to decode a shift-ciphered text and explore the structure of Shakespeare’s play through computational analysis. This includes finding word distributions, character speech patterns, and scene structures, while keeping the analysis visual and interpretable.

---

## What it computes

Given a ciphered text file, the script performs the following computations:

### Shift cipher discovery

* **find_shift_cipher(username)**
  Finds the smallest integer `n` such that the sum of powers exceeds the username:

  ```
  total = Σ (k^-0.2) for k = 1..n
  ```

  Stops when `total > username`.

* **gcd(a, b)**
  Computes the greatest common divisor of two numbers using the Euclidean algorithm.
  This value is used as the shift cipher to decode the play.

### Text decoding

* **decode_line(line, shift)**
  Decodes a single line using the shift cipher. Punctuation is ignored, and alphabetic characters are shifted.

* **decode_text(lines, shift)**
  Decodes all lines of the play and strips extra whitespace.

### Analysis

#### Word length distribution

* Computes frequency of word lengths across the entire play.
* Plotted as a bar chart with:

  * X-axis: number of characters in a word
  * Y-axis: frequency

#### Most frequent words (over 3 letters)

* Counts words longer than three letters, ignoring character names.
* Displays top 10 words by frequency in a horizontal bar chart.

#### Line lengths

* Counts the number of words per line (excluding stage directions).
* Plotted as a line chart showing line number vs. words per line.

#### Character speech analysis

* Computes the **longest speech** for each character.
* Computes **total number of lines** per character.
* Visualizations:

  * Bar chart for top 10 longest speeches
  * Pie chart for top 10 characters by line count (others combined as “Other Characters”)

#### Scene structure

* Detects scene markers in the text.
* Computes number of lines in each scene.
* Plotted as a bar chart showing scene number vs. line count.

---

## Plot

The repository generates multiple plots to visualize the analysis:

* Word length distribution
* Top 10 most frequent words (>3 letters)
* Number of words per line
* Longest speech per character (top 10)
* Lines per character (pie chart)
* Number of lines in each scene

---

## Requirements

* Python 3.9+ (works on newer versions)
* matplotlib

Install dependencies:

```bash
pip install matplotlib
```

Download the play file `lgm540_play.txt` and place it in the same directory as the script.

---

## How to run

Run the script:

```bash
python winter_tale_analysis.py
```

Edit parameters near the top of the script to change:

* `UserName` – integer for cipher calculation
* File path of the play (`lgm540_play.txt`)
* Shift cipher can also be adjusted manually
* Whether to display plots

The script prints the shift cipher and outputs visualizations for textual analysis.

---

## Notes

* The piecewise decoding assumes a simple shift cipher derived from GCD and username.
* Determining the shift cipher could have done more simply (manually). However, I wanted to include a mathematical problem in determining the cipher. 
* Plots are intended to give insight into character involvement, word usage, and scene length for *The Winter's Tale*.

