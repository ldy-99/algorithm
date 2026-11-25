# 프로그래머스 광고 삽입 (누적 합)
# 초 단위 환산
def change(time):
    HH,MM,SS = time.split(':')
    total_time = int(HH) * 3600 + int(MM) * 60 + int(SS)
    return total_time

# 출력할땐 다시 복구
def restore(time):
    HH = time // 3600
    MM = (time % 3600) // 60
    SS = time % 60

    return f"{HH:02d}:{MM:02d}:{SS:02d}"

def solution(play_time, adv_time, logs):
    answer = ''
    play = change(play_time)
    adv = change(adv_time)
    view = [0] * (play+1)
    prefix = [0] * (play+1)
    
    for t in logs :
        start,end = t.split('-')
        start = change(start)
        end = change(end)
        view[start]+=1
        view[end]-=1

    # 첫번째 누적합
    for i in range(1, play + 1):
        view[i] += view[i - 1]
    # 두번째 누적합
    for i in range(play):
        prefix[i+1] = prefix[i] + view[i]
    
    max_view = -1
    best = 0
    
    for i in range(play-adv + 1) :
        total = prefix[i+adv] - prefix[i]
        if total > max_view :
            max_view = total
            best = i
            
    return restore(best)