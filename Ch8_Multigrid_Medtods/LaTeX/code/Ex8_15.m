syms x;
f1 = sin(3 * pi * x);
f2 = sin(9 * pi * x);
t = 0:1/6:1;
scatter(t, subs(f1,x,t))
hold on
scatter(t, subs(f2,x,t))