# Brute Force POST Login request 
# What does this script do?

This script is designed to perform a brute force attack on an authentication web page that uses the POST method of the HTTP protocol, for authentication.

# How does it work ?

1. test the authentication with random username and password value.
2. It loads the two 'list of word file for the password and user name combinations.
3. use of a main thread, with two nested loops to test all combinations

# Help
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
 <form action="/login.php" method="post">
  <label for="fname">username:</label><br>
  <input type="text" id="username" name="username"><br>
  <label for="password">password:</label><br>
  <input type="password" id=password" name="password"><br><br>
  <input type="submit" value="login">
</form> 
```
## Exemple
___Stop on the frist correct login___
```
ssh$ brutforce_post.py -l http://localhost/login.php -u username -p password -s /usr/share/wordlists/metasploit/http_default_users.txt -a /usr/share/wordlists/metasploit/http_default_pass.txt -v
```
___Test All Combination and save all correct login to found.txt___
```
ssh$ brutforce_post.py -l http://localhost/login.php -u username -p password -s /usr/share/wordlists/metasploit/http_default_users.txt -a /usr/share/wordlists/metasploit/http_default_pass.txt -t -o found.txt
```
