from random import sample

class Quiz(object):
    """Quiz yourself on terms entered with definitions into dictionary ."""
    def __init__(self, terms):
        self.terms = terms
        self.keys = self.terms.keys()

    def quiz_base(self, which1, which2, which3):
        print "What's {0}?".format(which1)
        self.answer = raw_input("> ")
        if self.answer == which2:
            print "Yup!"
        else:
            print "Nope, it's {0}!".format(which3)

    def quiz_terms(self):
        self.index = sample(xrange(0,len(self.terms)), len(self.terms))
        for x in self.index:
            self.quiz_base(self.terms[self.keys[x]], self.keys[x], self.keys[x])

    def quiz_defs(self):
        self.index = sample(xrange(0,len(self.terms)), len(self.terms))
        for x in self.index:
            self.quiz_base(self.keys[x], self.terms[self.keys[x]], self.terms[self.keys[x]])

terms1 = {
    "class": "make new type of thing",
    "object": "most basic type of thing, or instance of thing",
    "instance": "what you get when you create class",
    "def": "how to define function in class",
    "self": "inside class functions, variable for instance/object being accessed",
    "inheritance": "one class inherits traits from another",
    "composition": "classes can be composed of other classes, i.e. car has wheels",
    "attribute": "property given to class from composition, usually variables",
    "is-a": "something inherits some something else, i.e. salmon is-a fish",
    "has-a": "something is composed of other things or has trait, i.e. salmon has-a mouth"
}

terms2 = {
    "class x(y)": "make a class named x that is-a y",
    "class x(object): def __init__(self, j)": "class x has-a __init__ that takes self and j parameters",
    "class x(object): def m(self, j)": "class x has-a function named m that takes self and j parameters",
    "foo = x()": "set foo equal to instance of class x",
    "foo.m(j)": "from foo get m function and call it with parameters self and j",
    "foo.k = q": "from foo get k attribute and set it equal to q"
}
