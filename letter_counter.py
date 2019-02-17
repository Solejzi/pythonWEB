from collections import Counter
import zipfile
with zipfile.ZipFile("zad_1_word.zip", "r") as zip_ref:
    zip_ref.extractall()
    pass
str_container = ''
for i in range (0,30):
    with open(('word_' + str(i)+'.txt')) as file:
        str_container += file.readline()
lower_str = str_container.lower()
result = Counter(lower_str)
print(result)
