from collections import Counter

words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

ocurrences = Counter(words)

print(f"Palabra con mas ocurrencias: {ocurrences.most_common(1)[0][0]}, cantidades: {ocurrences.most_common(1)[0][1]}")

