# Property Based Testing
@BILLLABOON
Bill Laboon

## What is testing?
Checking observed behaviour 
against observed behavior
under certain circumstances

Lots of time will be spent writing test boilerplate

Cou;d check properties

First determine:
- The properties of values to be passed in
- the expected properties of the return value, given that input

Then let the computer come up with test cases for us

## Expeted Properties vs observed properties

- note that properties are a subset of "behaviour"
- in traditional testing, our expected be haviour would be listed as specific expected values...
	- but this is not necessary to meet our definition of "testing"
	- even if it is what we commonly think of as "testing"

- stochastic testing(using randomly or pseudorandomly generated values for testing)
- popular in functional programming

1. specify the propertied of the allowed input
2. specift the properties of the output that should always hold

outpu properties of sorting function
1. output array same saize as passed in array
2. values in output array always increasing or staying the same
3. value in output array never decreasing
4. every element in input array is in output array
5. no element not in input array is in output array
6. idempotent = running it again should not change output array
7 running twice should always result in the same output array

## Falsifying an invariant
When a test fails

**Shrinking** when the testing framework tries to reduce the number of elements in the inputs to find the smalled number of elements that still fails

helps track down actual issue

## Generators
- Inpu may be more complex than just list of random ints
- example: user object with various attributes
- Genrators allow you to specify rules for what kinds of input will be generated
**Examples**
- for an absolute value function, only pass in negative numbers for a test
- generating complex objects e/g/ various user objects with some values null, some strings containing strange unicode, some containing invalid data etc.
- Generate input with more complex restrictions(only prime numbers

## Not just for methods and unit testing
**System Testing Level**
- Check if random input to system causes issues
- check if nonexistent user names when loggong in get andy screen other nan invalid user
- check if users posting a message can cause issues
**Fuzzung (Fuzz testing) pass in generated values, see if system crashes**
- kind of property-based testing with one invariant, "system keeps running normally"

**More useful for **
- mathemetical functions
- pure functions
- well-specified problems
- anything where a variety of inuts map to specific kinds of outut

**less useful for((
1. writing to a file
2. communitcating over a network
3. displaying text of graphics
4. subjective testing(user acceptance)
5. impure functions in general

*ways around it would be mocks*

also, non-deterministic/multithreaded testing sucks

**General Benefits**
- easy to run hunderds, thousands, or even millions of tests
- can do so quickly, if tests are properly specified
- avoids human bias
- humands may inadvertently only select happy path tests or ignore specific edge cases
- works well if invariants if specified correctly

**Generad Drawbacks**
takes time and effort to correctly speficy properties of input and output
- if not done correctly, may cause false positives or miss defects
Due to reliance on randomness, may only find defects on some runs
- intermittent, non=deterministic failures
human bias is sometimes a good thing
- a good tester may knoe where to productively focus their effort

github.com/laboon/pghqa-talk
