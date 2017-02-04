# Object-Oriented Programming

---

## Terminology
- **Objects and Methods** - An object is an encapsulation of data together with procedures that manipulate the data and functions that return information about the data. The procedures and functions are both called methods.

- **Encapsulation** - Mechanisms that allow each object to have its own data and methods.
- **Messages and Receivers** - using method calls to interact with the data encapsulated inside an instance of an object.
- **Polymorphism** - the capability of having methods with the same names and parameter typed exhibit different behavior depending on the receiver. i.e. You can send the same message to two different objects and they can respond in different ways.
- **Overloading** - Generally, the capability of using names to mean different things in different contexts.
- **Members** - Objects can have their own data, including variables and constants, and their own methods. The variables, constants, and methods associates with an object are collectively refered to as its *members* or *features*.
- **Class** - A category of objects, classified according to the members that they have.
- **Class Members and Instance Members** - A class can hold data variable and constatns that are shared by all of its objects and can handle methods that deal with an entire class rather than an individual object. These are called *class members* or sometimes *static members*. The members associated with objects are called *instance members*.
- **Inheritance** - The capability of defining a new class of objects that inherits from a parent class. New data elements and methods can be added to the new class, but the data elements and methods of the parent class are available for objects in the new class without rewriting their declarations.
- **Dynamic Dispatch** - the process of selecting which implementation of a polymorphic operation to call at run time.
- **Abstract Class** - (Java) a class that is declared abstract (may or may not include abstract methods) Abstract classes cannot be instantiated, but they can be subclassed.
- **Abstract Method** - A method that is declared without an implementation.
- **Virtual Method/ Function** - An inheritable and overridable function or method for which dynamic dispatch is facilitated.

- **Difference between Virtual/Abstract Methods** - Virtual methods have an implementation and provide the derived class the option of overriding it. Abstract methods do not probide an implementation and force the derived classes to override the method.


### Sources
[link](https://www.d.umn.edu/~gshute/softeng/object-oriented.html)
