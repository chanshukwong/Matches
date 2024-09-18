# 移動一根火柴讓等式成立.
内換火柴=[['6','9'],[],['3'],['2','5'],[],['3'],['0','9'],[],[],['0','6']]
減一火柴=[[],[],[],[],[],[],['5'],['1'],['0','6','9'],['3','5']]
加一火柴=[['8'],['7'],[],['9'],[],['6','9'],['8'],[],[],['8']]

def 找答案(s):
	數字位置=[i for i in range(len(s)) if '0'<=s[i]<='9']	# 找出等式中數字的位置
	
	没有答案=True
	for i in 數字位置:
		for c in 内換火柴[int(s[i])]:
			ss=s[:i]+c+s[i+1:]
			try:
				if eval(ss.replace('=','==')):
					print(ss)
					没有答案=False
			except:
				pass
		
	for i in 數字位置:
		for c in 減一火柴[int(s[i])]:
			ss=s[:i]+c+s[i+1:]
			for j in 數字位置:
				if i==j:
					continue
				for d in 加一火柴[int(ss[j])]:
					tt=ss[:j]+d+ss[j+1:]
					try:
						if eval(tt.replace('=','==')):
							print(tt)
							没有答案=False
					except:
						pass
	if 没有答案:
		print('没有答案!')

# main
等式=input("輸入一條等式: ")
找答案(等式)
