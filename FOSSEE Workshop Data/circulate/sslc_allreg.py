math_scores = []

for record in open('sslc1.txt'):
    fields = record.split(';')

    score_str = fields[5].strip()
    score = int(score_str) if score_str != 'AA' else 0

    math_scores.append(score)

# Using lists
print 'Mean: ', mean(math_scores)
print 'Median: ', median(math_scores)
print 'Standard Deviation: ', std(math_scores)

# Using arrays
math_array = array(math_scores)
print 'Mean: ', mean(math_array)
print 'Median: ', median(math_array)
print 'Standard Deviation: ', std(math_array)
