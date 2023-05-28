def solution(angle):
    return (angle // 90) * 2 + (angle % 90 != 0) * 1
    
    
#     angles = {180:4, 91:3, 90:2, 0:1}
    
#     for angleRange, val in angles.items():
#         if angle >= angleRange: return val
        
    # if angle == 180:
    #     return 4
    # elif angle > 90:
    #     return 3
    # elif angle == 90:
    #     return 2
    # else: return 1
