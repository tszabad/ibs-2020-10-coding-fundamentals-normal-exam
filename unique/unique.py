def unique(str1):
    char_list = []
    chars = {}
    for char in str1:
            if char in chars:
                    chars[char] += 1
            else:
                    chars[char] = 1
    
    for i, k in chars.items():
        if k == 1:
            char_list.append(i)

    return char_list

print(unique("anagram"))