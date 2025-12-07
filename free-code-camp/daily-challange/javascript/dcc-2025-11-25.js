function fizzBuzz(n) {

const list = [];

for (let l=1; l<=n; l++) {
  let output = l;
  if (l%15 === 0){
    output = "FizzBuzz";
  }
  else if (l%5 === 0){
    output = "Buzz";
  }
    else if (l%3 === 0){
    output = "Fizz";
  }
  list.push(output);
}
  return list;
}
console.log(fizzBuzz(50))

