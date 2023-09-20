#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
function pigIt(str){
  //Code here
  let strArr = str.split(" ");
  for(let i=0; i<strArr.length; i++){
    if (strArr[i].charCodeAt(strArr[i].substr(0)) >= 65){
      strArr[i] = strArr[i].substr(1) + strArr[i].substr(0, 1) + "ay"
    }
  }
  return strArr.join([separator = ' '])
}