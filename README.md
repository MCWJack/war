# war
Run the classic card game war and collect stats

for many runs try:
run.sh | awk -F'\t' 'NR<4;NR>=4{if($5=="p1")tally+=1}END{print tally/(NR-3)}'

