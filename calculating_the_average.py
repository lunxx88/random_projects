def average(visitors: List[int]) -> int:
    # write your code here ^_^
    lowest = min(visitors)
    highest = max(visitors)
    old_list = visitors.remove(lowest), visitors.remove(highest)
    
    for i in visitors:
        result = sum(visitors)
        result = result / len(visitors)
    return int(result)


print(average([100,200,300]))

