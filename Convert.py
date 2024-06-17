import re
from datetime import date
todays_date = date.today()

####### —————————————— Processing ——————————————

inputFile = "./macula-SBLGNTa.txt"
outputFile1 = "./Macula-CN-Ruby.nt"
#outputFile2 = "./Macula-EN-Ruby.nt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f1 = open(outputFile1,'w',encoding="utf_8_sig")
#f2 = open(outputFile2,'w',encoding="utf_8_sig")
bcv = ""
gaplines = ['MAT 17:22','MAT 18:12','MAT 23:15','MRK 7:17','MRK 9:45','MRK 9:47','MRK 11:27','MRK 15:29','LUK 17:37','LUK 23:18','JHN 5:5','ACT 8:38','ACT 15:35','ACT 20:1','ACT 24:8','ACT 28:30','1CO 1:1','GAL 1:1']

for line in Lines:
	if len(line) > 1:
		line = re.sub(r'\n',r'',line)
		x = re.split("\t", line)

		
		# add emphasis for punctuation marks
		x[5] = re.sub(r'([\.,;·])',r'<mark class="pm">\1</mark>',x[5])

		# add emphasis for Verbs
		if (re.match(r'V-...-\d.',x[9])) or (re.match(r'V-...⁞...-\d.',x[9])) or (re.match(r'V-....-\d.',x[9])):
			x[4]='<strong>'+x[4]+'</strong>'

		# add emphasis for participles
		elif (re.match(r'V-..P-...',x[9])) or (re.match(r'V-..P-...⁞...',x[9])) or (re.match(r'V-...P-...',x[9])):
			x[4]='<em>'+x[4]+'</em>'

		# add emphasis for infinitives
		elif (re.match(r'V-..N',x[9])) or (re.match(r'V-...N',x[9])):
			x[4]='<em>'+x[4]+'</em>'

		else:
			x[4]=x[4]

		if (x[0]==bcv):
			f1.write("<RUBY><ruby><ruby>"+x[4]+"<rt>"+x[6]+"</rt></ruby><rt>"+x[2]+"</rt></ruby><rt>"+x[9]+"</rt></RUBY>"+x[5])
		else:
			if (x[0] in gaplines): f1.write("\n")
			if (x[0] == "1CO 1:1"): f1.write("\n\n")
			if (x[0] == "MAT 1:1") or (x[0] == "3JN 1:15") or (x[0] == "REV 12:18"): 
				f1.write(x[0]+' ')
			else: 
				f1.write("\n"+x[0]+' ')
			bcv = x[0]
			f1.write("<RUBY><ruby><ruby>"+x[4]+"<rt>"+x[6]+"</rt></ruby><rt>"+x[2]+"</rt></ruby><rt>"+x[9]+"</rt></RUBY>"+x[5])


# ---------- 
f1.write("\n\n\nlang=grc\nnotags=1\nshort.title=Macula-CN\nversion.date="+str(todays_date)+"\ndescription=macula-SBLGNTy (https://github.com/Andley/macula-SBLGNTa)")

f1.close()
