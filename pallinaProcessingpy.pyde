vx=1
vy=1
x=10
y=10
x1=20
y1=20
h=25
l=80
xr=300
yr=375
xr2=300
yr2=0
c=0
def setup():
   size(800,400)

def draw():
       global x,y,vx,vy,x1,y1,xr,xr2,yr2

       background(5,255,0)
       ellipse(x,y,x1,y1)
       rect(xr,yr,l,h)
       rect(xr2,yr2,l,h)
       print("perso")
       textSize(20)
       text(c,100,100)
    
       x=x+2*vx
       y=y+2*vy
       if x>width or x<0:
           vx*=-1
           fill(random(255),random(255),random(255))
       if y>height or y<0:
           vy*=-1    
           fill(random(255),random(255),random(255))
       if x>xr and x<xr+l and y+y1/2>yr:
           vy*=-1
       if x>xr2 and x<xr2+l and y-y1/2<(yr2+h):
           vy*=-1
      
  
    
        
           
def keyPressed():
    global x,y,vx,vy,x1,y1,xr,xr2,yr2
    if key=='a' and xr2>0 :
            print("Sinistra")
            xr2-=8
    if key=='d' and xr2<(width-l):
           xr2+=8 
                      
    if keyCode==LEFT and xr>0 :
        print("Sinistra")
        xr-=8
    if keyCode==RIGHT and xr<(width-l):
        xr+=8 
  
        
