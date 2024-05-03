''' 
suhur problem
the idea is to see what meal can be eaten before fasting 
meals list have a different meals that can be eaten in a certain amount of time before Al-fajr prayer start "timeLeft"
for example:
meals = [2,3,4,9,10] 
timeLeft = 10

I still have 10 minutes before starting fasting,
then I can eat the meal that takes 10 minutes
'''

def maxMealsBeforeFajr(timeLeft: int, meals: List[int]) -> int:
    # write your code here ^_^
    
    total = 0
    counter = 0
    for i in meals:
      if i+total <= timeLeft:
       
       
        total += i
        counter += 1
      else:
        break
        
    return counter


      
      
print(maxMealsBeforeFajr(10, [2,3,4,9,10]))
print(maxMealsBeforeFajr(0,  [2,1,3])) 
print(maxMealsBeforeFajr(20,  [17,1,1,1]))  
print(maxMealsBeforeFajr(10,  [21,11,12,14] ))  
