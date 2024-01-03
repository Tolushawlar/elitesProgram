function verifyClaim(d, n){
    let numberDigits = d;
    let mulitplierCount = n;

    while(numberDigits >= 10)
}

function capitalizeEvenAndFirstChar(str) {
    // Split the string into an array of words
    let words = str.split(" ");
  
    // Iterate through each word
    for (let i = 0; i < words.length; i++) {
      let word = words[i].split("");
  
      // Capitalize even-indexed characters and the first character
      for (let j = 0; j < word.length; j++) {
        if (j % 2 === 0 || j === 0) {
          word[j] = word[j].toUpperCase();
        }
      }
  
      // Join the modified word back together
      words[i] = word.join("");
    }
  
    // Join the words back together to form the final string
    let result = words.join(" ");
  
    return result;
  }
  
  function capitalizeEvenAndFirstChar(inputedString) {
    // spliting the inputed string text into an array
    let inputedStringArray = inputedString.split(" ");
  
    // create a loop to go through the singular words in the inputed String array
    for (var i = 0; i < inputedStringArray.length; i++) {
      //spliting the singuler words in the array into each letter
      let stringLetter = inputedStringArray[i].split("");
  
      for (var j = 0; j < stringLetter.length; j++) {
        // targeting the index positioned 0 (first ) and even positioned letters
        if (j % 2 === 0 || j === 0) {
          stringLetter[j] = stringLetter[j].toUpperCase();
        }
      }
  
      //joined the transformed letters together
      inputedStringArray[i] = stringLetter.join("");
    }
    //joined the transformed words together and return
    return inputedStringArray.join(" ");
  }
  

  function verifyClaim(d, n) {
    let inputedNumber = d;
    let multiplerCount = 0;
  
    if (inputedNumber >= 10) {
      while (inputedNumber >= 10) {
        let digits = inputedNumber.toString().split("").map(Number);
        inputedNumber = digits.reduce((a, b) => a * b);
        multiplerCount++;
      }
    } else {
      multiplerCount = 1;
    }
  
    return multiplerCount === n;
  }
  
  console.log(verifyClaim(29 , 2));
  