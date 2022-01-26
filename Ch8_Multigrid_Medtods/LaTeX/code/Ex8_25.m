syms k w
n = 100; t = 0:0.1:n;
f = 1 - 2*w*(sin(k*pi/(2*n)))^2;
f1 = subs(subs(f,w,1/3),k,t);
f2 = subs(subs(f,w,1/2),k,t);
f3 = subs(subs(f,w,2/3),k,t);
f4 = subs(subs(f,w,1),k,t);
fig = figure();
hold on
plot(t, f1, 'k','linewidth', 2); plot(t, f2, 'k','linewidth', 2)
plot(t, f3, 'k','linewidth', 2); plot(t, f4, 'k','linewidth', 2)
% set the axis
plot([0 0], [-1.05 1.05], 'k','linewidth', 2); plot([0, 101], [0, 0], 'k', 'linewidth', 2)
xlim([0 n+1]); ylim([-1.1 1.1]);
axis off
scatter(0,1,'k+'); scatter(0,-1,'k+'); scatter(50,0,'k+'); scatter(100,0,'k+');
text(-2,1,'$1$','interpreter', 'latex', 'fontsize', 12)
text(-2,-1,'$-1$','interpreter', 'latex', 'fontsize', 12)
text(48,-0.05,'$n/2$','interpreter', 'latex', 'fontsize', 12)
text(100,-0.05,'$n$','interpreter', 'latex', 'fontsize', 12)
text(95,1/3+0.05,'$\omega=1/3$','interpreter', 'latex', 'fontsize', 12)
text(95,0.05,'$\omega=1/2$','interpreter', 'latex', 'fontsize', 12)
text(95,-1/3+0.05,'$\omega=2/3$','interpreter', 'latex', 'fontsize', 12)
text(95,-1+0.05,'$\omega=1$','interpreter', 'latex', 'fontsize', 12)
text(102,0,'$k$','interpreter', 'latex', 'fontsize', 12)
text(0,1.1,'$\lambda_k(T_\omega)$','HorizontalAlignment', 'center', 'interpreter', 'latex', 'fontsize', 12)
% save figure
scrsz=get(0,'ScreenSize'); set(gcf,'Position',scrsz);
saveas(gcf, '../media/Ex8_25.png')