'''
call the function with your name as a parameter (string)
then run the code to see how your name will be printed
reminder:
1- git add .
2- git commit -m "any message"
3- git push
'''
import string

s = "闩⻏⼕ᗪ🝗ﾁᎶ卄讠丿长㇄爪𝓝ㄖ尸Ɋ尺丂〸ㄩᐯ山〤丫Ⲍ"
alphabet = {}

for i in range(len(string.ascii_lowercase)):
	alphabet[string.ascii_lowercase[i]] = s[i]

def print_name(name):
	for char in name:
		char = char.lower()
		if char in alphabet:
			print(alphabet[char], end="")
		else:
			print(char, end="")
	print()

print_name("Yusuf el-nady")
print_name("Youssef Saeed")
print_name("Shahd Tharwat")
print_name("Hana Ghanem")
print_name("Heidi Ahmed")
print_name("Gasser Elgazoly")
print_name("Abdallah elsherbiny")
