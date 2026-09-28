from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = OrderedDict()
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.move_to_end(city)
        else:
            answer += 5
            
            if len(cache) >= cacheSize:
                cache.popitem(last=False)
                
            cache[city] = True
            
    return answer