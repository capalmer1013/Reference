# Angular 2 stuff
## What are observables
**Observables** are like **promises** but better. Super helpful.

### Observables
- handle multiple values over time
- are cancellable

### Promise
- only called once and will return a single value
- are not cancellable

Because observables can handle multiple values over time, they are good candidates for working with real-time data, events any sort of stream.

Being able to cancel observables gives better control when working with in-flow of values from a stream. The common example is the auto-complete widget which sends a request for every key-stroke.


