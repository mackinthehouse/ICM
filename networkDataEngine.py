#IMPORTING THE REQUIRED PACKAGES

import numpy as np #work with arrays
import pandas as pd #read from excel spreadsheet
import scipy.io  #convert file to matlab in test.mat
from statistics import mean

#READING THE EXCEL SPREADSHEET

spreadsheet = "C:/Users/seana/OneDrive/Desktop/passingevents.xlsx"

#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel(spreadsheet, sheet_name=0)
# insert the name of the column as a string in brackets
OriginPlayerID = list(df['OriginPlayerID'])
DestinationPlayerID = list(df['DestinationPlayerID'])
EventOriginX = list(df['EventOrigin_x'])
EventOriginY = list(df['EventOrigin_y'])

master_matrix = np.zeros((14,14))

for i in range(len(OriginPlayerID)): #counting each plass from player to player and adding 1 to its entry in the square adjecent matric
    x=0
    y=0
    if OriginPlayerID[i] == 'Huskies_D1':
        x=1
    elif OriginPlayerID[i] == 'Huskies_D2':
        x=2
    elif OriginPlayerID[i] == 'Huskies_D3':
        x=3
    elif OriginPlayerID[i] == 'Huskies_D4':
        x=4
    elif OriginPlayerID[i] == 'Huskies_D5':
        x=5
    elif OriginPlayerID[i] == 'Huskies_F1':
        x=6
    elif OriginPlayerID[i] == 'Huskies_F2':
        x=7
    elif OriginPlayerID[i] == 'Huskies_F3':
        x=8
    elif OriginPlayerID[i] == 'Huskies_G1':
        x=9
    elif OriginPlayerID[i] == 'Huskies_M1':
        x=10
    elif OriginPlayerID[i] == 'Huskies_M2':
        x=11
    elif OriginPlayerID[i] == 'Huskies_M3':
        x=12
    elif OriginPlayerID[i] == 'Huskies_M4':
        x=13
    elif OriginPlayerID[i] == 'Huskies_M5':
        x=14
    if DestinationPlayerID[i] == 'Huskies_D1':
        y=1
    elif DestinationPlayerID[i] == 'Huskies_D2':
        y=2
    elif DestinationPlayerID[i] == 'Huskies_D3':
        y=3
    elif DestinationPlayerID[i] == 'Huskies_D4':
        y=4
    elif DestinationPlayerID[i] == 'Huskies_D5':
        y=5
    elif DestinationPlayerID[i] == 'Huskies_F1':
        y=6
    elif DestinationPlayerID[i] == 'Huskies_F2':
        y=7
    elif DestinationPlayerID[i] == 'Huskies_F3':
        y=8
    elif DestinationPlayerID[i] == 'Huskies_G1':
        y=9
    elif DestinationPlayerID[i] == 'Huskies_M1':
        y=10
    elif DestinationPlayerID[i] == 'Huskies_M2':
        y=11
    elif DestinationPlayerID[i] == 'Huskies_M3':
        y=12
    elif DestinationPlayerID[i] == 'Huskies_M4':
        y=13
    elif DestinationPlayerID[i] == 'Huskies_M5':
        y=14

    if x>0:
        if y>0:
            master_matrix[x-1,y-1] += 1

SquareAdjacencyMatrix = master_matrix.reshape((14,14)) #reshape for matlab
print(SquareAdjacencyMatrix)
scipy.io.savemat('SAM.mat', mdict={'SAM': SquareAdjacencyMatrix})

print(SquareAdjacencyMatrix)

A = ['HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD1', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD2', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD3', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD4', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HD5', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF1', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF2', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HF3', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HG1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM1', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM2', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3', 'HM3' ,'HM3', 'HM3', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4', 'HM4' ,'HM4' ,'HM4', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5', 'HM5']

B = ['HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5']

#new variable as to not fuck with global ones
a = A
b = B
#initialise weights
w = []
#fill in weights (deconstruct the SquareAdjacencyMatrix)
for i in range(14):
    I = 13-i
    for j in range(14):
        J=13-j
        w.append(SquareAdjacencyMatrix[i,j])

print(w)

