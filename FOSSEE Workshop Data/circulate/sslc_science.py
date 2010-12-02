science = {}

for record in open('sslc1.txt'):
#    record = record.strip()
    fields = record.split(';')

    region_code = fields[0].strip()

    if region_code not in science:
        science[region_code] = 0

    score_str = fields[6].strip()

    score = int(score_str) if score_str != 'AA' else 0

    if score > 90:
        science[region_code] += 1

figure(1)
pie(science.values(), labels=science.keys())
title('Students scoring 90% and above in science by region')
savefig('science.png')
