## Benefits of Typescript over Javascript
1. Static Typing (most imp feature)
2. Code Completion
3. Refactoring
4. Shorthand notations

```Code 
Statically-Typed (C++, C#, Java)
int number = 10;
number = "a"; // Error

Dynamically Typed (Javascript, Python and Ruby)
let number = 10;
number = "a"; // Works

```

TypeScript is `Javascript with Type checking` 

![[Pasted image 20260504205105.png]]

## Install Typescript Compiler
```Powershell
npm i -g typescript 
```

```Typescript title="demo.ts"
let age: number = 10;
```
## To compile a typescript File
```Powershell
tsc demo.ts
```

---

## Configuring the Typescript Compiler
```Powershell
tsc --init // this will create a 'tsconfig.json'
```

## Debugging Typescript in VS Code.
==TODO==

## Data types in JS and TS
JS types 
1. number
2. string
3. boolean
4. null
5. undefined
6. object

Typescript types
1. any
2. unknown
3. never
4. enum
5. tuple

```Typescript 
let sales: number = 123_999 ;
let course : string = "hello";
let is_published: boolean = true;

let level; // typescript assumes its of type 'any' but for best practices avoid using it coz it goes back to JS only

// Array
let numbers: number[] = [1,2,3];

// Tuples
let user:[number, string] = [1, 'Most'];

// Enums
const small = 1;
const medium = 2;
enum Size{Small = 20, Medium = 'T'};
let mySize: Size = Size.Medium;
console.log(mySize);

// funtions
function sum(a: number , b: number): number{
    return a+b;
}
let result: number = sum(20,20);
console.log(result);

// Objects
let employee: {
    id: number,
    name: string,
    readonly isEmployed : boolean // cant be modified
    retire: (date: Date) => void    // Object's method
} = {id : 1,
     name: 'Boss',
     isEmployed: true,
     retire: (date: Date) => {
            console.log ( date );
     }
    };

employee.id = 10;
employee.name = 'Junior';
//employee.isEmployed = false; // Error

// Type Alias
type Employee = {
    id: number,
    name: string,
    readonly isEmployed : boolean // cant be modified
    retire: (date: Date) => void    // Object's method
};

let employee: Employee = {id : 1,
     name: 'Boss',
     isEmployed: true,
     retire: (date: Date) => {
            console.log ( date );
     }
    };

employee.id = 10;
employee.name = 'Junior';
//employee.isEmployed = false; // Error

// Union Types - here i told typescript that the parameter 'a' can be 'number or string'.
function sum (a: number | string):number{
    return Number(a);
}

console.log(sum(10));
let var1 = sum(10);
console.log(typeof(var1));
console.log(sum('10'));

//

```
