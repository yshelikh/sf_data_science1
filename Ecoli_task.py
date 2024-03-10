path = '/Users/yshel/Documents/Yulia Folder/Studyng/SkillFactory/Python/IDE/Ecoli_5_lines_1.txt'

file = open(path, mode='r')

text = file.read()
# for line in text:
#     print(line)
    
    
coli_dict = {}
str=""
for line in text:
    line = str+line
    line= line.replace("\n", "")
    for index in range(0, len(line) - 5):
        six = line[index:(index + 6)]
        if six not in coli_dict:
            coli_dict[six] = 1
        else:
            coli_dict[six] += 1
    str = line[-5:]
print(set(coli_dict.values()))
#{1,2,3}
list_of_frequent_six = []
for six,value in coli_dict.items():
    if coli_dict[six] ==3:
        list_of_frequent_six.append((six,value))
print(list_of_frequent_six)     
#[('AAAAAA', 3), ('ACCACC', 3), ('CCACCA', 3), ('CACCAT', 3), ('AGGTAA', 3), ('GGTAAC', 3), ('TTTTTT', 3)]

#print(list(coli_dict()))