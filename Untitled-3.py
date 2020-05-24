import re 

def popular_words(text: str, words: list) -> dict:
    # for i in words:
    #     p = re.compile(r"\bi\b", re.I)
    #     m = p.findall(text)
    #     print(m)

    # text = text.lower()# your code here
    words_in_text = tuple(map(str.lower, text.split())) 
    print({word:words_in_text.count(word) for word in words})

    # print(data)
    # data_result = []
    # for i in range(len(data)) : 
    #     a = data.pop(0)
    #     if "\n" not in a : data_result.append(a)
    #     else : data_result += a.split("\n")
    # print(data_result)
    # result = []
    # for i in words :
    #     count = 0
    #     for j in data_result : 
    #         if i == j : count += 1
    #     result.append(count)
    #     count = 0
    # result_final = dict() 
    # for k, v in zip(words, result) : 
    #     result_final[k] = v
    # print(result_final)
popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near'])


# if __name__ == '__main__':
#     print("Example:")
#     print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
