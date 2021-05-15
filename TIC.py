def tic():
    import turtle as t;
    t.speed(100)
    t.title('TIC TAC TOE')
    t.hideturtle()
    import square_draw as a;
    def grid():
        t.pencolor('red')
        t.pensize(8);
        a.square(-150,150,300);
        t.pensize(5);
        a.square(-150,150,100);#1
        a.square(-50,150,100);#2
        a.square(50,150,100);#3
        a.square(-150,50,100);#4
        a.square(-50,50,100);#5
        a.square(50,50,100);#6
        a.square(-150,-50,100);#7
        a.square(-50,-50,100);#8
        a.square(50,-50,100);#9
        return(1);
    def h1(p):
        t.up();
        t.goto(-130,20);
        t.down();
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h2(p):
        t.up();
        t.goto(-30,20);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h3(p):
        t.up();
        t.goto(70,20);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h4(p):
        t.up();
        t.goto(-130,-80);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h5(p):
        t.up();
        t.goto(-30,-80);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h6(p):
        t.up();
        t.goto(70,-80);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h7(p):
        t.up();
        t.goto(-130,-180);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h8(p):
        t.up();
        t.goto(-30,-180);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    def h9(p):
        t.up();
        t.goto(70,-180);
        t.down();
        style=("chiller",90)
        if p==1:
            t.pencolor("black")
            t.write('X',font=style,align="left")
        elif p==2:
            t.pencolor("blue")
            t.write('O',font=style,align="left")
    p1=(t.textinput('TIC TAC TOE','Enter name of Player I'))
    if list(p1)==[]:
        t.bye()
    else:
        p1=p1.capitalize()
    p2=(t.textinput('TIC TAC TOE','Enter name of Player II'))
    if list(p2)==[]:
        t.bye()
    else:
        p2=p2.capitalize()
    t.penup();
    t.pencolor('black')
    t.goto(0,180);
    t.down();
    style=('joker',80)
    t.write('TIC TAC TOE',font=style,align="center")
    grid()
    q=[0,0,0,0,0,0,0,0,0]
    for g in range(1,10):
        if g%2==1:
            while 1:
                v=t.textinput('TIC TAC TOE',p1+"\'s turn")
                if v.isdigit():
                    w=int(v)
                    if 0<w<10:
                        if q[w-1]==0:
                            break;
            if w==1:
                h1(1)
                q[0]=1
                if q[1]==1:
                    if q[2]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[3]==1:
                    if q[6]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[4]==1:
                    if q[8]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==2:
                h2(1)
                q[1]=1
                if q[0]==1:
                    if q[2]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[4]==1:
                    if q[7]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==3:
                h3(1)
                q[2]=1
                if q[1]==1:
                    if q[0]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[8]==1:
                    if q[5]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==4:
                h4(1)
                q[3]=1
                if q[0]==1:
                    if q[6]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[4]==1:
                    if q[5]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==5:
                h5(1)
                q[4]=1
                if q[3]==1:
                    if q[5]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[1]==1:
                    if q[7]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==6:
                h6(1)
                q[5]=1
                if q[3]==1:
                    if q[4]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[8]==1:
                    if q[2]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==7:
                h7(1)
                q[6]=1
                if q[3]==1:
                    if q[0]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[8]==1:
                    if q[7]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[4]==1:
                    if q[2]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==8:
                h8(1)
                q[7]=1
                if q[1]==1:
                    if q[4]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[8]==1:
                    if q[6]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            elif w==9:
                h9(1)
                q[8]=1
                if q[6]==1:
                    if q[7]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[5]==1:
                    if q[2]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
                if q[0]==1:
                    if q[4]==1:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p1+" Wins!!",font=style,align='center')
                        break;
            while 1:
                v=(t.textinput('TIC TAC TOE',p2+"\'s turn")) 
                if v.isdigit():
                    w=int(v)
                    if 0<w<10:
                        if q[w-1]==0:
                            break
            if w==1:
                h1(2)
                q[0]=2
                if q[1]==2:
                    if q[2]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[3]==2:
                    if q[6]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[4]==2:
                    if q[8]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==2:
                h2(2)
                q[1]=2
                if q[0]==2:
                    if q[3]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[4]==2:
                    if q[7]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==3:
                h3(2)
                q[2]=2
                if q[1]==2:
                    if q[0]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[8]==2:
                    if q[5]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[4]==2:
                    if q[6]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==4:
                h4(2)
                q[3]=2
                if q[0]==2:
                    if q[6]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[4]==2:
                    if q[5]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==5:
                h5(2)
                q[4]=2
                if q[3]==2:
                    if q[5]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[1]==2:
                    if q[7]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==6:
                h6(2)
                q[5]=2
                if q[3]==2:
                    if q[4]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[8]==2:
                    if q[2]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==7:
                h7(2)
                q[6]=2
                if q[3]==2:
                    if q[0]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[8]==2:
                    if q[7]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[4]==2:
                    if q[2]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==8:
                h8(2)
                q[7]=2
                if q[1]==2:
                    if q[4]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[8]==2:
                    if q[6]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            elif w==9:
                h9(2)
                q[8]=2
                if q[6]==2:
                    if q[7]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[5]==2:
                    if q[2]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
                if q[0]==2:
                    if q[4]==2:
                        t.home();
                        t.clear();
                        style=('casual',100);
                        t.write(p2+" Wins!!",font=style,align='center')
                        break;
            if g==9:
                g=g+1
    if g==10:
        t.home()
        t.clear()
        style=('casual',100);
        t.write('Its a Draw',font=style,align='center')
tic();
