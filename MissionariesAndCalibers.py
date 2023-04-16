leftside={'M':3,'C':3}
rightside={'M':0,'C':0}
goal={'M':0,'C':0}
print("INITIAL:",leftside)
print("GOAL:",goal)
print("1.MOVE 1 CANNIBAL")
print("2.MOVE 1 MISSIONARY")
print("3.MOVE 2 CANNIBALS")
print("4.MOVE 2 MISSIONARIES")
print("5.MOVE 1 MISSIONARY AND 1 CANNIBAL")
def left(ch,leftside,rightside):
  if ch==1:
    leftside['C']=leftside['C']-1
    rightside['C']=rightside['C']+1
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==2:
    leftside['M']=leftside['M']-1
    rightside['M']=rightside['M']+1
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==3:
    leftside['C']=leftside['C']-2
    rightside['C']=rightside['C']+2
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==4:
    leftside['M']=leftside['M']-2
    rightside['M']=rightside['M']+2
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==5:
    leftside['C']=leftside['C']-1
    leftside['M']=leftside['M']-1
    rightside['C']=rightside['C']+1
    rightside['M']=rightside['M']+1
    print(leftside)
    print(rightside)
    return leftside,rightside
def right(ch,leftside,rightside):
  if ch==1:
    leftside['C']=leftside['C']+1
    rightside['C']=rightside['C']-1
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==2:
    leftside['M']=leftside['M']+1
    rightside['M']=rightside['M']-1
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==3:
    leftside['C']=leftside['C']+2
    rightside['C']=rightside['C']-2
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==4:
    leftside['M']=leftside['M']+2
    rightside['M']=rightside['M']-2
    print(leftside)
    print(rightside)
    return leftside,rightside
  if ch==5:
    leftside['C']=leftside['C']+1
    leftside['M']=leftside['M']+1
    rightside['C']=rightside['C']-1
    rightside['M']=rightside['M']-1
    print(leftside)
    print(rightside)
    return leftside,rightside
while(leftside['M']!=0 or leftside['C']!=0):
  ch=int(input("ENTER CHOICE: "))
  print("LEFT")
  leftside,rightside=left(ch,leftside,rightside)
  if(leftside['M']!=0 or leftside['C']!=0):
    ch=int(input("ENTER CHOICE: "))
    print("RIGHT")
    leftside,rightside=right(ch,leftside,rightside)
if(leftside==goal):
  print("Goal Acheived")
