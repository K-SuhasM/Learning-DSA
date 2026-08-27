'''
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''

class Solution: 
    def fizzBuzz(self,n):
        self.n = int(n)
        answer = []  
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                answer.append("FizzBuzz") 
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else: answer.append(str(i))
        return (answer)
    
   