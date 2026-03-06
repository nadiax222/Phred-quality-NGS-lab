 # 1. Determine the quality score encoding system (Phred+33 or Phred+64).

sequence = 'ACGTGCATAGCTAGCATTACGATACGAGCCGGCGGCAAATATAGCG '
quality = 'ACDFAAEHHHBBAA?;<<CDEAD98<;;<ADE??<874873012,/.' # line containing quality scores
min_ascii = min(ord(ch) for ch in quality) # ord returns the numeric value for a character, here the minimum in the quality string
if min_ascii < 64:
	encoding = "Phred+33" # if the minimum character < 64, it matches Phred+33 encoding
else:
	encoding = "Phred+64"
	
print(min_ascii, encoding)

 # 2. Find positions with the highest and lowest quality.
	
offset = 33 # value added to raw Phred score to encode it as a character
qual = [ord(ch) - offset for ch in quality] # compute quality scores by subtracting offset from each character
min_quality = min(qual)
max_quality = max(qual)
min_pos = qual.index(min_quality) + 1
max_pos = qual.index(max_quality) + 1
print("min:", min_quality, "max:", max_quality, "minimum position:", min_pos, "max position:", max_pos)


 # 3. Calculate the average quality for the read.

avg = sum(qual) / len(qual)
print("average:", avg)

 # 4. Count positions with quality below 20 on the Phred scale and compute their percentage.
empty = 0
for q in qual: 
	if q < 20:
		empty += 1
	else:
		continue
print("number of positions with quality below 20:", empty)

procent = empty / len(qual) * 100
print("percentage:", procent, "%")

 # 5. Calculate error probability for Q=25 using formula Q = -10 log10(P(error)).
# reverse the formula to compute P from Q
import math 
Q = 25 # quality mamy okreslony
p_error = 10 ** (-Q/10)
print("error probability:", p_error)
print("error probability in percent:", p_error*100, "%")

 # 6. Determine the expected number of errors in this sequence.
	
#P(error) = 10^(-Q/10)
#p_error2 = [10 ** (-Q/10) for q in qual]
expected_errors = sum(10 ** (-q/10) for q in qual)
print("Expected number of errors:", expected_errors)



