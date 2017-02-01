# C++ notes
---
## Pointers
- **Address-of Operator (&)** - preceding the name of a variable with an ampersand (&) returns the address of the variable.
```c++
foo = &myvar;
```
This assigns the address of variable *myvar* to *foo*; by preceding the name of the variable *myvar* with the *address-of operator* (&). This assigns the address of the variable instead of the value.
```c++
myvar = 25;
foo = &myvar;
bar = myvar;
```
stores address in foo
stores 25 in bar

- **Dereference Operator(*)** - preceding a pointer with the *dereference operator(*)*

```c++
baz = *foo;
```
Read as "*baz* equal to value pointed to by *foo*". Assigns 25 to baz.

**The reference and dereference operators are compementary:**
- & is the *address-of operator*, and can be read simply as "address of"
- * is the *dereference operator*, and can be read as "value pointed to by"

**Declaring Pointers**
```c++
type *name;
// examples
int *number;
char *character;
double *decimals;
```

[source](http://www.cplusplus.com/doc/tutorial/pointers/)
