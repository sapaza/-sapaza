import turtle
k1=50
k2=-70
k3=0
k4=50
k5=30
k6=-80
turtle.penup()
turtle.goto(50,50)
turtle.dot(20,"red")
turtle.goto(-70,30)
turtle.dot(20,"blue")
turtle.goto(0,-80)
turtle.dot(20,"green")
turtle.goto(k1+k2+k3,k4+k5+k6)
turtle.write("КЛАД!")
turtle.home()
turtle.done()