1. [[#Extract Function]]
2. [[#Inline Function]]
3. [[#Extract Variable]]
4. [[#Inline Variable]]
5. [[#Change Function Declaration]]

## Extract Function

```javascript
function printOwing(invoice){
	printBanner();
	let outstanding = calculateOutstanding();
	
	// print details
	console.log(`name:${invoice.customer}`);
	console.log(`amount:${outstanding}`);
}
```

==After Refactoring==
```javascript
function printOwning(invoice){
	printBanner();
	let outstanding = calculateOutstanding();
	printDetails(outstanding);	
}

function printDetails(outstanding){
	console.log(`name:${invoice.customer}`);
	console.log(`amount:${outstanding}`);
}
```

Look at the fragment of code, understand what it is doing, then extract it into its own function named after its purpose.

---

## Inline Function

```javascript
function getRating(driver){
	return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver){
	return driver.numberOfLateDeliveries > 5;
}
```

==After Refactoring==
```javascript
function getRating(driver){
	return (driver.numberOfLateDeliveries > 5) ? 2: 1 ;
}
```

- Sometimes the body of the function is more clear than the name of the function.
- Also common theme which we want is short Function names
- I commonly use Inline Function when I see code that's using too much indirection - when it seems that every function does simple delegation to another function, and I get lost in all the delegation.

---

## Extract Variable

```javascript
return order.quantity * order.itemPrice -
	Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
	Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

==After Refactoring==

```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping =  Math.min(basePrice*0.1, 100);
return basePrice - quanitityDiscount + shipping;
```

- Long expressions can be very complex and in such situations, local variables may help break the expression down into something more manageable.
- I consider Extract Variable when i want to a name to an expression in my code.
- If the new variable is needed in more places than I'll make it available as a function.

---

## Inline Variable
```javascript
let basePrice = anOrder.basePrice;
return (basePrice>100);
```

==After Refactoring==
```Javascript
return (anOrder.basePrice > 100);
```

The expression is more readable than the variable name. 🤷‍♂️

---

## Change Function Declaration
























