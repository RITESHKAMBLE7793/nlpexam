# Simple Viterbi POS Tagging (No external libraries)

# Sample probabilities (manually defined)
states = ["NOUN", "VERB"]

start_prob = {"NOUN": 0.6, "VERB": 0.4}

transition_prob = {
    "NOUN": {"NOUN": 0.3, "VERB": 0.7},
    "VERB": {"NOUN": 0.8, "VERB": 0.2}
}

emission_prob = {
    "NOUN": {"I": 0.1, "love": 0.1, "coding": 0.8},
    "VERB": {"I": 0.0, "love": 0.9, "coding": 0.1}
}

# Sentence
sentence = ["I", "love", "coding"]

# Viterbi Algorithm
V = [{}]
path = {}

# Step 1: Initialization
for state in states:
    V[0][state] = start_prob[state] * emission_prob[state].get(sentence[0], 0.001)
    path[state] = [state]

# Step 2: Recursion
for t in range(1, len(sentence)):
    V.append({})
    new_path = {}

    for curr_state in states:
        prob, prev_state = max(
            (V[t-1][ps] * transition_prob[ps][curr_state] *
             emission_prob[curr_state].get(sentence[t], 0.001), ps)
            for ps in states
        )

        V[t][curr_state] = prob
        new_path[curr_state] = path[prev_state] + [curr_state]

    path = new_path

# Step 3: Final Result
n = len(sentence) - 1
prob, state = max((V[n][s], s) for s in states)

print("Sentence:", sentence)
print("POS Tags:", path[state])