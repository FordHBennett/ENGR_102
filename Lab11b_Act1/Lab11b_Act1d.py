# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act1d
# Date:         11/29/2021
import csv

def partd(exel):
    file = open(exel, 'r')
    holder = []
    for line in file:
        holder.append(line.split(','))
#it wont work
    for i in range(len(holder)):
        holder[i][2] = (holder[i][2])[-2]
    with open('test.tsv', 'wt') as out_file:
        for i in range(len(holder)):
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(holder)

    return 'Done!'
