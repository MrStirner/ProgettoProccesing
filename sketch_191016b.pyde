vx=1
vy=1
x=400
y=200
x1=20
y1=20
h=10
l=80
xr=300
yr=390
xr2=300
yr2=0
p1=0 
p2=0
def setup():
   size(800,400)

def draw():
       global x,y,vx,vy,x1,y1,xr,xr2,yr2,p1,p2

       background(0,0,0)
       ellipseMode(CENTER) 
       ellipse(x,y,x1,y1)

       rect(xr,yr,l,h)
       rect(xr2,yr2,l,h)
       textSize(20)
       text("SCORE :" + str(p1),10,20)
       text("SCORE :" + str(p2),20,400)
    
       x=(x)+2*vx
       y=(y)+2*vy
       if x>width or x<0:
           vx*=-1
           fill(random(255),random(255),random(255))
       if y>height or y<0:
           vy*=-1    
           fill(random(255),random(255),random(255))
       if x>xr and x<=xr+l and y+y1/2 >yr:
           vy*=-1
      
       if x>xr2 and x<=xr2+l and y-y1/2<(yr2+h):
           vy*=-1
       if y-y1/2 <yr2: 
           p1=p1+1  
           x=(width/2)
           y=(height/2)  
       if y-y1/2 > yr:    
           p2+=1
           x=(width/2)
           y=(height/2)  
  
    
        
           
def keyPressed():
    global x,y,vx,vy,x1,y1,xr,xr2,yr2
    if key=='a' and xr2>0 :
       
            xr2-=10
    if key=='d' and xr2<(width-l):
           xr2+=10
                      
    if keyCode==LEFT and xr>0 :
   
        xr-=10
    if keyCode==RIGHT and xr<(width-l):
        xr+=10
