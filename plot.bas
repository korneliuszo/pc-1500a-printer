
10 S = STATUS 2
20 GRAPH
30 CLOAD M S
31 M = PEEK(S)
32 N = PEEK(S+1)
33 IF M = 0 GOTO 300
40 FOR Y=0 TO M-1
44 FOR C=0 TO 3
46 COLOR C
60 FOR X=0 TO N-1
70 V = PEEK (S+2+X+N*C+N*4*Y)
90 Z = X*8
100 IF (V AND &80) = &80 GOTO 120
110 LINE (Z,-Y)-(Z+1,-Y),0
120 IF (V AND &40) = &40 GOTO 140
130 LINE (Z+1,-Y)-(Z+2,-Y),0
140 IF (V AND &20) = &20 GOTO 160
150 LINE (Z+2,-Y)-(Z+3,-Y),0
160 IF (V AND &10) = &10 GOTO 180
170 LINE (Z+3,-Y)-(Z+4,-Y),0
180 IF (V AND &08) = &08 GOTO 200
190 LINE (Z+4,-Y)-(Z+5,-Y),0
200 IF (V AND &04) = &04 GOTO 220
210 LINE (Z+5,-Y)-(Z+6,-Y),0
220 IF (V AND &02) = &02 GOTO 240
230 LINE (Z+6,-Y)-(Z+7,-Y),0
240 IF (V AND &01) = &01 GOTO 260
250 LINE (Z+7,-Y)-(Z+8,-Y),0
260 NEXT X
265 NEXT C
270 NEXT Y
275 GLCURSOR(0,-M)
280 SORGN
290 GOTO 30
300 