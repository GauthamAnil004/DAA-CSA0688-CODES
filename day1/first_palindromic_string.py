def first_palindromic_string(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words1 = ["abc","car","ada","racecar","cool"]
words2 = ["notapalindrome","racecar"]
print(first_palindromic_string(words1))  
print(first_palindromic_string(words2)) 