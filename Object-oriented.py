"""
有一个“中国人”类
1. 中国人的国籍是中国，并且有姓名和年龄，所以把这些设为【类属性】，但年龄对于一些人来说比较特殊，所以设为【私有属性】
2. 有一群人的户籍是"江西"，但是不是所有中国人的户籍地都是江西，所以把户籍设为【实例属性】，类调用的话会报错
2. 人都需要吃和睡，这个行为跟你叫什么，年龄多大，是不是中国人（不需要用到类的属性），以及和你是谁没有关系（不需要实例化类），所以把这些行为设为【静态方法】
3. 当别人询问国籍时，你需要做出回答，这是会用到类属性，所有把"回答"这个行动设为【类方法】
4. 有些人喜欢看书，但是这只跟个人习惯相关，所以把"看书"这个行动设为【实例方法】
"""


# 一个person类
class Person(object):
    # 类属性，
    country = "中国"
    name = '中国人'  # 类属性(公有)
    # 只能在类里被使用
    __age = 0  # 类属性（私有）

    def __init__(self, name, age):
        # 实例属性  通过类对象调用实例属性会报错，只能实例调用
        self.address = "江西"
        # 在类中调用类属性
        self.name = name
        self.__age = age
        print("我叫{0}，今年{1}岁".format(self.name, self.__age))

    # 静态方法类似普通方法，参数里面不用self。
    # 这些方法和类相关，但是又不需要类和实例中的任何信息、属性等等。
    # 如果把这些方法写到类外面，这样就把和类相关的代码分散到类外，使得之后对于代码的理解和维护都是巨大的障碍。而静态方法就是用来解决这一类问题的。
    @staticmethod
    def eat():       
        print("吃东西")

    @staticmethod
    def sleep():
        print("睡觉")

    # 类方法  当我们需要和类直接进行交互，而不需要和实例进行交互时，类方法是最好的选择。
    # 类方法与实例方法类似，但是传递的不是类的实例，而是类本身，第一个参数是cls。我们可以用类的实例调用类方法，也可以直接用类名来调用。
    @classmethod
    def answer(cls):
        print("我是{0}人".format(cls.country))

    # 实例方法  第一个参数是self，我们需要有一个类的实例，才可以调用这个函数。
    def read(self):
        print("{0}爱看书".format(self.name))


if __name__ == "__main__":
    # 类调用类属性（正确）
    print(Person.name)
    # 类调用类的私有属性(报错)
    # print(Person.__age)
    # 类调用类方法(正确)
    Person.answer()
    # 实例化一个中国人,姓名叫zero,年龄是18
    p1 = Person("zero", "18")
    # 实例化对象调用类属性和实例属性（正确）
    print("{0}的户籍是{1}".format(p1.name, p1.address))
    # 类调用实例属性(报错)
    # print(Person.address)
    # 实例化对象调用类方法(正确)
    # 江西人也是中国人
    p1.answer()
    # 实例对象改变类属性和实例属性(成功)
    # zero移民到了美国
    p1.country = "America"
    p1.address = "New York"
    print("{0}现在的国籍是{1}，户籍是{2}".format(p1.name, p1.country, p1.address))
    # 但他本质还是中国人
    p1.answer()

    # 实例化对象调用实例方法(成功)
    # 一个叫lisa的24岁江西人喜欢看书
    p2 = Person("lisa", "24")
    p2.read()

    # 类调用实例方法(报错)
    # Person.read()



