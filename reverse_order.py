"""
reverses the order of words in the string. Additionally, within each word, reverse the order of the letters. However, preserve the capitalization of each letter.

For example:

vbnet

Input: "Hello World How Are You"
Output: "olleH dlroW woH erA uoY"

"""

def reverse(inp):
    inp = inp.split(" ")
    result = " "
    for words in inp:
        result = result+ " " + words[::-1]
    
    result = result.strip()
    return(result)


if __name__ == "__main__":
    result = reverse("Hello World How Are You")
    expected = "olleH dlroW woH erA uoY"

    if result == expected:
        print("Passed")
    else:
        print("Failed")