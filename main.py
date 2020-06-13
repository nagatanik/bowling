rule_configs = '10 10 18'
beats_str = '3 4 G 1 8 2 6 2 10 2 7 G 10 10 10 9 1 3'

n_frame, n_pins, n_throws = (int(e) for e in rule_configs.split())

list_beats =  [int(e) if e.isdigit() else 0 for e in beats_str.split()]

scores = [] # list of scores per frame 

i = 0
while i < n_throws:
    beat_1st = list_beats[i]

    if i == n_throws-1:
        scores.append(beat_1st)
        i += 1
    else:
        if beat_1st == n_pins:
            # strike
            score_frame = sum(list_beats[i:i+3])
            scores.append(score_frame)
            i += 1
        else:
            beat_2nd = list_beats[i+1]
            score_frame = beat_1st + beat_2nd
            if score_frame == n_pins:
                # spare
                score_frame += list_beats[i+2]
            
            scores.append(score_frame)
            i += 2

total_score = sum(scores)

print(total_score)

