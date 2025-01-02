def main():
    amount = 30
    data = "{} is high or {} is low".format(amount, 20)
    print(data, type(data))
    datalen = "is good"
    print(len(datalen))
    print(datalen[1])


if __name__ == '__main__':
    main()

''  '#num = 30 integer '
''  '#num = 3.5 float '
''  '#num "hi" string '
''  '#num = 30/5 float '
''  '#num = int (30/5) integer '
''  '#num =(5*12) integer '
''  '#num = float (5*12) float '
''  '#print((num, type(num))) '
''  '#data = "my\nname\nis\nhumam", the "\n" is for next line '
''  '#data = r"my\nname\nis\nhumam", the "\n" is for next line, r is disabling the \n and considering it as text '
''  '#Form1: amount=30 data= "{} is high".format(amount) print(data, type(data)) this;ll take the amount&add "is high"'
''  '#Form2: amount = 30 data = "{} is high or {} is low".format(amount,20) print(data, type(data))'
''  '#in old versions of python you;ll use: %s is high:% amount '
'' '#amount = 30 i=0, s=1, " "=2, g=3, o=4, o=5, d=6' \
'   data = "{} is high or {} is low".format(amount, 20)   print(data, type(data))   datalen = "is good"' \
'   print(len(datalen))   print(datalen[0]) ##prints the location in [datalen = "is good"]'
