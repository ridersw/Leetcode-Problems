class Solution:
	def reorderLogFiles(self, logs):
		
		digitLogs = []
		letterLogs = []
		
		#newLog = logs[:]
		
		for log in logs:
			#print(f'log: {log}')
			tempLog = log.split(" ")
			tempLog = tempLog[1:]
			tempLog = "".join(tempLog)
			print(f'Checking for {tempLog}')
			if tempLog.isdigit():
				digitLogs.append(log)
			else:
				letterLogs.append(log)
				
		print(f'digitLogs: {digitLogs}')
		print(f'letterLogs: {letterLogs}')
		
		
		for swi in range(len(letterLogs)):
			for swj in range(len(letterLogs)-1-swi):
				space1 = letterLogs[swj].index(" ")
				space2 = letterLogs[swj+1].index(" ")
				if letterLogs[swj][space1:] > letterLogs[swj+1][space2:]:
					letterLogs[swj], letterLogs[swj+1] = letterLogs[swj+1], letterLogs[swj]
		
		letterLogs.extend(digitLogs)
		return letterLogs					
		
if __name__ == "__main__":
	obj = Solution()

	logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
	logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]	
	logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]	
	
	print(obj.reorderLogFiles(logs))
	#print(obj.reorderLogFiles(logs) == '["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]')
	
	
#You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

#There are two types of logs:

#    Letter-logs: All words (except the identifier) consist of lowercase English letters.
#    Digit-logs: All words (except the identifier) consist of digits.

#Reorder these logs so that:

#    The letter-logs come before all digit-logs.
#    The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
#    The digit-logs maintain their relative ordering.

#Return the final order of the logs.	