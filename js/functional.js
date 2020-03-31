//  var declarations are globally scoped or function scoped while let and const are block scoped. var variables can be updated and re-declared within its scope; let variables can be updated but not re-declared; const variables can neither be updated nor re-declared

const x = {
  val: 2  
};

const x1 = x => Object.assign({}, x, {val: x.val + 1});
const x2 = x => Object.assign({}, x, {val: x.val * 2})

console.log(x1(x2(x)).val);

const zeus = {}

// functions 

function Zeus(num1, num2) {
    return num1 * num2
}

console.log(Zeus(3,4))

// immutability  
// freeze object one level deep 
const a = Object.freeze({
    foo: 'Hello',
    bar: 'world',
    baz: '!'
});

a.foo = 'Goodbye'; // this will not work 
console.log(a); 

// However, if we go a level deeper, object is mutable
const b = Object.freeze({
  foo: { greeting: 'Hello' },
  bar: 'world',
  baz: '!'
});

b.foo.greeting = 'Goodbye';
console.log(`${ b.foo.greeting }, ${ b.bar }${b.baz}`);

// A higher order function is any function which takes a function as an argument, returns a function, or both
// mapping 
// => arrow used to make quick functions
var double = n => n * 2;
var doubleMap = numbers => numbers.map(double)
console.log(doubleMap([2, 3, 4]));
// map array of dictionaries
var double = n => n.points * 2;
var doubleMap = numbers => numbers.map(double);
var dictionary = [{'name': 'ball', 'points': 2}, {'name': 'coin', points: 3}, {'name': 'candy', 'points': 4}];
console.log(doubleMap(dictionary));

// imperative mapping - uses "statements" ie if, else
var doubleMap = numbers => {
  const doubled = [];
  for (let i=0; i < numbers.length; i++) {
      doubled.push(numbers[i] * 2);
  }
  return doubled;
};

console.log(doubleMap([2, 3, 4]))

// declarative function does same thing, but abstracts flow control using array.prototype.map() - uses expression 
var doubleMap = numbers => numbers.map(n => n * 2);
console.log(doubleMap([2, 3, 4])); // [4, 6, 8]

// REDUCE method -  reduces array single value
// subtract numbers in array, starting from left
var numbers = [175, 50, 25]
function myFunc(total, num) {
    return total - num;
}; 
console.log(numbers.reduce(myFunc));










