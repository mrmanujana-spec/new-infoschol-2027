# 1. capitalize() - Converts the first character to upper case
print("hello world".capitalize())
# Output: "Hello world"

# 2. casefold() - Converts string into lower case (stronger than lower())
print("ß".casefold())
# Output: "ss"

# 3. center() - Returns a centered string
print("python".center(12, "-"))
# Output: "---python---"

# 4. count() - Returns the number of times a specified value occurs
print("banana".count("a"))
# Output: 3

# 5. encode() - Returns an encoded version of the string (UTF-8 bytes)
print("hello".encode())
# Output: b'hello'

# 6. endswith() - Returns true if string ends with specified value
print("image.png".endswith(".png"))
# Output: True

# 7. expandtabs() - Sets the tab size of the string
print("H\te\tl\tl\to".expandtabs(4))
# Output: "H   e   l   l   o"

# 8. find() - Searches for specified value and returns position (-1 if not found)
print("python".find("th"))
# Output: 2

# 9. format() - Formats specified values in a string
print("Hello, {}!".format("Alice"))
# Output: "Hello, Alice!"

# 10. format_map() - Formats specified values using a dictionary/map
point = {'x': 4, 'y': -5}
print("Point: ({x}, {y})".format_map(point))
# Output: "Point: (4, -5)"

# 11. index() - Searches for specified value, returns position (raises ValueError if not found)
print("python".index("th"))
# Output: 2

# 12. isalnum() - Returns True if all characters are alphanumeric
print("Python3".isalnum())
# Output: True

# 13. isalpha() - Returns True if all characters are in the alphabet
print("Python".isalpha())
# Output: True

# 14. isascii() - Returns True if all characters are ASCII characters
print("Hello123!".isascii())
# Output: True

# 15. isdecimal() - Returns True if all characters are decimals (0-9)
print("12345".isdecimal())
# Output: True

# 16. isdigit() - Returns True if all characters are digits (includes superscripts)
print("12345".isdigit())
# Output: True

# 17. isidentifier() - Returns True if string is a valid Python identifier/variable name
print("my_var".isidentifier())
# Output: True

# 18. islower() - Returns True if all characters are lower case
print("hello".islower())
# Output: True

# 19. isnumeric() - Returns True if all characters are numeric (includes fractions/roman numerals)
print("12345".isnumeric())
# Output: True

# 20. isprintable() - Returns True if all characters are printable
print("Hello World!".isprintable())
# Output: True

# 21. isspace() - Returns True if all characters are whitespaces
print("   \t\n".isspace())
# Output: True

# 22. istitle() - Returns True if string follows rules of a title
print("Hello World".istitle())
# Output: True

# 23. isupper() - Returns True if all characters are upper case
print("HELLO".isupper())
# Output: True

# 24. join() - Joins elements of an iterable to end of string
print("-".join(["a", "b", "c"]))
# Output: "a-b-c"

# 25. ljust() - Returns a left justified version of string
print("cat".ljust(8, "*"))
# Output: "cat*****"

# 26. lower() - Converts string into lower case
print("HELLO".lower())
# Output: "hello"

# 27. lstrip() - Returns a left trim version of string
print("  hello  ".lstrip())
# Output: "hello  "

# 28. maketrans() & 41. translate() - Translation table utilities
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))
# Output: "h2ll4 w4rld"

# 29. partition() - Returns a tuple where string is parted into three parts
print("apple-banana-cherry".partition("-"))
# Output: ('apple', '-', 'banana-cherry')

# 30. replace() - Returns string where specified value is replaced
print("Hello World".replace("World", "Python"))
# Output: "Hello Python"

# 31. rfind() - Searches for specified value, returns last position
print("banana".rfind("a"))
# Output: 5

# 32. rindex() - Searches for specified value, returns last position
print("banana".rindex("a"))
# Output: 5

# 33. rjust() - Returns a right justified version of string
print("cat".rjust(8, "*"))
# Output: "*****cat"

# 34. rpartition() - Returns a tuple starting from the right parted into three parts
print("apple-banana-cherry".rpartition("-"))
# Output: ('apple-banana', '-', 'cherry')

# 35. rsplit() - Splits string at specified separator from right, returns list
print("a,b,c,d".rsplit(",", 2))
# Output: ['a,b', 'c', 'd']

# 36. rstrip() - Returns a right trim version of string
print("  hello  ".rstrip())
# Output: "  hello"

# 37. split() - Splits string at specified separator, returns list
print("apple,banana,cherry".split(","))
# Output: ['apple', 'banana', 'cherry']

# 38. splitlines() - Splits string at line breaks, returns list
print("Line 1\nLine 2".splitlines())
# Output: ['Line 1', 'Line 2']

# 39. startswith() - Returns True if string starts with specified value
print("Hello".startswith("He"))
# Output: True

# 40. strip() - Returns trimmed version of string (both sides)
print("  hello  ".strip())
# Output: "hello"

# 42. swapcase() - Swaps cases, lower becomes upper and vice versa
print("PyThOn".swapcase())
# Output: "pYtHoN"

# 43. title() - Converts first character of each word to upper case
print("hello world".title())
# Output: "Hello World"

# 44. upper() - Converts string into upper case
print("hello".upper())
# Output: "HELLO"

# 45. zfill() - Fills string with specified number of 0 values at start
print("42".zfill(5))
# Output: "00042"