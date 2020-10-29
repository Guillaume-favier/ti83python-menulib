from ti_system import *
import sys

def menu(list,curs=0,title=False):
  disp_cursor(0)
  if len(list) > 10:
    raise NameError('list has more then 10 objects')
  disp_clr()
  cur=int(curs)
  pcur =cur
  ok=True
  f=0
  v=0
  while ok==True:
    if f==0:
      if title==False:
        p=0
      else:
        disp_at(1,str(title),"center")
        p=1
      for x in range(len(list)):
        disp_at(x+1+p,"  "+str(x)+": "+str(list[x]),"left")
        pass
    if pcur == cur:
      if f==0:
        disp_at(cur+1+p,"> "+str(cur)+": "+str(list[cur]),"left")
        f=1
    else:
      disp_at(pcur+1+p,"  "+str(pcur)+": "+str(list[pcur]),"left") 
      disp_at(cur+1+p,"> "+str(cur)+": "+str(list[cur]),"left")
    pcur=cur
    y=wait_key()
    if y==3:
      if cur!=0:
        cur-=1
      else:
        cur=len(list)-1
    elif y==4:
      if cur+1!=(len(list)):
        cur+=1
      else:
        cur=0
    elif y==64018:
      if v==0:
        v=1
      else:
        v=0
    elif y>=142 and y<=151:
      if y-142 <=len(list):
        disp_clr()
        disp_cursor(1)
        return y-142
    elif y>=243 and y<=251:
      disp_clr()
      disp_cursor(1)
      return 242-y
    elif y==10 or y==11 or y==68 or y==90 or y==2 or y==9 or y==64:
      disp_clr()
      disp_cursor(1)
      return 0
    elif y==5 or y==13 or y==1:
      disp_clr()
      disp_cursor(1)
      return cur
    if v==1 :
      disp_at(11,str(y),"left")
      disp_at(11,str(cur),"right")
    else :
      disp_at(11,"","left")
#print('\n'+str(menu(["zero","un","deux","brouette"],0)))
