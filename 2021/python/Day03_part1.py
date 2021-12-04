
# read input
with open('PuzzleInput_day03.txt') as f:
    lines = f.readlines()
    report = [line.strip() for line in lines]

# set parameter
total_binaries = len(report)
total_bits = len(report[0])
gamma_rate = ''
epsilon_rate = ''
one_count = [0 for i in range(total_bits)]

# count ones

# only works if total_binaries < 10
# one_count = 0
# for binary in report:
#     for k, bit in enumerate(binary):
#         one_count = one_count + int(bit)*10**(total_bits-k-1)

for binary in report:
    for i, bit in enumerate(binary):
        if int(bit) == 1 : one_count[i] = one_count[i] + 1

# get most common bit
for count in one_count:
    if count > total_binaries/2:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

# calculate solution
print(gamma_rate, int(gamma_rate,2))
print(epsilon_rate, int(epsilon_rate,2))
print(int(gamma_rate,2)*int(epsilon_rate,2))
