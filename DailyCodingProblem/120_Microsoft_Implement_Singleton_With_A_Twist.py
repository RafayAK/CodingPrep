"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
return the second instance.
"""

class TwistedSingleton:
    _instances = dict()
    even_call = False

    def __init__(self, instance_num):
        self.instance_num = instance_num

    @staticmethod
    def initialize():
        print("Initialized")
        TwistedSingleton._instances[0] = TwistedSingleton(1)
        TwistedSingleton._instances[1] = TwistedSingleton(2)

    @staticmethod
    def getInstance():
        if len(TwistedSingleton._instances) == 0:
            TwistedSingleton.initialize()

        if TwistedSingleton.even_call:
            TwistedSingleton.even_call = False
            return TwistedSingleton._instances[1]
        else:
            TwistedSingleton.even_call = True
            return TwistedSingleton._instances[0]


if __name__ == "__main__":
    a1 = TwistedSingleton.getInstance()
    print(a1.instance_num)

    a2 = TwistedSingleton.getInstance()
    print(a2.instance_num)

    a3 = TwistedSingleton.getInstance()
    print(a3.instance_num)

    a4 = TwistedSingleton.getInstance()
    print(a4.instance_num)

