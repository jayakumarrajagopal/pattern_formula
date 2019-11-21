Problem:  Find smallest repeating character sequence a string is made of.
An exampe input string :

  "aaaaa" consists of "a" 5 times.
  
or "batbat" consists of "bat" twice.

or "eueueueueueu" consists "eu" 6 times.


Write function to solve above problem. The function should output: "(<repeating seq>)^<no of repetitions>"
  
                  'foobar':'(foobar)^1',
  
                  'foofoo':'(foo)^2',
                  
                  'fofofofofo':'(fo)^5',
                  
                  'bbbbbbbbbb':'(b)^10'


this provides O(n) solution for finding a smallest repeating pattern a string is made of.
where n is length of string.

test sample is there as well.
