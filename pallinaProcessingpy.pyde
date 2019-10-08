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
c="HAI PERSO"
def setup():
   size(800,400)

def draw():
       global x,y,vx,vy,x1,y1,xr

       background(5,255,0)
       ellipse(x,y,x1,y1)
       rect(xr,yr,l,h)
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
       if y > yr :
           print("perso")
           background(0,0,0)
           textSize(50)
           text(c,400,200)
    
        
           
def keyPressed():
    global x,y,vx,vy,x1,y1,xr
    if keyCode==LEFT and xr>0 :
        print("Sinistra")
        xr-=8
    if keyCode==RIGHT and xr<(width-l):
        xr+=8 
  
        
