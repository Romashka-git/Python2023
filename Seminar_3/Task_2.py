# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# res_dict = list()

# for cor_dict in my_dict:
#     for key in cor_dict:
#         res_dict.append(cor_dict[key])

# print(res_dict)
# res_dict = set(res_dict)
# print(res_dict)

# ----------------------------------------------------

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# res_dict = set()

# for cor_dict in my_dict:
#     for key in cor_dict:
#         res_dict.add(cor_dict[key])


# print(res_dict)

# ----------------------------------------------------

my_dict = [{"V": "S001", "VII": "S008"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
res_dict = list()

for cor_dict in my_dict:
    for key in cor_dict:
        res_dict.append(cor_dict[key])

print(res_dict)
res_dict = set(res_dict)
print(res_dict)