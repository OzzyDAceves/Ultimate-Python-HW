print("Insert a word")
Input_text = input()
word = Input_text.upper()


def NotSpaces(text):
    return [char for char in text if char != " "]


def CountString(String):
    String = {}
    word_ = NotSpaces(word)
    for char in word_:
        if char in String:
            String[char] += 1
        else:
            String[char] = 1
    return String


# def SortDictionary(Dictionary):
#     Dictionary = CountString(word)
#     SortDictionary_ = []
#     for value in Dictionary.items():
#         SortDictionary_.append(value)
#     SortDictionary_.sort(key=lambda el: el[1], reverse=True)
#     return SortDictionary_

def SortDictionary(Dictionary):
    return sorted(
        Dictionary.items(),
        key=lambda key: key[1],
        reverse=True
    )


def HighestValue(Highest):
    Max = Highest[0][1]
    Max_list = {}
    for comparison in Highest:
        if Max > comparison[1]:
            break
        Max_list[comparison[0]] = comparison[1]
    return Max_list


def Message(dictionary):
    Message_ = "The most repeated are: \n"
    for key, value in dictionary.items():
        Message_ += f"- {key} with {value} times \n"
    return Message_


String_ = NotSpaces(word)
Count_Dictionary = CountString(String_)
List_Sort = SortDictionary(Count_Dictionary)
Mode = HighestValue(List_Sort)
Menssage_ = Message(Mode)
print(Menssage_)
