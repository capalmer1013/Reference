# Typescript Notes

variables begin with letter, $, or _


```typescript
var myName: string = "Chris";
var myAge: number = 25;
var canVode: boolean = true;
var anything: any = "dog";
anything = 2;
```


example html:
```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
    </head>
    
    <body>
        <p id="tsStuff"></p>
        
        <script src="tstut.js"></script>
    </body>
</html>
```

tstut
```typescript
document.getElementById("tsStuff")
    .innerHTML = "Hello"

document.write("myname is a " + typeof(myName) + "<br />");
```
