# datetime هنا قمنا بتضمين كل محتوى الموديول
import datetime
# dt يمثل تاريخ + وقت محدد و قمنا بتخزينه في الكائن datetime هنا قمنا بإنشاء كائن من الكلاس
dt = datetime.datetime(2012, 4, 5, 7, 30, 46)
# dt هنا قمنا بعرض قيمة الكائن
print(dt)
# تم حفظ الوقت الحالي في الكائن
de = datetime.datetime.now()
# عرض / طباعة قيمة الكائن
print(de)
# de الموجودة في الكائن year هنا قمنا بعرض قيمة الخاصية
print('This tutorial is written in', de.year)
# و من ثم قمنا بطباعته dt لها كنص حتى ترجع إسم الشهر المخزن في الكائن %B و تمرير الرمز strftime() هنا قمنا باستدعاء الدالة
print(de.strftime('%B'))
# بشكل كامل و من ثم قمنا بطباعته dt لها كنص حتى ترجع التاريخ و الوقت الحالي المخزن في الكائن %c و تمرير الرمز strftime() هنا قمنا باستدعاء الدالة
print(de.strftime('%c'))
