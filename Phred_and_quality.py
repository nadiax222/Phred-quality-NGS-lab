Phre




	
	
 # 1. Określi system kodowania jakości (Phred+33 czy Phred+64).

sequence = 'ACGTGCATAGCTAGCATTACGATACGAGCCGGCGGCAAATATAGCG '
quality = 'ACDFAAEHHHBBAA?;<<CDEAD98<;;<ADE??<874873012,/.' #linijka zawierająca jakość
min_ascii = min(ord(ch) for ch in quality) #ord zwraca wartość liczbową odpowiadającą danemu znakowi, w tym wypadku minimalną dla znaków w linijce 'quality'
if min_ascii < 64:
	encoding = "Phred+33" # jeśli minimalny znak < 64, pasuje do kodowania jakości phred 33
else:
	encoding = "Phred+64"
	
print(min_ascii, encoding)

 # 2. Znajdzie pozycję o najwyższej i najniższej jakości.
	
offset = 33 #wartość, która jest dodawana do surowego wyniku jakości Phred do zakodowania go jako znak
qual = [ord(ch) - offset for ch in quality] #obliczam jakość z uwzględnieniem offset, by zmienić znak na 
min_quality = min(qual)
max_quality = max(qual)
min_pos = qual.index(min_quality) + 1
max_pos = qual.index(max_quality) + 1
print("min:", min_quality, "max:", max_quality, "minimalna pozycja:", min_pos, "max pozycja:", max_pos)


 # 3. obliczy średnią jakość dla odczytu.

avg = sum(qual) / len(qual)
print("srednia:", avg)

 # 4. Policzy liczbę pozycji o jakości poniżej 20 w skali Phred oraz ich procentowy udział.
empty = 0
for q in qual: 
	if q < 20:
		empty += 1
	else:
		continue
print("liczba pozycji o jakości poniżej 20:", empty)

procent = empty / len(qual) * 100
print("procentowy udział:", procent, "%")

 # 5. Obliczy prawdopodobieństwo błędu dla Q=25, wiedząc, że: Q=−10log⁡10(P(error)) / Q=−10log10​(P(error))
#trzeba obrocic wzor tak zeby mogl wyliczyc P zamiast Q 
import math 
Q = 25 # quality mamy okreslony
p_error = 10 ** (-Q/10)
print("prawdopodobienstwo błędu:", p_error)
print("prawdopodobienstwo bledu w procentach:", p_error*100, "%")

 # 6. Określi spodziewaną liczbę błędów w tej sekwencji.
	
#P(error) = 10^(-Q/10)
#p_error2 = [10 ** (-Q/10) for q in qual]
expected_errors = sum(10 ** (-q/10) for q in qual)
print("Spodziewana liczba błędów:", expected_errors)



