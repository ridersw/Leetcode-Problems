from gingerit.gingerit import GingerIt

text = ""

while text != "exit":

	text = input("Enter the String- ")
	result = GingerIt().parse(text)

	print(f'Result: {result["result"]}')

