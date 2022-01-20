# 元类(Metaclasses)是什么？
# 元类让你来定义某些类是如何被创建的，
# 从根本上说，赋予你如何创建类的控制权。(你甚至不用去想类实例层面的东西。)
# 从根本上说，你可以把元类想成是一个类中类，或是一个类，它的实例是其它的类。实际上，
# 当你创建一个新类时，你就是在使用默认的元类，它是一个类型对象。(对传统的类来说，它们的元
# 类是 types.ClassType.)当某个类调用 type()函数时，你就会看到它到底是谁的实例：

"""
    什么时候使用元类?
    元类一般用于创建类。在执行类定义时，解释器必须要知道这个类的正确的元类。解释器会先
寻找类属性__metaclass__，如果此属性存在，就将这个属性赋值给此类作为它的元类。如果此属性
没有定义，它会向上查找父类中的__metaclass__. 所有新风格的类如果没有任何父类，会从对象或
类型中继承。(type (object) 当然是类型).
    如果还没有发现__metaclass__属性，解释器会检查名字为__metaclass__的全局变量，如果它
存在，就使用它作为元类。否则, 这个类就是一个传统类，并用 types.ClassType 作为此类的元类。
(注意：在这里你可以运用一些技巧... 如果你定义了一个传统类，并且设置它的__metaclass__ =
type，其实你是在将它升级为一个新风格的类!)
"""
