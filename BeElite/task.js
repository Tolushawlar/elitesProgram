function verifyClaim(d, n) {
  let inputedNumber = d;
  let multiplerCount = 0;

  if (inputedNumber >= 10) {
    // running the inputedNumber split  while it contain 2 numbers
    while (inputedNumber >= 10) {
      // chained function for converting inputedNumber to string, then split and storing in an array as number.
      let digits = inputedNumber.toString().split("").map(Number);
      // using the javascript reduce method to calculate the accumulated product of the array.
      inputedNumber = digits.reduce((a, b) => a * b);
      multiplerCount++;
    }
  } else {
    multiplerCount = 0;
  }
  // using booloen comparison to check value of n
  return multiplerCount === n;
}

console.log(verifyClaim(22, 1));
// Test case verifyClaim(39,4) is false, because the right answer is 3 and not 4

/* DOCUMENTATION USED
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
*/



function capitalizeEvenAndFirstChar(inputedString) {
  // spliting the inputed string text into an array
  let inputedStringArray = inputedString.split(" ");

  // create a loop to go through each words in the inputed String array.
  for (var i = 0; i < inputedStringArray.length; i++) {
    //spliting each words in the array into each letter.
    let stringLetter = inputedStringArray[i].split("");

    for (var j = 0; j < stringLetter.length; j++) {
      // targeting the index positioned 0 (first ) and even index positioned letters.
      if (j % 2 > 0 || j === 0) {
        stringLetter[j] = stringLetter[j].toUpperCase();
      }
    }

    //join the transformed letters together.
    inputedStringArray[i] = stringLetter.join("");
  }
  //join the transformed words together and return.
  return inputedStringArray.join(" ");
}

console.log(capitalizeEvenAndFirstChar("you are a good person"));

/*
DOCUMENTATION USED
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
*/
