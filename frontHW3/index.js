// Part1
var arr = ["Banana", "Orange", "Apple", "Mango"]
function deleteByIndex(arr,ind)
{
    arr.splice(ind,1)
    return arr
}

arr = deleteByIndex(arr,2)

console.log(arr)

// Paraat2
function concatenation(args)
{
   
    let totalArr = []
    totalArr = totalArr.concat(...arguments)
    return totalArr.sort(function(a, b){return a-b});
      
}
let sortedArrays = concatenation([1,3,2],[4,6,7],[5,9,8])
console.log(sortedArrays)

//Part3

function flatten(input) {
    const stack = [...input];
    const res = [];
    while(stack.length) {
      // pop value from stack
      const next = stack.pop();
      if(Array.isArray(next)) {
        // push back array items, won't modify the original input
        stack.push(...next);
      } else {
        res.push(next);
      }
    }
    // reverse to restore input order
    return res.reverse();
  }
  
  const nestedArray = [1, 2, [3, 4, [5, 6]]];
  let farry = flatten(nestedArray);
  console.log(farry)

  //Part4
  function findByItem(arr,item)
  {
      var index = arr.indexOf(item);
      if (index > -1)
      {
          return {index,item}
      }
      else
      {
          return "Item not found."
      }
  }
  console.log(findByItem([2,3,4],3))

  // Part5

  function replaceByItem(arr,CurrentItem,NewItem)
  {
    var index = arr.indexOf(CurrentItem);

    if (index !== -1) {
        arr[index] = NewItem;
    }
    return arr
  }

  console.log(replaceByItem(['a','b','c','d','e','f'],'e','t'))
   //Part6
   function NumbersExtractor(str){    
    return str.match(/\d+/g);
}

let str = "I have 2 apples and 3 pineapples"
console.log(NumbersExtractor(str))

// Part7

function duplicateRemover(arr)
{
    return [...new Set(arr)];// first we convert an array to set then convert back to the array
}
console.log(duplicateRemover([1, 1, 4, 5, 3, 5, 3, 9]))