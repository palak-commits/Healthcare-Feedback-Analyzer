import pickle

# Load model + vectorizer
with open("ml_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# ML function
def ml_predict(user_input):
    user_vector = vectorizer.transform([user_input])
    return model.predict(user_vector)[0]

# Rule-based
def rule_based(user_input):
    keywords = {
    "staff": ["doctor", "nurse", "rude", "staff"],
    "delay": ["wait", "deri", "late", "delay", "intezaar"],
    "facility": ["clean", "room", "saaf", "facility", "hospital", "accha", "acha"],
    "billing": ["payment", "bill", "billing"],
    "treatment": ["treatment", "ilaaj", "wrong"]
}
    user_input = user_input.lower()
    matched = []

    for label, words in keywords.items():
        if any(word in user_input for word in words):
            matched.append(label)

    return matched

# Combined
def combined_output(user_input):
    rule = rule_based(user_input)
    ml = str(ml_predict(user_input))
    final = list(set(rule + [ml]))
    return final, rule, ml