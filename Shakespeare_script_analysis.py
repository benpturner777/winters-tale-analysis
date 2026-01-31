import matplotlib.pyplot as plt
from collections import Counter

# ==========================
# PART 1 - FINDING CIPHER
# ==========================
def find_shift_cipher(username: int) -> int:
    """Finds the smallest n such that sum(n^-0.2) exceeds username."""
    n, total = 1, 1 ** -0.2
    while total <= username:
        n += 1
        total += n ** -0.2
    return n

def gcd(a: int, b: int) -> int:
    """Compute greatest common divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

UserName = 540
n_value = find_shift_cipher(UserName)
print(f"Our value for the shift cipher is {n_value}")

shift_cipher = gcd(1973, 540)
print(f"The greatest common divisor of 1973 & 540 is {shift_cipher}, used as the shift cipher.")

# ==========================
# PART 2 - DECODING PLAY
# ==========================
def decode_line(line: str, shift: int = 1) -> str:
    """Decodes a single line using a shift cipher."""
    decoded = ''
    punctuation = set(".,'\":;?!&/()[]{} -")
    for char in line:
        if char not in punctuation:
            ascii_val = ord(char) - shift
            char = 'Z' if ascii_val == ord('@') else chr(ascii_val)
        decoded += char
    return decoded

def decode_text(lines: list[str], shift: int = 1) -> list[str]:
    """Decodes a list of lines and strips whitespace."""
    return [decode_line(line, shift).strip() for line in lines]

# Read and decode text
file_path = 'lgm540_play.txt'
with open(file_path) as f:
    full_text = f.readlines()
decoded_lines = decode_text(full_text)

# ==========================
# PART 3 - ANALYSIS
# ==========================
Characters = [
    "POLIXENES:", "CAMILLO:", "AUTOLYCUS:", "ARCHIDAMUS:", "Clown:", "FLORIZEL:", "PERDITA:", 
    "king:", "Shepherd:", "DORCAS:", "MOPSA:", "Servant:", "herdsman:","himself:", "MAMILLIUS:", 
    "DION:", "PAULINA:", "CLEOMENES:", "LEONTES:", "Gentleman:", "Lord:", "First Lady:", 
    "Second Lady:", "First Lord:", "Second Lord:", "LEONTES", "ANTIGONUS:", "Gaoler:", 
    "First Gentleman:", "Third Gentleman:", "Second Gentleman:", "EMILIA:", "First gentleman:", 
    "Lords:", "First Servant:", "Officer:", "Second Servant:", "HERMIONE:", "Mariner:", "Time:", 
    "Shepard:"
]

# --------- 3i(a) Word length distribution ---------
words = [w for w in open(file_path).read().split() if w]
word_lengths = [len(w) for w in words]
length_counts = Counter(word_lengths)
lengths, values = zip(*sorted(length_counts.items()))

plt.bar(lengths, values, width=0.6, color='aqua', edgecolor='black')
plt.xlabel("Number of characters")
plt.ylabel("Frequency of words")
plt.title("Distribution of word lengths in The Winter's Tale")
plt.show()

# --------- 3i(b) Most frequent words over 3 letters ---------
words_counter = Counter()
for line in decoded_lines:
    if line and line[0] not in "[({":
        for w in line.replace(':', ' ').split():
            if len(w) > 3 and w not in Characters:
                words_counter[w] += 1

top_words = words_counter.most_common(10)
words_labels, words_freqs = zip(*top_words)

fig, ax = plt.subplots(figsize=(6, 4))
ax.barh(range(10, 0, -1), words_freqs, color='crimson', edgecolor='black')
ax.set_yticks(range(10, 0, -1))
ax.set_yticklabels(words_labels)
ax.set_xlabel('Frequency')
ax.set_ylabel('Words')
ax.set_title('Top ten words with over 3 characters')
plt.show()

# --------- 3ii Line lengths ---------
line_lengths = [
    len(line.replace(':', ' ').split()) - 1
    for line in decoded_lines
    if line and line[0] not in "[({"
]

plt.figure()
plt.plot(range(1, len(line_lengths) + 1), line_lengths, ls='-', c='purple')
plt.xlabel('Line number')
plt.ylabel('Number of words')
plt.title('Number of words per line in The Winter\'s Tale')
plt.show()

# --------- 3iii Character speech analysis ---------
Characters2 = [c.rstrip(':') for c in Characters]
char_longest_speech = {c: 0 for c in Characters2}
char_total_lines = {c: 0 for c in Characters2}

for line in decoded_lines:
    if line and line[0] not in "[({":
        speaker = line.split(':')[0]
        char_longest_speech[speaker] = max(char_longest_speech.get(speaker, 0), len(line) - 1)
        char_total_lines[speaker] += 1

# Longest speech top 10
top_longest = sorted(char_longest_speech.items(), key=lambda x: x[1], reverse=True)[:10]
fig, ax = plt.subplots(figsize=(6, 4))
ax.barh(range(10, 0, -1), [v for _, v in top_longest], edgecolor='black', color='gold')
ax.set_yticks(range(10, 0, -1))
ax.set_yticklabels([k for k, _ in top_longest])
ax.set_xlabel('Number of words in longest speech')
ax.set_ylabel('Character')
ax.set_title("Longest speech per character")
plt.show()

# Lines per character pie chart
top10_lines = sorted(char_total_lines.items(), key=lambda x: x[1], reverse=True)[:10]
others_sum = sum(v for _, v in sorted(char_total_lines.items(), key=lambda x: x[1], reverse=True)[10:])
top10_lines.append(('Other Characters', others_sum))

tot_lines = sum(v for _, v in top10_lines)
ratios = [v / tot_lines for _, v in top10_lines]

fig, ax = plt.subplots(figsize=(10, 8))
colors = plt.colormaps["tab20"](range(len(top10_lines)))
ax.pie([v for _, v in top10_lines], labels=[round(r, 2) for r in ratios], colors=colors, radius=0.85)
ax.legend([k for k, _ in top10_lines])
plt.title('Line involvement per character')
plt.show()

# --------- PART IV - Play structure ---------
scene_indices = [i for i, line in enumerate(decoded_lines) if '[[SCENE' in line]
scenes = [decoded_lines[scene_indices[i]:scene_indices[i+1]] for i in range(len(scene_indices)-1)]
scene_lengths = [len(scene) for scene in scenes]

plt.bar(range(1, len(scene_lengths)+1), scene_lengths, width=0.5, color='springgreen', edgecolor='black')
plt.xlabel('Scene number')
plt.ylabel('Number of lines')
plt.title('Number of lines in each scene')
plt.show()

# %%
