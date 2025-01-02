

def main():
    student = {'name': "Huma", 'age': 17, 'salary': 10.2}
    '' '#this is a way to define dictionary, you give it first all the data with keys'
    'then you can call data with the key'
    sstudent = dict(Name="Huma", Age=17, Salary=5.26)
    '' '#this is the basic way to define dictionary, you give it first all the data with keys'
    'then you can call data with the key'
    sstudent['Name'] = "Humam"
    ''  '#this is how to add item to dictionary'
    sstudent["Dept"] = "College PHd"
    print(sstudent, type(sstudent))
    '' '#b4 delete "Dept" '
    del sstudent["Dept"]
    ''  '#this is how to delete a data from the dict'
    print(student, type(student))
    print(student['name'])
    ''  '#"name" here is the key, so it calls "Huma" and print it'
    print(student['age'])
    ''  '#"age" here is the key, so it calls "17" and print it'
    print(sstudent, type(sstudent))
    ''  '#after delete "Dept"'
    print(sstudent['Name'])
    ''  '#"name" here is the key, so it calls "Huma" and print it'
    print(sstudent['Age'])
    ''  '#"age" here is the key, so it calls "17" and print it'
    sstudent.clear()
    ''  '#how to clear the items in any dict'
    print(sstudent, type(sstudent))


if __name__ == '__main__':
    main()
