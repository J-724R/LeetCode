const numArray = [1, 3, 5 ,7, 15]

function containsDup(numArray: number[]): boolean{
  let duplicated = false
  
  numArray.forEach( num => {
    let count = 0
    numArray.forEach(element => {
      if(num == element) count++
      if(count >= 2){
        duplicated = true
        return
      }
    });
  });

  return duplicated
}

console.log(containsDup(numArray));
