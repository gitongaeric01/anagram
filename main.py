# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    if len(word) !=len(anagram):
        return False
    else:
        if ''.join(sorted(word)) == ''.join(sorted(anagram)):
            return True
        else:
            return False

print(find_anagram("elbow","below"))


