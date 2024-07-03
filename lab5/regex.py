#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def match_ab(string):
    
    pattern = r'ab*'
    
    return bool(re.fullmatch(pattern, string))

# Example 
print(match_ab("a"))     # True
print(match_ab("ab"))    # True
print(match_ab("abb"))   # True
print(match_ab("b"))     # False
print(match_ab("aab"))   # False


#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def match_a_2_to_3_b(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    return False

# Example 
print(match_a_2_to_3_b("abb"))  # True
print(match_a_2_to_3_b("abbb"))  # True
print(match_a_2_to_3_b("ab"))  # False
print(match_a_2_to_3_b("abbbb"))  # False

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def find_lowercase_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

# Example 
print(find_lowercase_underscore("hello_world hi_kbtu"))  # ['hello_world', 'hi_kbtu']

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def find_uppercase_followed_by_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

# Example 
print(find_uppercase_followed_by_lowercase("Hello World"))  # ['Hello', 'World']

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def match_a_anything_b(string):
    pattern = r'a.*b'
    if re.fullmatch(pattern, string):
        return True
    return False

# Example 
print(match_a_anything_b("a123b"))  # True
print(match_a_anything_b("ab"))  # True
print(match_a_anything_b("a_b"))  # True
print(match_a_anything_b("a"))  # False

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def replace_with_colon(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

# Example 
print(replace_with_colon("Hello, world."))  # 'Hello: world:'

#7 Write a python program to convert snake case string to camel case string.
import re

def snake_to_camel(string):
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Example 
print(snake_to_camel("hello_world"))  # 'helloWorld'

#8 Write a Python program to split a string at uppercase letters.
import re

def split_at_uppercase(string):
    pattern = r'[A-Z][^A-Z]*'
    return re.findall(pattern, string)

# Example 
print(split_at_uppercase("HelloWorld"))  # ['Hello', 'World']

#9 Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(string):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', string)

# Example 
print(insert_spaces("HelloWorld"))  # 'Hello World'

#10 Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(string):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', string).lower()

# Example 
print(camel_to_snake("helloWorld"))  # 'hello_world'
