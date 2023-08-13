//Return the number (count) of vowels in the given string.

//We will consider a, e, i, o, u as vowels for this Kata (but not y).

//The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
    let count = 0;
    for (var i=0;i<str.length;i++)
      {
        let ch = str.charAt(i);    //Taking each character in the string one by one
        if(ch=='a' || ch=='e'|| ch=='i' || ch=='o' || ch=='u') //Check if the character is a vowel
          {
            count+=1;       //Increment the count every time we find a match
          }
      }
    return count;
  }

