# Ionic Notes

## Project Structure
- Uses a typical *Cordova* project structure.
- `src/index.html` is the main entry point for the app (actual purpose is to set up scrip and css includes, bootstrap or run app)
- looks for the <ion-app> tag in the HTML
- `./src/` Inside the src directory is where the raw, uncompiled code is. (where most of the work for an ionic app will take place.)
- when running `ionic serve` the code inside of `src` is transpiled into ES5
- *src/app/app.module.ts* is the entry point for the app
    

near the top of `src/app/app.module.ts` should see this block of code.
```typescript
@NgModule({
  declarations: [MyApp,HelloIonicPage, ItemDetailsPage, ListPage],
  imports: [ BrowserModule, IonicModule.forRoot(MyApp)],
  bootstrap: [IonicApp],
  entryComponents: [MyApp,HelloIonicPage,ItemDetailsPage,ListPage],
  providers: []
})
export class AppModule {}
```

- The root module of the app essentially controls the rest of the application.
- Similar to ng-app from Ionic and Angular 1.
- Also where we bootstrap our app using ionicBootstrap (doesn't seem important yet)
- In this module `src/app/app.module.ts`, we're setting the root component to MyApp in `src/app/app.component.ts`.
- This is the first component that gets loaded in our app, and typically it's an empty shell for other components to be loaded into.
- in `app.components.ts`, we're setting our template to `src/app/app.html`
*main template for the app goes in* `src/app/app.html`

```html
<ion-nav id="nav" [root]="rootPage" #nav swipeBackEnabled="false"></ion-nav>

<ion-menu [content]="nav">

  <ion-header>
    <ion-toolbar>
      <ion-title>Pages</ion-title>
    </ion-toolbar>
  </ion-header>

  <ion-content>
    <ion-list>
      <button ion-item *ngFor="let p of pages" (click)="openPage(p)">
        {{p.title}}
      </button>
    </ion-list>
  </ion-content>

</ion-menu>
```

- In this template we set up an `ion-menu` to function as a side menu, and then an `ion-nav` component to act as the main content area.
- The `ion-menu`'s `content` property is bound to the local variable `nav` from our `ion-nav`, so it knows where it should animate around.

# Angular Notes

- Angular applications are made up of components.
- **Component** - the combination of an HTML template and a component class that controls a portion of the screen.
*Example of a component class that displays a simple string*
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}</h1>`
})
export class AppComponent { name = 'Angular'; }
```

