#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
show_age = 0
show_imp = 2
show_click = 3
count_impression = 0
count_age = 0
total_record = 0
ave_age = 0
count_click = 0
ave_CTR = 0.0001
largest_num = 0
oldest_person = 0
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
    count_impression = count_impression + int(line.strip().split(',')[show_imp])
    count_age = count_age +  int(line.strip().split(',')[show_age]) 
    count_click = count_click  +  int(line.strip().split(',')[show_click]) 

total_record = len(lines)

print '0:Age,1:Gender,2:Impressions,3:Clicks,4:Signed_In'
print 'TOTAL record:' + str(total_record)
print 'TOTAL Impressions:' + str(count_impression)
print 'TOTAL Age:' + str(count_age)

ave_age = count_age/total_record
print 'AVERAGE age:' + str(ave_age)

print 'TOTAL click:' + str(count_click)

ave_CTR = float(count_click)/float(count_impression)
print 'Average Click Thru Rate:' + str(ave_CTR)

largest_num = max(lines)
oldest_person = int(largest_num.strip().split(',')[0])
print 'OLDEST person:' + str(oldest_person)

### EOF ###