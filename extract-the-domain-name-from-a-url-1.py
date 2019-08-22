'''
#2019-08-22

        https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/

Write a function that when given a URL as a string, parses out just the
domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
def domain_name(url):
    pass
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    return url.split('.')[0]

s = input()
print(domain_name(s))

'''By Abhishek Adhikari'''
