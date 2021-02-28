import os
import re
from collections import Counter

def isProblemDir(dirname):
	return True if re.match("Problem[0-9]+", dirname) is not None else False

def isLanguage(filename, language_ext_regex):
	return True if re.match(language_ext_regex, filename) is not None else False
	
print("Stats of Leetcode Repo")
problem_dirs = [x for x in os.listdir() if isProblemDir(x)]
daily_challenge_problems = os.listdir('./DailyChallenge')
problems_attempted = len(problem_dirs) + len(daily_challenge_problems)
print("Problems attempted: %d" % problems_attempted)
languages = {'python':'Solution.*py', 'java': '.*java'}
language_counts = Counter()
for problem_dir in problem_dirs:
	os.chdir(problem_dir)
	for language in languages:
		files_in_dir = os.listdir()
		for filename in files_in_dir:
			if isLanguage(filename, languages[language]):
				language_counts[language] += 1
				break
	os.chdir('..') 
	
# Why is the count 15 rn?
os.chdir('./DailyChallenge')
dc_problems = os.listdir()
for language in languages:
	for filename in dc_problems:
		if isLanguage(filename, languages[language]):
			language_counts[language] += 1
os.chdir('..')

for language in language_counts:
	print("	%s:	%d" % (language, language_counts[language]))

#print(problem_dirs)


