awk -F, '$3 == 2' titanic.csv | sed 's/\bmale\b/M/g; s/\bfemale\b/F/g' | gawk -F, '{sum += $7; count++ } END {if (count > 0) print "Average Age : " sum / count; else print "No passengers found!"}'
