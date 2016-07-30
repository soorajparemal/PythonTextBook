#solution is to sort the word you're searching anagrams for (for example using sorted), sort the alternative and compare those.

#So if you would be searching for anagrams of 'rac' in the list ['car', 'girl', 'tofu', 'rca'], your code could look like this:

word = sorted('rac')
alternatives = ['car', 'girl', 'tofu', 'rca']

for alt in alternatives:
    if word == sorted(alt):
        print alt
