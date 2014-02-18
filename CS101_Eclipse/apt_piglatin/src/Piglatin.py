'''
Created on Feb 9, 2013

@author: Jimmy
'''
def convert(s):
    if "aeiou".count(s[0]) > 0:
        return s + "-way"
    if s[0] == 'q':
        return s[2:] + "-quay"
    for i in range(0,len(s)):
        if "aeiou".count(s[i]) > 0:
            return s[i:] + "-" + s[:i] + "ay"
    return s
    