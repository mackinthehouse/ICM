clear ALL

aPy = load('-mat', 'a.mat');
bPy = load('-mat', 'b.mat');
wPy = load('-mat', 'w.mat');
xPy = load('-mat', 'x_data.mat');
yPy = load('-mat', 'y_data.mat');
samPy = load('-mat', 'SAM.mat');

s = cellstr(aPy.a)';
t = cellstr(bPy.b)';
w = wPy.w;
D = digraph(s,t,w,'omitselfloops');
x = xPy.xCoordinates;
y = yPy.yCoordinates;
SAM = samPy.SAM;

Dundirected = graph(s,t,w,'omitselfloops');

LWidths = 5*D.Edges.Weight/(max(D.Edges.Weight));

k=plot(D,'LineWidth',LWidths,'xdata',x,'ydata',y);
xlim([0,100])
ylim([0,100])

hold on
I = imread('C:\Users\seana\OneDrive\Desktop\SFL.png'); 
h = image(xlim,flip(ylim),I); 
uistack(h,'bottom')

k.EdgeColor = [1 1 1];
k.NodeColor = [1 1 1];

eV = centrality(D,'betweenness')
clustCoeff(SAM)