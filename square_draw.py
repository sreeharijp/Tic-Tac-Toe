def square(x,y,s):
    import turtle as t;
    a=t.getscreen();
    a.setup(width=1.0,height=1.0);
    t.penup();
    t.goto(x,y);
    t.pendown();
    t.fd(s);
    t.rt(90);
    t.fd(s);
    t.rt(90);
    t.fd(s);
    t.rt(90);
    t.fd(s);
    t.rt(90);
    t.penup();
    return(a);
    
