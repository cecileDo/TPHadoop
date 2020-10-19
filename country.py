import math
import sys

tab_pays = dict()

fichier_pays="""AA,-70.066667, 12.416667, -69.85, 12.616667, -69.9583335, 12.516667
AC,-62.333333, 16.916667, -61.666667, 17.733333, -62, 17.325
AE,45, 22.166667, 58, 26.133333, 51.5, 24.15
AF,60.566667, 29.383333, 74.8868713067265, 38.483611, 67.7267691533633, 33.933472
AG,-8.666667, 19, 13, 37.116667, 2.1666665, 28.0583335
AJ,44.876389, 38.416667, 50.858333, 41.910556, 47.867361, 40.1636115
AL,19.266667, 39.65, 21.05, 42.659167, 20.1583335, 41.1545835
AM,43.4425, 38.894167, 46.560556, 41.3, 45.001528, 40.0970835
AN,1.416667, 42.433333, 1.783333, 42.65, 1.6, 42.5416665
AO,10, -32, 23.983333, -4.4, 16.9916665, -18.2
AR,-73.533333, -58.116667, -53.65, -21.783333, -63.5916665, -39.95
AS,112.928889, -55.05, 167.983333, -9.133333, 140.456111, -32.0916665
AT,123.016667, -12.533333, 123.533333, -12.216667, 123.275, -12.375
AU,1.2, 46.377222, 19, 49.016667, 10.1, 47.6969445
AV,-63.433333, 18.15, -62.916667, 18.6, -63.175, 18.375
BA,45, 25, 50.823333, 26.416667, 47.9116665, 25.7083335
BB,-59.65, 13.033333, -59.416667, 13.333333, -59.5333335, 13.183333
BC,20, -26.833333, 29.016667, -17.833333, 24.5083335, -22.333333
BD,-64.882778, 32.246944, -64.633333, 32.390556, -64.7580555, 32.31875
BE,2.566667, 49.516667, 6.4, 51.683333, 4.4833335, 50.6
BF,-80.483333, 20, -70, 29.375, -75.2416665, 24.6875
BG,84, 20.6, 92.683333, 26.5, 88.3416665, 23.55
BH,-89.216944, 15.9, -87.483333, 18.483333, -88.3501385, 17.1916665
BK,15.747222, 42.558056, 19.618333, 45.268333, 17.6827775, 43.9131945
BL,-69.6, -22.883333, -57.566667, -9.666667, -63.5833335, -16.275
BM,92.190833, 6, 102, 28.35, 97.0954165, 17.175
BN,-4, 6.233333, 3.816667, 12.3614, -0.0916665000000001, 9.2973665
BO,22.55, 50.716667, 32.708056, 56.066667, 27.629028, 53.391667
BP,155.516667, -12.883333, 170.2, -5.166667, 162.8583335, -9.025
BR,-73.75, -33.733333, -28.85, 5.266667, -51.3, -14.233333
BS,39.7, -21.416667, 39.7, -21.416667, 39.7, -21.416667
BT,80, 26.716667, 92.033333, 30, 86.0166665, 28.3583335
BU,22.371389, 41, 28.6, 44.193611, 25.4856945, 42.5968055
BV,3.285278, -54.452778, 3.433889, -54.386111, 3.3595835, -54.4194445
BX,110, -2, 120, 5.05, 115, 1.525
BY,29.023889, -4.443333, 30.831389, -2.3425, 29.927639, -3.3929165
CA,-141.666667, 40, -52.666667, 83.116667, -97.166667, 61.5583335
CB,102.358333, 9.916667, 107.566667, 17.483333, 104.9625, 13.7
CD,2, 7.5, 24, 26, 13, 16.75
CE,79.516667, 5.916667, 81.866667, 9.833333, 80.691667, 7.875
CF,11.166667, -4.995556, 20, 3.866667, 15.5833335, -0.5644445
CG,12.266667, -13.466667, 31.233333, 5.133333, 21.75, -4.166667
CH,74.166667, 18.163056, 134.672222, 53.5, 104.4194445, 35.831528
CI,-109.466667, -56.533333, -66.433333, -17.53, -87.95, -37.0316665
CJ,-81.416667, 19.25, -79.716667, 19.75, -80.566667, 19.5
CK,96.816667, -12.204167, 96.918056, -11.833333, 96.8673615, -12.01875
CM,8.483333, 2.016667, 16, 16, 12.2416665, 9.0083335
CN,43.226111, -13, 45.316667, -11.35, 44.271389, -12.175
CO,-81.85, -4.214722, -66.854722, 13.383333, -74.352361, 4.5843055
CR,147.1, -29.472222, 159.119444, -15.5, 153.109722, -22.486111
CS,-87.1, 5.5, -82.05, 11.216667, -84.575, 8.3583335
CT,14.533333, 2.433333, 27.216667, 10.7, 20.875, 6.5666665
CU,-84.950833, 19.828056, -74.135, 23.265833, -79.5429165, 21.5469445
CV,-25.366667, 14.8, -22.666667, 17.2, -24.016667, 16
CW,-171.783333, -21.953056, -157.3375, -8.918611, -164.5604165, -15.4358335
CY,32.270833, 34.566667, 34.6, 35.7, 33.4354165, 35.1333335
DA,4.516667, 53.583333, 18, 64, 11.2583335, 58.7916665
DJ,41, 10.9825, 43.451944, 13, 42.225972, 11.99125
DO,-61.483333, 15.2, -61.25, 15.633333, -61.3666665, 15.4166665
DR,-71.966667, 17.473056, -68.316667, 19.933333, -70.141667, 18.7031945
EC,-92, -4.95, -75.216667, 1.65, -83.6083335, -1.65
EG,24.7, 20.383333, 36.333333, 31.916667, 30.5166665, 26.15
EI,-10.680833, 51.425556, -6.0025, 55.433333, -8.3416665, 53.4294445
EK,5.05, -1.483333, 11.4, 3.783333, 8.225, 1.15
EN,21.795833, 57.521389, 28.883333, 59.983333, 25.339583, 58.752361
ER,36.483333, 12.383333, 43.114722, 18.033333, 39.7990275, 15.208333
ES,-90.116389, 13.158611, -87.657222, 14.433333, -88.8868055, 13.795972
ET,33.033333, 3.433333, 47.45, 14.698889, 40.2416665, 9.066111
EU,40.366667, -22.333333, 40.366667, -22.333333, 40.366667, -22.333333
EZ,12.116667, 40.65, 25.5, 59.65, 18.8083335, 50.15
FG,-60, 2.166667, -51.65, 5.75, -55.825, 3.9583335
FI,18, 58.83, 32, 70.083333, 25, 64.4566665
FJ,180, -21.016667, -179.983333, -12.466667, -179.9916665, -16.741667
FK,-61.433333, -52.966667, -57.666667, -50.966667, -59.55, -51.966667
FM,137.425, 1.026389, 163.034444, 10.093611, 150.229722, 5.56
FO,-7.8, 61.333333, -6.25, 62.4, -7.025, 61.8666665
FP,180, -27.916667, -179.8, 16.633333, -179.9, -5.641667
FR,-5.133333, 41.333333, 9.533333, 51.083333, 2.2, 46.208333
FS,50.233333, -50.016667, 77.6, -37.783333, 63.9166665, -43.9
GA,-16.816944, 7, -4, 13.816667, -10.408472, 10.4083335
GB,8.7, -3.9, 14.483333, 2.283333, 11.5916665, -0.8083335
GG,40.013056, 41.15, 46.635556, 43.570556, 43.324306, 42.360278
GH,-4, 4.733333, 1.192778, 11.15, -1.403611, 7.9416665
GI,-5.35, 36.1, -5.333333, 36.15, -5.3416665, 36.125
GJ,-61.8, 11.983333, -61.25, 12.666667, -61.525, 12.325
GK,-2.7, 49.401111, -2.158056, 49.733333, -2.429028, 49.567222
GL,-73.05, 51.7, -12.133333, 83.666667, -42.5916665, 67.6833335
GM,5.9, 47.266667, 15.033333, 55.05, 10.4666665, 51.1583335
GO,47.3, -11.566667, 47.366667, -11.5, 47.3333335, -11.5333335
GP,-63.15, 15, -61, 18.116667, -62.075, 16.5583335
GR,19.381667, 34.8, 29.648056, 44, 24.5148615, 39.4
GT,-92.583333, 13.751111, -87.05, 17.816667, -89.8166665, 15.783889
GV,-15.366667, 7, -4, 12.633333, -9.6833335, 9.8166665
GY,-61.233333, 1.316667, -56, 8.433333, -58.6166665, 4.875
GZ,34.221389, 31.216667, 34.533333, 31.566667, 34.377361, 31.391667
HA,-74.483333, 18.016667, -71.633333, 20.083333, -73.058333, 19.05
HK,113.833333, 22.15, 114.433333, 22.566667, 114.133333, 22.3583335
HM,72.566667, -53.2, 73.85, -52.9, 73.2083335, -53.05
HO,-89.333333, 13.016667, -82.5, 17.45, -85.9166665, 15.2333335
HR,13.493333, 42.380278, 19.383056, 46.526944, 16.4381945, 44.453611
HU,16.183333, 45.75, 22.866667, 48.983333, 19.525, 47.3666665
IC,-24.533333, 63.3, -13.2, 66.566667, -18.8666665, 64.9333335
ID,94.970278, -11, 141.016667, 10.616667, 117.9934725, -0.1916665
IM,-4.833333, 54.033333, -4.316667, 54.4, -4.575, 54.2166665
IN,67.016667, 6.755556, 97.35, 35.9558333333333, 82.1833335, 21.3556946666667
IO,71.265278, -7.35, 72.483333, -5.233333, 71.8743055, -6.2916665
IP,-109.216667, 10.283333, -109.216667, 10.283333, -109.216667, 10.283333
IR,27.4455, 25.05, 62, 39.7754, 44.72275, 32.4127
IS,34.283333, 29.516667, 35.666667, 33.286111, 34.975, 31.401389
IT,1.35, 35.483333, 20.433333, 48.533333, 10.8916665, 42.008333
IV,-8.538889, 4.35, -2.566667, 10.652222, -5.552778, 7.501111
IZ,38.800871, 28.866667, 48.833333, 37.352778, 43.817102, 33.1097225
JA,122.933333, 20.416667, 154, 45.520833, 138.4666665, 32.96875
JE,-2.253889, 49.112778, -1.927778, 49.305833, -2.0908335, 49.2093055
JM,-78.366667, 17, -70, 18.533333, -74.1833335, 17.7666665
JN,-9.071944, 70.826389, -7.933056, 71.157778, -8.5025, 70.9920835
JO,34.9875, 29, 38.883333, 33.002222, 36.9354165, 31.001111
JU,42.75, -17.05, 42.75, -17.05, 42.75, -17.05
KE,27.433333, -4.716667, 41.8583834826426, 4.883333, 34.6458582413213, 0.0833330000000005
KG,69.333333, 39.25, 80.115833, 43.016667, 74.724583, 41.1333335
KN,124.1875, 37.6775, 130.672222, 43.003889, 127.429861, 40.3406945
KR,179.716667, -10.3, -174.533333, 4.716667, -177.408333, -2.7916665
KS,124.612222, 33.1175, 131.866667, 38.586667, 128.2394445, 35.8520835
KT,105.566667, -10.566667, 105.75, -10.4, 105.6583335, -10.4833335
KU,45, 25, 49.410556, 30.069444, 47.205278, 27.534722
KZ,46.589722, 40.416667, 90, 55.330556, 68.294861, 47.8736115
LA,100.095833, 13.933333, 107.633333, 22.5, 103.864583, 18.2166665
LE,35.103611, 33.078333, 36.592778, 34.69, 35.8481945, 33.8841665
LG,20.966667, 55.7, 28.2, 58.066667, 24.5833335, 56.8833335
LH,21, 53, 27, 56.441667, 24, 54.7208335
LI,-11.472222, 4.328333, -4, 9.5, -7.736111, 6.9141665
LO,17, 45.5, 26.5, 49.6, 21.75, 47.55
LS,9.5, 47.05, 9.75, 47.233333, 9.625, 47.1416665
LT,24, -30.666667, 29.316667, -28.616667, 26.6583335, -29.641667
LU,5.742778, 49.460833, 6.505833, 50.181667, 6.1243055, 49.82125
LY,5, 20.8, 25.5, 33.15, 15.25, 26.975
MA,43.183333, -25.6, 50.483333, -11.95, 46.833333, -18.775
MB,-61.966667, 14.383333, -60.816667, 14.866667, -61.391667, 14.625
MC,113.531389, 22.1125, 113.592222, 22.216389, 113.5618055, 22.1644445
MD,26.672222, 45.481667, 30.096111, 48.467222, 28.3841665, 46.9744445
MF,45.024444, -12.993889, 45.288611, -12.641389, 45.1565275, -12.817639
MG,87.783333, 41.55, 119.916667, 52.1, 103.85, 46.825
MH,-62.233333, 16.666667, -62.15, 16.816667, -62.1916665, 16.741667
MI,32.716667, -17.15, 37, -5, 34.8583335, -11.075
MJ,18.438056, 41.864167, 20.3425, 43.547778, 19.390278, 42.7059725
MK,20.459167, 40.866667, 23.033333, 42.373056, 21.74625, 41.6198615
ML,-12.55, 10.15, 13, 26, 0.225, 18.075
MN,7.4, 43.716667, 7.439444, 43.745833, 7.419722, 43.73125
MO,-13.1, 5.51, 2, 36.21, -5.55, 20.86
MP,56.6, -20.516667, 72.466667, -5.25, 64.5333335, -12.8833335
MR,-17.079444, 14.7382733887277, 13, 26.9, -2.039722, 20.8191366943638
MT,14.185556, 35.783889, 14.575, 36.081944, 14.380278, 35.9329165
MU,45, 16.633333, 59.838056, 26.505, 52.419028, 21.5691665
MV,72.583333, -.7, 73.7, 7.1, 73.1416665, 3.2
MX,-119.921667, 14.55, -86.716667, 32.983333, -103.319167, 23.7666665
MY,99.641277, .85, 120, 7.383333, 109.8206385, 4.1166665
MZ,30.231389, -26.857222, 40.845278, 15.033333, 35.5383335, -5.9119445
NC,158.246667, -22.783333, 172.05, -18.016667, 165.1483335, -20.4
NE,-169.916667, -19.1, -169.783333, -18.933333, -169.85, -19.0166665
NF,167.95, -29.05, 167.95, -29.05, 167.95, -29.05
NG,.233333, 11.716667, 16, 26, 8.1166665, 18.8583335
NH,166.016667, -20.25, 170.216667, -13.066667, 168.116667, -16.6583335
NI,2.716667, 4.266667, 14.65, 13.866667, 8.6833335, 9.066667
NL,3.133333, 50.75, 7.2, 53.583333, 5.1666665, 52.1666665
NO,3.033333, 56.15, 31.166667, 71.181944, 17.1, 63.665972
NP,80, 26.45, 88.183333, 30.45, 84.0916665, 28.45
NR,166.916667, -.55, 166.95, -.5, 166.9333335, -0.525
NS,-60, 2.1, -53.983333, 6, -56.9916665, 4.05
NT,-69.166667, 12.016667, -62.933333, 18.05, -66.05, 15.0333335
NU,-87.684167, 10.716667, -82.566667, 15, -85.125417, 12.8583335
NZ,179.066667, -52.616667, -178.9, -29.216667, -179.9166665, -40.916667
PA,-62.633333, -27.533333, -54.35, -19.333333, -58.4916665, -23.433333
PC,-130.733333, -25.066667, -124.783333, -23.916667, -127.758333, -24.491667
PE,-81.358333, -18.333333, -68.833333, 4.626667, -75.095833, -6.853333
PF,106.7, 6.183333, 117.816667, 20.7, 112.2583335, 13.4416665
PG,111.916667, 7.883333, 116.9, 16.966667, 114.4083335, 12.425
PK,60.866667, 23.966667, 77.800014, 37.0837107040298, 69.3333405, 30.5251888520149
PL,14, 45.5, 26.5, 54.833333, 20.25, 50.1666665
PM,-82.95, 7.213333, -77.283333, 9.65, -80.1166665, 8.4316665
PO,-31.266667, 30.033333, -5, 42.15, -18.1333335, 36.0916665
PP,120, -11.65, 159.483333, -.733333, 139.7416665, -6.1916665
PS,131.175, 2.898333, 134.716389, 8.166667, 132.9456945, 5.5325
PU,-16.651944, 5, -4, 12.683333, -10.325972, 8.8416665
QA,50.680556, 24.284722, 52.75, 26.441111, 51.715278, 25.3629165
RB,18.928889, 41.866667, 22.966667, 46.155556, 20.947778, 44.0111115
RE,55.216667, -21.366667, 57, -20, 56.1083335, -20.6833335
RM,160.8, 4.566667, 172.8, 19.316667, 166.8, 11.941667
RO,19, 43.666667, 29.65, 48.25, 24.325, 45.9583335
RP,116.65, 4.588889, 126.604444, 21.113056, 121.627222, 12.8509725
RS,19.655556, 38.7, 147.172222, 86.216667, 83.413889, 62.4583335
RW,28.866667, -2.8, 37, 5, 32.9333335, 1.1
SA,34.566667, 5, 55.166667, 32.2, 44.866667, 18.6
SB,-56.405278, 46.748333, -56.120556, 47.139722, -56.262917, 46.9440275
SC,-62.85, 17.1, -62.516667, 17.416667, -62.6833335, 17.2583335
SE,46.216667, -10.216667, 56.266667, -3.716667, 51.241667, -6.966667
SF,16.466667, -34.833333, 32.883333, -22.133333, 24.675, -28.483333
SG,-17.682778, 12.336667, -11.3780213873722, 16.666667, -14.5303996936861, 14.501667
SH,-14.416667, -40.4, -5.633333, -7.9, -10.025, -24.15
SI,13.426667, 45.083333, 17.466667, 46.866667, 15.446667, 45.975
SL,-13.316667, 5, -4, 10, -8.6583335, 7.5
SM,12.416667, 43.908333, 12.5, 43.966667, 12.4583335, 43.9375
SN,102, 1.159444, 104.4075, 4, 103.20375, 2.579722
SO,41, -1.65942969590957, 51.4, 11.983333, 46.2, 5.16195165204521
SP,-18.166667, 27.633333, 4.333333, 43.916667, -6.916667, 35.775
ST,-61.066667, 13.7, -60.866667, 14.1, -60.966667, 13.9
SU,21.883333, 3.516667, 38.833333, 27.166667, 30.358333, 15.341667
SV,10.5, 74.35, 32.583333, 80.816667, 21.5416665, 77.5833335
SW,10.958333, 46.758333, 25, 69.033333, 17.9791665, 57.895833
SX,-38.305, -59.466667, -26.333333, -53.970278, -32.3191665, -56.7184725
SY,35.6, 32, 42.337778, 37.280278, 38.968889, 34.640139
SZ,6, 45.366667, 10.5, 49.866667, 8.25, 47.616667
TD,-74, 10.033333, -60.5, 20, -67.25, 15.0166665
TE,54.416667, -15.866667, 54.416667, -15.866667, 54.416667, -15.866667
TH,97.366667, 5.616667, 105.766667, 20.442778, 101.566667, 13.0297225
TI,67.416667, 36.716667, 75, 40.9, 71.2083335, 38.8083335
TK,-72.466667, 21.116667, -71.083333, 21.95, -71.775, 21.5333335
TL,-172.516667, -9.433333, -171.183333, -8.533333, -171.85, -8.983333
TN,-176.2, -22.333333, -150, -15.566667, -163.1, -18.95
TO,-4, 6.131944, 1.816667, 11.103889, -1.0916665, 8.6179165
TP,6.466667, -.016667, 7.483333, 1.733333, 6.975, 0.858333
TS,7, 26, 13, 37.566667, 10, 31.7833335
TT,124.085556, -9.469722, 127.336667, -7.597222, 125.7111115, -8.533472
TU,25, 35.819444, 44.8, 42.1, 34.9, 38.959722
TV,176.116667, -10.75, 179.883333, -5.65, 178, -8.2
TW,118.115255566105, 21.733333, 122.107778, 26.389444, 120.111516783053, 24.0613885
TX,52.5, 35.216667, 66.65, 42.566667, 59.575, 38.891667
TZ,29.583333, -11.7, 40.433333, .833333, 35.008333, -5.4333335
UG,29.583333, -1.433333, 34.95, 4.166667, 32.2666665, 1.366667
UK,-13.65, 49.866667, 2.866667, 61.5, -5.3916665, 55.6833335
UP,20.933333, 37.8, 68.85, 63.4, 44.8916665, 50.6
US,167.740111, 8.731796, 167.740111, 8.731796, 167.740111, 8.731796
UV,-5.466667, 9.45, 2.2655, 14.983333, -1.6005835, 12.2166665
UY,-58.5, -35.033333, -53.266667, -30.183333, -55.8833335, -32.608333
UZ,56.083333, 35.266667, 80.383333, 48.583333, 68.233333, 41.925
VC,-61.433333, 12.533333, -61.116667, 13.366667, -61.275, 12.95
VE,-73.16, .766667, -59.966667, 15.7, -66.5633335, 8.2333335
VI,-64.85, 18.3, -64.266667, 18.766667, -64.5583335, 18.5333335
VM,102.216667, 8.383333, 109.466667, 23.666667, 105.841667, 16.025
VT,12.45, 41.9, 12.45, 41.9, 12.45, 41.9
WA,12.016667, -28.933333, 25.25, -16.983333, 18.6333335, -22.958333
WE,34.083333, 31.35, 35.933333, 32.545556, 35.008333, 31.947778
WF,-178.183333, -14.35, -176.083333, -13.183333, -177.133333, -13.7666665
WI,-17.110556, 20.8, -8.666667, 27.666667, -12.8886115, 24.2333335
WS,-172.816667, -14.05, -171, -13.433333, -171.9083335, -13.7416665
WZ,30.783333, -27.316667, 32.133333, -25.783333, 31.458333, -26.55
YI,19.223056, 42.556111, 20.75, 43.75, 19.986528, 43.1530555
YM,41.833333, 12.1, 54.533333, 27.695278, 48.183333, 19.897639
ZA,22, -18.05, 39.283333, 5, 30.6416665, -6.525
ZI,25.333333, -22.316667, 33.05, -15.6, 29.1916665, -18.9583335
"""

# a appeler avant d'utiliser la librairie pour initialiser le tableau de pays
def init_pays():

    for l in fichier_pays.splitlines():
        code, minLong, minLat, maxLong, maxLat, centreLong, centreLat = l.split(',')

        tab_pays.update({code:(float(minLong),float(minLat),float(maxLong),float(maxLat),float(centreLong),float(centreLat))});


def distancefromcenter(lat,long,centre_lat,centre_long):
    dlat = centre_lat-lat
    dlong = centre_long-long
    return math.sqrt(dlat*dlat + dlong*dlong)

    
# retourne le code sur 2 caracteres du pays trouve ou une chaine vide
def getCountryAt(latitude, longitude):
    closest = ''
    closestDistance = sys.float_info.max

    for p in tab_pays.keys():
        minLong, minLat, maxLong, maxLat, centreLong, centreLat = tab_pays.get(p)
             
        if (minLong<=longitude and longitude<=maxLong) and (minLat<=latitude and latitude<=maxLat):
            d = distancefromcenter(latitude,longitude,centreLat,centreLong)
            if d < closestDistance:
                closestDistance=d
                closest=p
    return closest

