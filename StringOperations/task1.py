"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""
import re

def domain_name(url):

	my_pattern = re.compile(r'git')
	return my_pattern.match(url)
	




a = domain_name('http://github.com/carbonfive/raygun')
print(a)

