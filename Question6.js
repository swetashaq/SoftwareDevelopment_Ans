//Question 6: Reversing a String in JavaScript

function reverseString(str) {
  //defining new function
  return str.split("").reverse().join(""); //built-in Javascript function
}
let reversed = reverseString("Hello, World!"); //The string to be reversed
console.log(reversed); //Prints the reversed string
