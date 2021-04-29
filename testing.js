// I know the technical challenge prompt requires testing, but I'm not sure how to write tests for 
// a web app.  While I'm looking that up, here are some basic assert equals tests to show that
// I understand the concept of testing.  


function square(n) {
    return n * n;
  }
  
  function assertEqual(actual, expected, testName) {
   
    if (actual === expected) {
        console.log('passed'); 
    } else {
    console.log('FAILED [' + testName + '] Expected "' + expected + '", but got "' + actual + '"')
  }
  }

  // Test cases
  let output1 = square(2)
  //should be 4
  let output2 = square(-3)
  //should be 9
  assertEqual(output1, 4, "Square positive number")
  assertEqual(output2, 9, "Square negative number")



function every(array, callbackFunction) {
    var doesEveryElementMatch = true;
    for (var i = 0; i < array.length; i++) {
      doesEveryElementMatch = callbackFunction(array[i]);
      if (doesEveryElementMatch === false) {
        return false;
      }
    }
    return doesEveryElementMatch;
  }
  
  function assertEqual(actual, expected, testName) {
      if (actual === expected) {
          console.log("PASSED");
      } else {
          console.log(`FAILED [${testName}] expected ${expected} but got ${actual}`);
      }
  }
  // Test cases
  function isGreaterThan10(element) {
      return element > 10;
  }
  var testArray = [11, 12, 13]
  assertEqual(every(testArray, isGreaterThan10), true, 'greater than 10 output')
  assertEqual(every([8, 9, 11], isGreaterThan10), false, 'less than 10 output')
  assertEqual(every([10], isGreaterThan10), false, '10 output')
  assertEqual(every([8, 9], isGreaterThan10), false, 'less than 10 output pt 2')
  assertEqual(every([11,12,13,10,15], isGreaterThan10), false, '10 in the middle')
  assertEqual(every([-12, 12], isGreaterThan10), false, 'negative numbers')
  assertEqual(every([10.5, 13.24], isGreaterThan10), true, 'decimal numbers')