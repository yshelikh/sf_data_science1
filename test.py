path = '/Users/yshel/Documents/Yulia Folder/Studyng/SkillFactory/Python/Семинары/Ecoli_5_lines_1.txt'

#path = '/Users/iadovgopolyi/Desktop/Работа/SkillFactory/Программирование на Python/Занятие 2/sequence.fasta'

file = open(path, mode='r')

text = file.read()
# for line in text:
#     print(line)
    
    
coli_dict = {}
str=""
for line in text:
    line = str+line
    for index in range(0, len(line) - 5):
        six = line[index:(index + 6)]
        if six not in coli_dict:
            coli_dict[six] = 1
        else:
            coli_dict[six] += 1
    str = line[-5:]
print(coli_dict)

# textok = "qweertyu"
# str = textok[-5:]
# text = str+textok
# print(text)