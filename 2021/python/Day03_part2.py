
# read input
with open('PuzzleInput_day03.txt') as f:
    lines = f.readlines()
    report = [line.strip() for line in lines]

# find oxygen generator rating
report_copy = report.copy()
column = 0
while len(report_copy) > 1:
    one_count = 0
    for binary in report_copy:
        if int(binary[column]) == 1: one_count = one_count + 1
    most_common = 1 if one_count >= len(report_copy)/2 else 0
    report_copy = [binary for binary in report_copy if int(binary[column]) == most_common]
    column = column + 1
oxygen_generator_rating = report_copy[0]
print(oxygen_generator_rating, int(oxygen_generator_rating,2))

# find oxygen generator rating
report_copy = report.copy()
column = 0
while len(report_copy) > 1:
    one_count = 0
    for binary in report_copy:
        if int(binary[column]) == 1: one_count = one_count + 1
    least_common = 0 if one_count >= len(report_copy)/2 else 1
    report_copy = [binary for binary in report_copy if int(binary[column]) == least_common]
    column = column + 1
co2_scrubber_rating = report_copy[0]
print(co2_scrubber_rating, int(co2_scrubber_rating, 2))

print(int(oxygen_generator_rating,2)*int(co2_scrubber_rating, 2))