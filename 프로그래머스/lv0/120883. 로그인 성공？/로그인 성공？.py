def solution(id_pw, db):

    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    
    return "fail"    
        
#     for i in db:
#         if i[0] == id_pw[0]:
#             if i[1] == id_pw[1]:
#                 return "login"
#             else:
#                 return "wrong pw"
    
#     return "fail"