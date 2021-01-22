# Brute Force POST Login request 
# What does this script do?

This script is designed to perform a brute force attack on an authentication web page that uses the POST method of the HTTP protocol, for authentication.

# How does it work ?

1. test the authentication with random username and password value.
2. It loads the two 'list of word file for the password and user name combinations.
3. use of a main thread, with two nested loops to test all combinations

# Help
  -s <username wordlist> -a <password wordlist> -v
  
	-h		--help				To print this message.
  
	-l		--url				web page (ex : -l http://test.com/login.php).
  
	-u		--user_option			username input name on form (ex: -u user).
  
	-p		--pass_option			password input name on form (ex: -p pass).
  
	-s		--username_wordlist		tfile with usernames to test (ex: -s /usr/share/wordlists/metasploit/http_default_users.txt.
  
	-a		--password_wordlist		file with passwords to test (ex: -a /usr/share/wordlists/metasploit/http_default_pass.txt.
  
	-v		--verbose			to active verbose mode (show evrey tentative).
  
	-t		--testall			to test all, without stop after a correcte user,pass.
  
	-o		--output			file to save correct user,pass.
  

# Example of use
## HTML Code on Authentication page 
  

```
r3d# brutforcePostRequest.py -s login
````
