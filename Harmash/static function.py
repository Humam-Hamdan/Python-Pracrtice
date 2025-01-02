
# StaticExample هنا قمنا بتعريف الكلاس
class StaticExample:
    # هنا قمنا بتعريف دالة ثابتة في الكلاس عند إستدعاءها تقوم بطباعة جملة عادية فقط
    @staticmethod
    def print_msg():
        print("Static method can be called directly from the class.")


# بدون الحاجة لإنشاء كائن منه StaticExample بشكل مباشر من الكلاس print_msg() هنا قمنا باستدعاء الدالة الثابتة
StaticExample.print_msg()

'''..........................................'''

# Session هنا قمنا بتعريف الكلاس
class Session:
    # هنا قمنا بوضع 4 متغيرات ( أي خصائص ) في الكلاس
    title = 'Python for beginners'
    language = 'English'
    teacher = 'Sara Smith'
    credits = 5
    # هنا قمنا بتعريف دالة ثابتة في الكلاس عند إستدعاءها تقوم بطباعة قيم الخصائص بشكل مرتب
    # لاحظ أنك مجبر على وضع إسم الكلاس ثم نقطة ثم إسم المتغير الذي تريد الوصول إليه من داخل الدالة
    @staticmethod
    def print_info():
        print('Title:', Session.title)
        print('Language:', Session.language)
        print('Teacher:', Session.teacher)
        print('Credits Number:', Session.credits)


# Session مباشرةً من الكلاس print_info() هنا قمنا باستدعاء الدالة الثابتة
Session.print_info()

'''..........................................'''

# MyTools هنا قمنا بتعريف الكلاس
class MyTools:
    # و تحتوي على باراميتر واحد print_words_count هنا قمنا بتعريف دالة ثابتة إسمها
    @staticmethod
    def print_words_count(val):
        # هنا قلنا إذا كانت القيمة التي مررناها لها عبارة عن قيمة نصية
        if isinstance(val, str):
            # إذا كانت هذه القيمة النصية عبارة عن نص فارغ سيتم طباعة أن النص عبارة عن نص فارغ و أن عدد الكلمات فيه هو صفر
            if val == '':
                print('Empty string, so number of words is 0')
            # و من ثم طباعة قيمته words_count إذا لم تكن هذه القيمة النصية عبارة عن نص فارغ سيتم تخزين عدد الكلمات الموجودة فيه في المتغير
            else:
                words_count = len(val.split())
                print('Number of words is:', words_count)
        # عبارة عن قيمة نصية سيتم طباعة الجملة التالية val إذا لم تكن قيمة الباراميتر
        else:
            print('Oops..', val, 'is not a string!')


# هنا قمنا بتعريف متغير نصي يحتوي على مجموعة كلمات
text = 'Today, you are studying static methods.'
# text لمعرفة عدد الكلمات الموجودة في المتغير MyTools من الكلاس print_words_count() هنا قمنا باستدعاء الدالة الثابتة
MyTools.print_words_count(text)

'''..........................................'''

# StaticExample هنا قمنا بتعريف الكلاس
class StaticExample:
    # هنا قمنا بتعريف متغير ( أي خاصية ) في الكلاس و حددنا أن قيمته تساوي 5
    x = 5
    # الموجود مباشرةُ في الكلاس و ليس في كائن منه x تعرض قيمة المتغير print_x هنا قمنا بتعريف دالة ثابتة إسمها
    @staticmethod
    def print_x():
        print('StaticExample.x =', StaticExample.x)


# obj إسمه StaticExample هنا قمنا بإنشاء كائن من الكلاس
obj = StaticExample()
# من 5 إلى 10 obj الخاصة بالكائن x هنا قمنا بتغيير قيمة
obj.x = 10
# الخاصة بالكائن و التي تساوي 10 x الخاصة بالكلاس, أي 5 و ليس قيمة x لاحظ أن سيتم طباعة قيمة .obj من الكائن print_x() هنا قمنا باستدعاء الدالة الثابتة
obj.print_x()
 
# الخاصة بالكلاس x بشكل مباشر و بالتالي سيتم أيضاً طباعة قيمة StaticExample من الكلاس print_x() هنا قمنا باستدعاء الدالة الثابتة
StaticExample.print_x()    # الخاصة بالكلاس لأننا نستدعي الدالة الثابتة مباشرةً من الكلاس 
# print_x() هي إستدعاءها منه كالتالي و ليس عن طريق الدالة الثابتة obj الخاصة بالكائن x الطريقة الوحيدة لطباعة قيمة
print('obj.x =', obj.x)
