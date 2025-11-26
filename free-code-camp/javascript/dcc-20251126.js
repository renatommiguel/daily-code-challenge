function isFizzBuzz(seq) {

const list = [];

for (let i=1; i<=seq.length;i++){
  if (i%15===0){
    let text = "FizzBuzz"
    list.push(text);
    if (seq[i-1]!=text){
      return false;
    }
  }
  else if (i%5===0){
    let text = "Buzz"
    list.push(text);
    if (seq[i-1]!=text){
      return false;
    }    }
    else if (i%3===0){
    let text = "Fizz"
    list.push(text);
    if (seq[i-1]!=text){
      return false;
    }
  }
  else{
    list.push(i);
    if (seq[i-1]!=i){
      return false;
    }
}
}
return true;
}

console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))