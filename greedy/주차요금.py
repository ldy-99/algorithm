def solution(fees, records):
    answer = []
    
    base_time , base_fee , unit_time , unit_fee = fees
    acc = dict()
    in_time = dict()
    
    for r in records :
        _time, _car, _state = r.split()
        h,m = _time.split(':')
        cur_time = int(h) * 60 + int(m)
        if _state == 'IN':
            in_time[_car] = cur_time
        else:
            acc[_car] = acc.get(_car, 0) + cur_time - in_time.pop(_car)

    for car in in_time:
        acc[car] = acc.get(car, 0) + 23 * 60 + 59 - in_time[car]

    for car in sorted(acc):
        total_time = acc[car]
        fee = base_fee
        if total_time > base_time:
            fee += ((total_time - base_time + unit_time - 1) // unit_time) * unit_fee
        answer.append(fee)
    return answer

# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = solution(fees,records) # [14600, 34400, 5000]
# print(result)