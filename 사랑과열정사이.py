def hot_cold(emotion):
    # emotion 리스트 속에서 냉정과 열정 사이의 사랑의 개수를 세어 반환.
    ss = 0
    bb = ""
    aa = ""
    for i in emotion:
        ##print(i)
        if (i == "열정") | (i == "냉정"):
            aa = i
            if bb == "사랑":
                return ss
            elif (bb == "열정") | (bb == "냉정"):
                return ss
            else:
                bb = i
        elif (i == "사랑") & (aa != ""):
            ss = ss + 1
            bb = i
        
            
print(hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']))
print(hot_cold(['냉정', '열정', '사랑', '사랑', '사랑', '사랑', '사랑']))