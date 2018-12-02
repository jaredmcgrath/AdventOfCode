# INCOMPLETE
data = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
data = [int(x) for x in data.split("\t")]
patterns = []
count = 0
while data not in patterns:
    patterns.append(data)
    # Find max bank
    max_val = data[0]
    max_index = 0
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
            max_index = i
    # Take all blocks out of max bank
    data[max_index] = 0
    # Redistribute blocks to all banks
    for i in range(max_val):
        data[(max_index+i+1) % len(data)] += 1
    count += 1
print(count)