#whittle out the edges with weight 0
for i in range(len(w)):
    while w[len(w)-i-1]==0: #changed if to while to get rid of the double/triple zeros (v proud of it too lmao)
        del(a[len(w)-i-1])
        del(b[len(w)-i-1])
        del(w[len(w)-i-1])

#save new a,b,w for digraph
scipy.io.savemat('a.mat', mdict={'a': np.asarray(a)})
scipy.io.savemat('b.mat', mdict={'b': np.asarray(b)})
scipy.io.savemat('w.mat', mdict={'w': np.asarray(w)})

players = ['HD1', 'HD2', 'HD3', 'HD4', 'HD5', 'HF1', 'HF2', 'HF3', 'HG1', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5']

#initialise the x coordinates for each player
HD1x = []
HD2x = []
HD3x = []
HD4x = []
HD5x = []
HF1x = []
HF2x = []
HF3x = []
HG1x = []
HM1x = []
HM2x = []
HM3x = []
HM4x = []
HM5x = []

#initialise the y coordinates for each player
HD1y = []
HD2y = []
HD3y = []
HD4y = []
HD5y = []
HF1y = []
HF2y = []
HF3y = []
HG1y = []
HM1y = []
HM2y = []
HM3y = []
HM4y = []
HM5y = []

#place x,y coordinates in each player's list
for i in range(len(OriginPlayerID)):
    if OriginPlayerID[i] == 'Huskies_D1':
        HD1x.append(EventOriginX[i])
        HD1y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_D2':
        HD2x.append(EventOriginX[i])
        HD2y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_D3':
        HD3x.append(EventOriginX[i])
        HD3y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_D4':
        HD4x.append(EventOriginX[i])
        HD4y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_D5':
        HD5x.append(EventOriginX[i])
        HD5y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_F1':
        HF1x.append(EventOriginX[i])
        HF1y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_F2':
        HF2x.append(EventOriginX[i])
        HF2y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_F3':
        HF3x.append(EventOriginX[i])
        HF3y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_G1':
        HG1x.append(EventOriginX[i])
        HG1y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_M1':
        HM1x.append(EventOriginX[i])
        HM1y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_M2':
        HM2x.append(EventOriginX[i])
        HM2y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_M3':
        HM3x.append(EventOriginX[i])
        HM3y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_M4':
        HM4x.append(EventOriginX[i])
        HM4y.append(EventOriginY[i])
    elif OriginPlayerID[i] == 'Huskies_M5':
        HM5x.append(EventOriginX[i])
        HM5y.append(EventOriginY[i])

#initialise the average xoordinates for every player
xCoordinates = []
yCoordinates = []

#average the coordinates for every player
xCoordinates.append(mean(HD1x))
xCoordinates.append(mean(HD2x))
xCoordinates.append(mean(HD3x))
xCoordinates.append(mean(HD4x))
xCoordinates.append(mean(HD5x))
xCoordinates.append(mean(HF1x))
xCoordinates.append(mean(HF2x))
xCoordinates.append(mean(HF3x))
xCoordinates.append(mean(HG1x))
xCoordinates.append(mean(HM1x))
xCoordinates.append(mean(HM2x))
xCoordinates.append(mean(HM3x))
xCoordinates.append(mean(HM4x))
xCoordinates.append(mean(HM5x))

yCoordinates.append(mean(HD1y))
yCoordinates.append(mean(HD2y))
yCoordinates.append(mean(HD3y))
yCoordinates.append(mean(HD4y))
yCoordinates.append(mean(HD5y))
yCoordinates.append(mean(HF1y))
yCoordinates.append(mean(HF2y))
yCoordinates.append(mean(HF3y))
yCoordinates.append(mean(HG1y))
yCoordinates.append(mean(HM1y))
yCoordinates.append(mean(HM2y))
yCoordinates.append(mean(HM3y))
yCoordinates.append(mean(HM4y))
yCoordinates.append(mean(HM5y))

scipy.io.savemat('x_data.mat', mdict={'xCoordinates': np.asarray(xCoordinates)})
scipy.io.savemat('y_data.mat', mdict={'yCoordinates': np.asarray(yCoordinates)})
