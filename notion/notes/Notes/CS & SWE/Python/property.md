# property

[https://realpython.com/python-property/](https://realpython.com/python-property/)

Say you’re working on a `Circle` class. The initial implementation has a single attribute called `.radius`. You finish coding the class and make it available to your end users. They start using `Circle` in their code to create a lot of awesome projects and applications. Good job!

Now suppose that you have an important user that comes to you with a new requirement. They don’t want `Circle` to store the radius any longer. They need a public `.diameter` attribute.

At this point, removing `.radius` to start using `.diameter` could break the code of some of your end users. You need to manage this situation in a way other than removing `.radius`.

Programming languages such as [Java](https://realpython.com/oop-in-python-vs-java/) and [C++](https://en.wikipedia.org/wiki/C%2B%2B) encourage you to never expose your attributes to avoid this kind of problem. Instead, you should provide [getter and setter](https://realpython.com/python-getter-setter/) methods, also known as [accessors](https://en.wikipedia.org/wiki/Accessor_method) and [mutators](https://en.wikipedia.org/wiki/Mutator_method), respectively. These methods offer a way to change the internal implementation of your attributes without changing your public API.

**Note:** Getter and setter methods are often considered an [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) and a signal of poor object-oriented design. The main argument behind this proposition is that these methods break [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)). They allow you to access and mutate the components of your objects.

[Properties](https://en.wikipedia.org/wiki/Property_(programming)) represent an intermediate functionality between a plain attribute (or field) and a method. In other words, they allow you to create methods that behave like attributes. With properties, you can change how you compute the target attribute whenever you need to do so.

[https://realpython.com/python-api/](https://realpython.com/python-api/)