#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas
import numpy


file = 'titanic.csv'
file_col = 'PassengerId'
global count_of_victims


def parse_name(row):
    if 'Mrs.' in row.split()[2] or 'Miss.' in row.split()[2]:
        name = row.split()[3]
    elif 'Mr.' in row.split()[2]:
        name = row.split()[3]
    else:
        name = row.split()[2]
    name = name.strip('"()')
    return name


def parse_date(file, file_col):
    data = pandas.read_csv(file, index_col=file_col)
    return data


def count_of_genders(col):
    count_of_man, count_of_women = 0, 0
    for i in col:
        if i == 'male':
            count_of_man += 1
        else:
            count_of_women += 1
    print('count of man:', count_of_man, '\ncount of women:', count_of_women)
    global count_of_victims
    count_of_victims = count_of_man + count_of_women


def part_of_survived(col):
    count_of_survs = 0
    for i in col:
        if i == 1:
            count_of_survs += 1
    print('part of survived', round(
        count_of_survs / count_of_victims * 100, 2), '%')


def part_of_firstclass(col):
    count_of_firstclass = 0
    for i in col:
        if i == 1:
            count_of_firstclass = +1
    print('part of passengers of first class:', round(
        count_of_firstclass / count_of_victims * 100, 2), '%')


def counts_of_age(col):
    total_age = 0
    count_nan = 0
    for i in col:
        if pandas.isnull(i):
            total_age += 0
            count_nan = +1
        else:
            total_age += i
    age_lst = col.dropna().tolist()
    age_lst.sort()
    print('half of age', round(total_age / (count_of_victims - count_nan)))
    if (len(age_lst) % 2) == 0:
        median = (age_lst[int(len(age_lst) / 2)] +
                  age_lst[int(len(age_lst) / 2) + 1]) / 2
    else:
        median = age_lst[int(len(age_lst) / 2)]
    print('median of age', median)


def correlatton_of_pierse(col1, col2):
    pass


def dic_sort(dic):
    for key in sorted(dic, key=lambda x: dic[x][1]):
        print('key', key, 'value', dic[key])


def get_key(dic, value):
    for k, v in dic.items():
        if v == value:
            return k


def adding_to_dic(dic, name):
    if name not in dic:
        dic.update({name: 1})
    else:
        count = dic.get(name)
        count += 1
        dic.update({name: count})
     # return dic


def max_value_of_dic(dic):
    max_value = 1
    for i in dic:
        if max_value < dic[i]:
            max_value = dic[i]
    return max_value


def what_is_popular_name(col1, col2):
    dic_of_man_names = {}
    dic_of_women_names = {}
    count = 0
    for k, i in enumerate(col1):
        count += 1
        if col2[count] == 'female':
            current_name = parse_name(i)
            adding_to_dic(dic_of_women_names, current_name)
    print('popular women names:')
    for i in range(1, 4):
        max_value = max_value_of_dic(dic_of_women_names)
        top = get_key(dic_of_women_names, max_value)
        print(top, dic_of_women_names[top])
        dic_of_women_names.pop(top)


def analyze_em(data):
    count_of_genders(data['Sex'])
    part_of_survived(data['Survived'])
    part_of_firstclass(data['Pclass'])
    counts_of_age(data['Age'])
    correlatton_of_pierse(data['SibSp'], data['Parch'])
    what_is_popular_name(data['Name'], data['Sex'])


def main():
    date = parse_date(file, file_col)
    analyze_em(date)

if __name__ == '__main__':
    main()
