class Date(object):
    def GetDate(self):
        return '2016-5-12'

class Time(Date):
    def GetTime(self):
        return '05:13:07'

d = Date()
print(d.GetDate())
t = Time()
print(t.GetDate(), t.GetTime())
