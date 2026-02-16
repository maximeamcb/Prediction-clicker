#prediction autoclick prochain score 5 secondes

def score_prediction(values):
    if len(values) == 0:
        return None
    total_weight = sum(range(1, len(values) + 1))
    weighted_sum = sum(value * weight for value, weight in zip(values, range(1, len(values) + 1)))
    return weighted_sum / total_weight

#5 scores precedents

print ("Entrez les 5 scores précédents :")
scores = []
for i in range(5):
    score = float(input(f"Score {i + 1}: "))
    scores.append(score)
predicted_score = score_prediction(scores)
print(f"Le score prédit pour la prochaine partie est : {predicted_score:.2f}")