- Every component begins with an `@Component` *decorator* function that takes a *metadata* object.
- The metadata object describes how the HTML template and the compon
- the **selector** property tells Angular to display the component inside a custom **<my-app>** tag in `index.html`
index.html
```html
<my-app>Loading AppComponent content here ...</my-app>
```
- The **template** property defines a message inside an `<h1>` header.
- The message starts with "Hello" and ends with `{{name}}`, which is an angular [Interpolation Binding](https://angular.io/docs/ts/latest/guide/displaying-data.html) expression.
- At runtime, Angular replaces `{{name}}` with the value of the component's `name` property. **Interpolation Binding** is a fancy word.

However, you don't call **new** to create an instance of the `AppComponent` class. Angular does that for you. And this is how.
- the CSS `selector` in the `@Component` decorator specifies an element named `<my-app>`. That element is a placeholder in the body of your `index.html` file
```html
<body>
  <my-app>loading...</my-app>
</body>
```


# Dependency Injection
I've never felt like I've properly understood this
**Dependency Injection** - is an important application design pattern. Angular has its own dependency injection framework and you really ccan'y build an Angular application without it. It's used so widely that almost everyone just calls it *DI* (just so you don't feel left out).

## Why dependency injection?
To understand why dependency injection is so important, consider an example without it.
```typescript
export class Car {
  public engine: Engine;
  public tires: Tires;
  public description = 'No DI';
  constructor() {
    this.engine = new Engine();
    this.tires = new Tires();
  }
  // Method using the engine and tires
  drive() {
    return `${this.description} car with ` +
      `${this.engine.cylinders} cylinders and ${this.tires.make} tires.`;
  }
}
```
The `Car` class creates everything it needs inside its constructor. What's the problem? The problem is that the `Car` class is brittle, inflexible, and hard to test.

This `Car` needs an engine and tires. Instead of asking for them, the `Car` constructor instantiates its own copies from the very specific classes `Engine` and `Tires`.

What if the `Engine` class evolces and its constructor requires a parameter? That would break the `Car` class and it would stay broken until you reqrote it along the lines of `this.engine = new Engine(theNewParameter)` The `Engine` constructor parameters weren't even a consideration when you first wrote `Car`. You may not anticipate them even now. But you'll have to start caring becase when the definition of `Engine`Changes, the `Car` class must change. That makes`Car` brittle.

excerpt with DI
```typescript
public description = 'DI'

constructor(public engine: Engine, public tires: Tires){ }
```

excerpt without DI
```typescript
public engine: Engine;
public tires: Tires;
public description = 'No DI';

constructor() {
  this.engine = new Engine();
  this.tires = new Tires();
}
```
The definition of the dependencies are now in the constructor. The `Car` class no longer creates an `engine` or `tires`. It just consumes them.

Now you can create a car by passing the engine and tires to the constructor.
```typescript
// Simple car with 4 cylinders and Flintstone tires.
let car = new Car(new Engine(), new Tires());
```
The definition of the engine and tire dependencies are decoupled from the `Car` class. You can pass in any kind of `engine` or `tires` you like, as long as they conform to the general API requirements of an `engine` or `tires`.

If someone extends the `Engine` class, that is not `Car`'s problem.
*The consumer of `Car` has the problem. The consumer must update the car creation code to something like this:*
```typescript
class Engine2 {
  constructor(public cylinders: number) { }
}
// Super car with 12 cylinders and FLintstone tires.
let bigCylinders = 12;
let ccar = new Car(new Engine2(bigCylinders), new Tires());
```
The critical point is this: the `Car` class did not have to change. You'll take care of the consumer's problem shortly.

The `Car` class is much easier to test now because you are in complete control of its dependencied. You can pass mocks to the constructor that do exactttly what you want them to do during each test:

```typescript
class MockEngine extends Engine{ cylinders = 8; }
class MockTires extends Tires { make = 'YokoGoodStone'; }

// Test car with 8 cylinders and YokoGoodStone tires.
let car = new Car(new MockEngine(), new MockTires());
```
**That's what dependency injection is. Yay!**
It's a coding patter in which a class received its dependencies from external sources rather than creating them itself.

But what about the poor consumer? Anyone who wants a `Car` must now create all thress parts: the `Car`, `Engine`, and `Tires`. The `Car` class shed its problems at the consumer's expense. You need something that takes care of assembling these parts.
You *could* write a giant class to do that:

```typescript
import { Engine, Tires, Care } fromm './car';

// BAD pattern!
export class CarFactory {
  createCar() {
    let car = new Car(this.createEngine(), this.createTires());
    car.description = 'Factory';
    return car;
  }

  createEngine() {
    return new Engine();
  }

  createTires() {
    return new Tires();
  }
}
```
Not so bad with only three creation methods. But maintaining it will be hairy as the application grows. This factory is coing to become a huge spiderweb of interdependent factory methods!

Wouldn't it be nice if you could simply list the things you want to build without having to define which dependency gets injected into what?

This si where the dependency injection framework comes into play. Imagine the framework had something called an injector. You register some classes with this injector, and it figures out how to create them.

When you need a `Car`, you simply ask the injector to get it for you and you're good to go.

```typescript
let car = injector.get(Car)
```
Everyone wind. The `Car` knows nothing about creating an `Engine` or `Tires`. The consumer knows nothing about creating a `Car`. You don't have a gigantic factory class to maintain. Both `Car` and consumer simply ask for what they need and the injector delivers.

This is what a *dependency injection framework*  is all about.

# Angular Dependency Injection
Angular ships with its own dependency injection framework. This fraework can also be used as a standalone module by other applications and frameworks.

To see what it can do when building components in Angular, start with a simplified version of the `HeroesComponent` that from [The Tour of Heroes](https://angular.io/docs/ts/latest/tutorial/).

## Angular Injectable Decorator

**What it Does** - A marker metadata that marks a class as available to *Injector* for creation.
**How to use** - `@Injectable() class Car { }`

**Example:**
```typescript
@Injectable()
class UsefulService {
}

@Injectable()
class NeedsService {
  constructor(public service: UsefulService) { }
}

const injector = ReflectiveInjector.resolveAndCreate([NeedsService, UsefulService]);
expect(injector.get(NeedsService).service instanceof UsefulService).toBe(true);
```

`Injector` will throw `NoAnnotationError` when trying to instantiate a class that does not have @Injectable marker, as shown in the example below.

```typescript
class UserfulService {}

class NeedsService {
  constructor(public service: UsefulService) {}
}

expect(() => ReflectiveInjector.resolveAndCreate([NeedsService, UsefulService])).toThrow();
```

