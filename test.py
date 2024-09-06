arr = [
    {'req':'hi','res':'hello , how are you'},
    {'req':'I am fine and you','res':'I am also fine '},
    {'req':'tell me about yourself','res':'I am enola . I am voice talking assisstant . I was born in 2020 but my engineer did not upgrade me that time . but now I am upgraded and also trying to upgrade myself '},
]


# print(arr[0]['ask'])
# print(arr[0]['ans'])



inp = input("Command please : ")
def fetchCommand(question, answer):
    if question in inp :
        print(answer)
        return True
    return False
flag = False
for coms in arr:
    if takeCommand(coms["req"], coms["res"]):
        flag = True
        break
# if flag==False:
if not flag:
    print("sorry i can't understand")



  