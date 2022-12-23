def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    min_score_broke = 0
    max_score_broke = 0
    for score in scores:
        if score < min_score:
            min_score = score
            min_score_broke += 1
        elif score > max_score:
            max_score = score
            max_score_broke += 1
    return [max_score_broke, min_score_broke]

print(breakingRecords([12, 24, 10, 24]))