from z3 import *

x = Solver()
flag = [Int('flag%d'%i) for i in range(32)]

for i in range(32):
    x.add(flag[i] > 23)
    x.add(flag[i] < 127)

x.add((82 * flag[16] + 58 * flag[25] + 76 * flag[21] + 31 * flag[9]+ 87 * flag[28]+ 54 * flag[2]+ 74 * flag[5]+ 99 * flag[26]+ 94 * flag[3]+ 84 * flag[19]+ 32 * flag[15]+ 90 * flag[27]+ 16 * flag[14]+ 19 * flag[8]+ 33 * flag[20]+ 35 * flag[31]+ 65 * flag[29]+ 47 * flag[12]+ 3 * flag[1]+ 57 * flag[7]+ 5 * flag[17]+ 70 * flag[13]+ 28 * flag[24]+ 79 * flag[11]+ 63 * flag[23]+ 66 * flag[30]+ 28 * flag[10]+ flag[4] + 81 * flag[6] + 61 * flag[18] + 31 * flag[22] + 71 * flag[0]) == 0x237F5)

x.add((55 * flag[6]+ 38 * flag[9]+ 39 * flag[18]+ 73 * flag[24]+ 86 * flag[13]+ 18 * flag[11]+ 40 * flag[21]+ 40 * flag[26]+ 54 * flag[14]+ 81 * flag[10]+ 71 * flag[27]+ 20 * flag[8]+ 16 * flag[28]+ 65 * flag[30]+ 87 * flag[3]+ 14 * flag[16]+ flag[5]+ 41 * flag[0]+ 58 * flag[15]+ 73 * flag[2]+ 46 * flag[23]+ 7 * flag[19]+ 89 * flag[17]+ 65 * flag[25]+ 43 * flag[7]+ 6 * flag[20] + 60 * flag[12] + 40 * flag[31] + 57 * flag[29] + 40 * flag[4] + 30 * flag[1] + 63 * flag[22]) == 0x1F21D)

x.add((28 * flag[6] + 17 * flag[21] + 18 * flag[3] + 53 * flag[10]+ 82 * flag[14]+ 70 * flag[5]+ 84 * flag[2]+ 57 * flag[19]+ 92 * flag[27]+ 57 * flag[11]+ 77 * flag[4]+ 49 * flag[8]+ 62 * flag[29]+ 97 * flag[22]+ 47 * flag[1]+ 30 * flag[16]+ 45 * flag[30]+ 94 * flag[28]+ 6 * flag[9]+ 83 * flag[20]+ 18 * flag[23]+ 97 * flag[15]+ 11 * flag[12]+ 35 * flag[7]+ 81 * flag[26]+ 67 * flag[13]+ 11 * flag[31]+ 84 * flag[24] + 63 * flag[25] + 61 * flag[18]) == 0x22863)

x.add((86 * flag[23] + 52 * flag[1] + 14 * flag[24]+ 46 * flag[6]+ 56 * flag[7]+ 13 * flag[2]+ 82 * flag[11]+ 49 * flag[30]+ 97 * flag[18]+ 50 * flag[14]+ 83 * flag[27]+ 38 * flag[13]+ 49 * flag[29]+ 9 * flag[4]+ 91 * flag[20]+ 33 * flag[25]+ 4 * flag[22]+ 5 * flag[17]+ 61 * flag[15]+ 65 * flag[3]+ 68 * flag[28]+ 6 * flag[16]+ (flag[8] * 64)+ 56 * flag[9]+ 67 * flag[10]+ 5 * flag[5]+ flag[21]+ 10 * flag[19] + 83 * flag[12] + 37 * flag[26] + 85 * flag[0]) == 0x1CA87)

x.add( 53 * flag[3] + 91 * flag[2] + 57 * flag[25] + 66 * flag[20] + 9 * flag[28]+ 63 * flag[5]+ 20 * flag[4]+ 96 * flag[8]+ 39 * flag[11]+ 91 * flag[1]+ 40 * flag[9]+ 85 * flag[14]+ 62 * flag[16]+ 95 * flag[19]+ 34 * flag[22]+ 67 * flag[31]+ 51 * flag[27]+ 45 * flag[26]+ 92 * flag[15]+ 91 * flag[21]+ 85 * flag[13]+ 12 * flag[7]+ 26 * flag[23]+ 56 * flag[30]+ 82 * flag[18]+ 72 * flag[17]+ 54 * flag[6]+ 17 * flag[12]+ 84 * flag[29]+ 17 * flag[0] + 8 * flag[24] + 63 * flag[10] == 0x261F8 )

x.add( 55 * flag[23] + 88 * flag[9]+ 48 * flag[4]+ 83 * flag[13]+ 66 * flag[7]+ 60 * flag[30]+ 57 * flag[6]+ 85 * flag[17]+ 71 * flag[28]+ 98 * flag[24]+ 83 * flag[10]+ 12 * flag[1]+ 72 * flag[31]+ 12 * flag[22]+ 80 * flag[20]+ 15 * flag[19]+ 81 * flag[21]+ 87 * flag[0]+ 37 * flag[16]+ 4 * flag[15]+ 41 * flag[3]+ 84 * flag[26]+ 56 * flag[25]+ 84 * flag[14]+ 41 * flag[27]+ 98 * flag[18]+ 18 * flag[2] + 95 * flag[11] + 33 * flag[29] + 66 * flag[8] == 0x245E3 )

x.add( 43 * flag[16] + 47 * flag[0] + 53 * flag[24] + 75 * flag[11] + 57 * flag[21]+ 63 * flag[12]+ 4 * flag[14]+ 59 * flag[31]+ 15 * flag[23]+ 12 * flag[25]+ 58 * flag[5]+ 40 * flag[4]+ 26 * flag[30]+ 8 * flag[15]+ 25 * flag[6]+ 97 * flag[10]+ 12 * flag[28]+ 74 * flag[26]+ 65 * flag[8]+ 93 * flag[27]+ 18 * flag[22]+ 84 * flag[2]+ 7 * flag[1]+ 22 * flag[18]+ 9 * flag[17]+ 89 * flag[19]+ 72 * flag[13]+ 47 * flag[20]+ 7 * flag[29] + 8 * flag[9] + 24 * flag[7] + 75 * flag[3] == 121517 )

x.add( 77 * flag[30] + 89 * flag[31] + 55 * flag[7] + 86 * flag[17]+ 74 * flag[0]+ 72 * flag[4]+ 27 * flag[20]+ 88 * flag[9]+ (flag[21] * 64)+ 52 * flag[15]+ 4 * flag[19]+ 8 * flag[1]+ 16 * flag[13]+ 54 * flag[25]+ 8 * flag[29]+ 52 * flag[23]+ 14 * flag[10]+ 88 * flag[18]+ 33 * flag[8]+ 99 * flag[27]+ 65 * flag[14]+ 66 * flag[5]+ 36 * flag[6]+ 58 * flag[16]+ 63 * flag[22]+ 93 * flag[3]+ 96 * flag[11]+ 26 * flag[26]+ 65 * flag[12] + 42 * flag[28] + 14 * flag[2] + 57 * flag[24] == 0x24F96 )

x.add( 53 * flag[24] + 95 * flag[27] + 51 * flag[7]+ 42 * flag[4]+ 78 * flag[8]+ 45 * flag[25]+ 63 * flag[30]+ 85 * flag[26]+ 30 * flag[29]+ 83 * flag[14]+ 62 * flag[31]+ 71 * flag[22]+ 45 * flag[17]+ (flag[6] * 64)+ 87 * flag[23]+ 49 * flag[28]+ 14 * flag[0]+ 4 * flag[21]+ 63 * flag[5]+ 53 * flag[13]+ 19 * flag[19]+ 44 * flag[16]+ 5 * flag[3]+ 74 * flag[15]+ 19 * flag[18]+ 89 * flag[11]+ 11 * flag[20]+ 34 * flag[12] + 14 * flag[1] + 87 * flag[10] + 63 * flag[9] + 70 * flag[2] == 142830 )

x.add( 69 * flag[0]+ 67 * flag[9]+ 57 * flag[15]+ 77 * flag[10]+ 67 * flag[26]+ 94 * flag[11]+ 13 * flag[29]+ 11 * flag[22]+ 41 * flag[5]+ 38 * flag[13]+ 90 * flag[31]+ 68 * flag[7]+ 56 * flag[14]+ 4 * flag[23]+ 66 * flag[28]+ 28 * flag[1]+ 6 * flag[12]+ 91 * flag[16]+ 59 * flag[3]+ 81 * flag[17]+ 44 * flag[2]+ 33 * flag[24]+ 34 * flag[19]+ 17 * flag[18]+ 77 * flag[25]+ 25 * flag[8]+ 8 * flag[6]+ 10 * flag[30]+ 66 * flag[20]+ 41 * flag[27]+ 29 * flag[21] == 0x1DED9 )

x.add( 31 * flag[9] + 17 * flag[4] + 6 * flag[28] + 23 * flag[25]+ 32 * flag[3]+ 72 * flag[15]+ 41 * flag[26]+ 33 * flag[30]+ 82 * flag[13]+ 20 * flag[0]+ 7 * flag[12]+ 25 * flag[29]+ 39 * flag[21]+ 57 * flag[14]+ 14 * flag[16]+ 24 * flag[24]+ 37 * flag[22]+ 71 * flag[10]+ 65 * flag[23]+ 46 * flag[8]+ 40 * flag[19]+ 77 * flag[27]+ 80 * flag[18]+ 88 * flag[6]+ 20 * flag[31]+ 83 * flag[11]+ 73 * flag[1]+ 8 * flag[5]+ 15 * flag[20] + 70 * flag[7] + 24 * flag[17] + 16 * flag[2] == 0x19B4D )

x.add( 25 * flag[21] + 79 * flag[3] + 41 * flag[24]+ 45 * flag[30]+ 82 * flag[20]+ 86 * flag[19]+ 99 * flag[9]+ 96 * flag[22]+ 85 * flag[28]+ 70 * flag[5]+ 77 * flag[23]+ 80 * flag[11]+ 40 * flag[31]+ 66 * flag[12]+ 12 * flag[2]+ 77 * flag[15]+ 72 * flag[4]+ 42 * flag[26]+ 81 * flag[27]+ 90 * flag[13]+ 37 * flag[16]+ 29 * flag[17]+ 20 * flag[29]+ 85 * flag[6]+ 6 * flag[7]+ 2 * flag[0]+ 72 * flag[1]+ 75 * flag[14] + 40 * flag[25] + 29 * flag[8] + 25 * flag[10] == 0x2519A )

x.add( 83 * flag[11] + 75 * flag[1] + 42 * flag[31]+ 95 * flag[30]+ 58 * flag[8]+ 47 * flag[13]+ 65 * flag[15]+ 24 * flag[17]+ 97 * flag[10]+ 24 * flag[21]+ 28 * flag[0]+ 77 * flag[5]+ 97 * flag[6]+ 24 * flag[26]+ 32 * flag[12]+ 5 * flag[25]+ 55 * flag[28]+ 9 * flag[23]+ 85 * flag[4]+ 6 * flag[9]+ 61 * flag[19]+ 12 * flag[3]+ 76 * flag[7]+ 36 * flag[27]+ 77 * flag[24]+ 24 * flag[29]+ 67 * flag[14]+ 19 * flag[16] + 47 * flag[20] + 13 * flag[22] == 125609 )

x.add( 30 * flag[25] + 41 * flag[28] + 65 * flag[10] + flag[1]+ 88 * flag[3]+ 90 * flag[0]+ 4 * flag[23]+ 46 * flag[7]+ 54 * flag[16]+ 16 * flag[6]+ 89 * flag[22]+ 76 * flag[27]+ 38 * flag[17]+ 3 * flag[5]+ 70 * flag[14]+ 3 * flag[24]+ 24 * flag[13]+ 54 * flag[2]+ 20 * flag[8]+ 83 * flag[12]+ 21 * flag[15]+ 77 * flag[18]+ 31 * flag[19]+ 59 * flag[21]+ 33 * flag[20]+ 84 * flag[11]+ 19 * flag[29]+ 38 * flag[26]+ 63 * flag[31] + 16 * flag[30] + 15 * flag[4] + 39 * flag[9] == 123069 )

x.add( 6 * flag[9] + 19 * flag[19] + 27 * flag[18]+ 48 * flag[4]+ 13 * flag[20]+ 44 * flag[10]+ 70 * flag[12]+ 44 * flag[17]+ 22 * flag[23]+ 55 * flag[14]+ 73 * flag[26]+ 55 * flag[8]+ 58 * flag[11]+ 31 * flag[30]+ 78 * flag[29]+ 19 * flag[25]+ 52 * flag[31]+ 27 * flag[21]+ 38 * flag[27]+ 40 * flag[28]+ 35 * flag[1]+ 48 * flag[22]+ 71 * flag[15]+ 24 * flag[6]+ 89 * flag[16]+ 37 * flag[3]+ 78 * flag[2] + 3 * flag[5] + 52 * flag[24] + 40 * flag[7] == 113842 )

x.add( 95 * flag[8] + 92 * flag[18] + 84 * flag[31] + 31 * flag[12]+ 35 * flag[10]+ 54 * flag[20]+ 26 * flag[29]+ 29 * flag[3]+ 2 * flag[23]+ 46 * flag[0]+ 30 * flag[26]+ 56 * flag[27]+ 100 * flag[11]+ 43 * flag[1]+ 15 * flag[4]+ 79 * flag[17]+ 12 * flag[5]+ 38 * flag[9]+ 3 * flag[30]+ 16 * flag[21]+ 19 * flag[13]+ 67 * flag[19]+ 37 * flag[28]+ flag[7]+ 73 * flag[16]+ 85 * flag[6]+ 17 * flag[14]+ 90 * flag[22]+ 15 * flag[2] + 43 * flag[25] + 96 * flag[24] == 119824 )

x.add( 36 * flag[22] + 69 * flag[28] + 77 * flag[6] + 92 * flag[20]+ 43 * flag[23]+ 16 * flag[19]+ 92 * flag[5]+ 49 * flag[26]+ 44 * flag[2]+ 26 * flag[29]+ (flag[25] * 64)+ 45 * flag[24]+ 99 * flag[11]+ 43 * flag[4]+ 75 * flag[21]+ 53 * flag[31]+ 18 * flag[18]+ 11 * flag[13]+ 52 * flag[0]+ 16 * flag[8]+ 9 * flag[7]+ 77 * flag[16]+ 33 * flag[10]+ 86 * flag[1]+ 33 * flag[3]+ 29 * flag[9]+ 6 * flag[12]+ 91 * flag[14]+ 36 * flag[15] + 94 * flag[27] + 13 * flag[30] + 89 * flag[17] == 135873 )

x.add( 16 * flag[7] + flag[15] + 82 * flag[9] + 60 * flag[29] + 68 * flag[2]+ 83 * flag[10]+ 47 * flag[5]+ 85 * flag[13]+ 22 * flag[8]+ 92 * flag[27]+ 75 * flag[28]+ 43 * flag[3]+ 29 * flag[22]+ 92 * flag[0]+ 54 * flag[16]+ 17 * flag[30]+ 78 * flag[18]+ 7 * flag[23]+ 69 * flag[21]+ 63 * flag[31]+ 71 * flag[4]+ 10 * flag[6]+ 66 * flag[14]+ 25 * flag[26]+ 32 * flag[1]+ 48 * flag[19]+ 86 * flag[11]+ 20 * flag[25]+ 78 * flag[20]+ 25 * flag[17] + 76 * flag[12] + 13 * flag[24] == 142509 )

x.add( 88 * flag[22] + 23 * flag[13] + 18 * flag[14] + 77 * flag[9]+ 56 * flag[30]+ 79 * flag[2]+ 71 * flag[29]+ 95 * flag[28]+ 87 * flag[24]+ 62 * flag[16]+ 85 * flag[26]+ 43 * flag[20]+ 67 * flag[15]+ 97 * flag[8]+ 80 * flag[0]+ 23 * flag[3]+ 95 * flag[25]+ 82 * flag[21]+ 66 * flag[31]+ 5 * flag[4]+ 66 * flag[27]+ 25 * flag[12]+ 4 * flag[5]+ 12 * flag[7]+ 85 * flag[1]+ 10 * flag[6]+ 45 * flag[11]+ 28 * flag[18]+ 26 * flag[19] + 48 * flag[23] + 45 * flag[17] == 148888 )

x.add( 25 * flag[8] + 81 * flag[30]+ 21 * flag[6]+ 72 * flag[11]+ 48 * flag[18]+ 2 * flag[19]+ 42 * flag[10]+ 22 * flag[24]+ 99 * flag[2]+ 78 * flag[22]+ 83 * flag[12]+ 60 * flag[9]+ 59 * flag[13]+ 15 * flag[5]+ 25 * flag[20]+ 43 * flag[15]+ 56 * flag[28]+ 33 * flag[25]+ 71 * flag[23]+ 31 * flag[0]+ 95 * flag[3]+ 73 * flag[17]+ 86 * flag[14]+ 15 * flag[21]+ 61 * flag[7]+ 12 * flag[29]+ 95 * flag[26] + 13 * flag[1] + 100 * flag[16] + 11 * flag[4] + 79 * flag[27] == 138023 )

x.add( 37 * flag[28] + 62 * flag[25] + 42 * flag[18] + 53 * flag[27]+ 52 * flag[29]+ 70 * flag[22]+ 35 * flag[30]+ 50 * flag[16]+ 59 * flag[8]+ 75 * flag[10]+ 55 * flag[20]+ 23 * flag[0]+ 52 * flag[17]+ 47 * flag[3]+ 91 * flag[13]+ 46 * flag[7]+ 42 * flag[14]+ 79 * flag[26]+ 87 * flag[21]+ 30 * flag[6]+ 26 * flag[1]+ 57 * flag[31]+ 33 * flag[12]+ 51 * flag[9]+ 56 * flag[24]+ 59 * flag[11]+ 36 * flag[23]+ 88 * flag[4]+ 28 * flag[2] + 44 * flag[15] + 19 * flag[19] + 74 * flag[5] == 142299 )

x.add( 80 * flag[21]+ 43 * flag[31]+ 67 * flag[16]+ 55 * flag[13]+ 95 * flag[24]+ 46 * flag[28]+ 93 * flag[5]+ 75 * flag[20]+ 14 * flag[25]+ 24 * flag[26]+ 50 * flag[29]+ 70 * flag[15]+ 63 * flag[30]+ 77 * flag[23]+ 96 * flag[19]+ 66 * flag[11]+ 72 * flag[27]+ 94 * flag[4]+ 63 * flag[22]+ 69 * flag[3]+ 73 * flag[1]+ 60 * flag[7]+ 9 * flag[2]+ 39 * flag[17]+ 25 * flag[0]+ 49 * flag[14] + 48 * flag[8] + 86 * flag[9] + 72 * flag[10] + 23 * flag[18] + 21 * flag[6] == 155777 )

x.add( 25 * flag[24] + 11 * flag[22] + 27 * flag[11]+ 40 * flag[8]+ 53 * flag[15]+ 40 * flag[18]+ 56 * flag[3]+ 2 * flag[2]+ 32 * flag[4]+ 90 * flag[1]+ 54 * flag[16]+ 20 * flag[9]+ 86 * flag[17]+ 82 * flag[31]+ 43 * flag[25]+ 43 * flag[13]+ 86 * flag[21]+ 17 * flag[0]+ (flag[14] * 64)+ 6 * flag[30]+ 86 * flag[5]+ 15 * flag[7]+ 46 * flag[12]+ 21 * flag[26]+ 90 * flag[20]+ 19 * flag[6]+ 93 * flag[23]+ 31 * flag[27] + 62 * flag[29] + 21 * flag[19] + 42 * flag[10] == 117687 )

x.add( 89 * flag[21] + 100 * flag[13] + flag[27]+ 66 * flag[18]+ 40 * flag[17]+ 17 * flag[0]+ 27 * flag[19]+ 26 * flag[31]+ 57 * flag[24]+ 35 * flag[3]+ 80 * flag[1]+ 67 * flag[5]+ 85 * flag[6]+ 7 * flag[15]+ 93 * flag[8]+ 3 * flag[22]+ 77 * flag[12]+ 12 * flag[28]+ 4 * flag[2]+ 27 * flag[9]+ 53 * flag[25]+ 37 * flag[30]+ 43 * flag[23]+ 33 * flag[4]+ 39 * flag[26]+ 7 * flag[7]+ 75 * flag[10]+ 15 * flag[14] + 45 * flag[20] + 36 * flag[29] + 78 * flag[11] + 31 * flag[16] == 117383 )

x.add( 73 * flag[20] + 16 * flag[26] + 100 * flag[5] + 71 * flag[28] + 71 * flag[16]+ 4 * flag[1]+ 77 * flag[31]+ 83 * flag[2]+ 11 * flag[30]+ 53 * flag[19]+ 85 * flag[12]+ 67 * flag[13]+ 39 * flag[8]+ 45 * flag[24]+ 84 * flag[22]+ 99 * flag[14]+ 38 * flag[3]+ 29 * flag[4]+ 90 * flag[9]+ 61 * flag[18]+ 40 * flag[7]+ (flag[17] * 64)+ 9 * flag[25]+ 86 * flag[29]+ 80 * flag[21]+ 4 * flag[15]+ 96 * flag[23]+ 99 * flag[10]+ 40 * flag[27] + 4 * flag[0] + 56 * flag[11] == 155741)

x.add((flag[12] * 64) + 76 * flag[0] + 5 * flag[11] + 87 * flag[2]+ 86 * flag[24]+ 76 * flag[14]+ 38 * flag[23]+ 85 * flag[3]+ 71 * flag[22]+ 42 * flag[29]+ 85 * flag[30]+ 14 * flag[10]+ 17 * flag[13]+ 42 * flag[25]+ 11 * flag[19]+ 44 * flag[15]+ 21 * flag[4]+ 60 * flag[16]+ 28 * flag[6]+ 46 * flag[20]+ 25 * flag[9]+ 77 * flag[31]+ 21 * flag[8]+ 85 * flag[7]+ 36 * flag[1]+ 91 * flag[27]+ 21 * flag[28]+ 38 * flag[17] + 3 * flag[26] + 61 * flag[21] + 15 * flag[5] + 32 * flag[18] == 132804)

x.add(95 * flag[30] + 75 * flag[28] + 3 * flag[10] + 36 * flag[1]+ 60 * flag[3]+ 84 * flag[11]+ 19 * flag[26]+ 76 * flag[27]+ 86 * flag[16]+ 92 * flag[8]+ 96 * flag[14]+ 60 * flag[21]+ 23 * flag[4]+ 60 * flag[12]+ 50 * flag[23]+ 78 * flag[22]+ 45 * flag[9]+ 42 * flag[18]+ 10 * flag[2]+ 60 * flag[20]+ 24 * flag[24]+ 77 * flag[7]+ 41 * flag[6]+ 29 * flag[13]+ 33 * flag[5]+ 2 * flag[15]+ 33 * flag[29]+ 39 * flag[31] + 41 * flag[25] + 100 * flag[19] + 9 * flag[17] + 79 * flag[0] == 145568)

x.add(68 * flag[5] + 98 * flag[27] + 98 * flag[16] + 10 * flag[19] + 25 * flag[26]+ 98 * flag[24]+ 15 * flag[6]+ 50 * flag[18]+ 88 * flag[20]+ 74 * flag[11]+ 83 * flag[1]+ 86 * flag[21]+ 52 * flag[7]+ 39 * flag[10]+ 40 * flag[13]+ 82 * flag[28]+ 37 * flag[3]+ 45 * flag[0]+ 18 * flag[25]+ 2 * flag[29]+ 6 * flag[12]+ 78 * flag[31]+ 37 * flag[2]+ 57 * flag[23]+ 3 * flag[4]+ 59 * flag[8]+ 73 * flag[15]+ flag[22]+ 18 * flag[9]+ 35 * flag[14] + 20 * flag[17] + 54 * flag[30] == 130175)

x.add(60 * flag[10] + 50 * flag[12] + 30 * flag[29] + 90 * flag[19] + 68 * flag[23]+ 60 * flag[18]+ 93 * flag[20]+ 100 * flag[11]+ 98 * flag[14]+ 32 * flag[3]+ 15 * flag[21]+ 79 * flag[0]+ 6 * flag[24]+ 62 * flag[26]+ 96 * flag[6]+ 68 * flag[22]+ 9 * flag[7]+ 88 * flag[5]+ 18 * flag[27]+ 70 * flag[9]+ 96 * flag[25]+ 89 * flag[4]+ 14 * flag[31]+ 83 * flag[17]+ 19 * flag[15]+ 44 * flag[1]+ 96 * flag[8]+ 87 * flag[16]+ 48 * flag[2]+ 95 * flag[13] + 73 * flag[28] + 92 * flag[30] == 171986)

x.add(53 * flag[30] + 87 * flag[25] + 23 * flag[29] + 80 * flag[20] + 86 * flag[9]+ 20 * flag[7]+ 29 * flag[16]+ 31 * flag[14]+ 83 * flag[26]+ 11 * flag[4]+ 29 * flag[19]+ 82 * flag[13]+ 84 * flag[10]+ 70 * flag[1]+ 52 * flag[12]+ 40 * flag[6]+ 91 * flag[8]+ 6 * flag[17]+ 77 * flag[28]+ 56 * flag[5]+ 86 * flag[23]+ 63 * flag[31]+ 26 * flag[27]+ 19 * flag[22]+ 50 * flag[3]+ 15 * flag[15]+ 67 * flag[2]+ 37 * flag[24]+ 84 * flag[18] + 81 * flag[21] + 93 * flag[0] == 151676)

x.add(29 * flag[3] + 93 * flag[5] + 67 * flag[21] + 12 * flag[11]+ 82 * flag[24]+ 100 * flag[8]+ 29 * flag[26]+ 97 * flag[12]+ 32 * flag[6]+ 26 * flag[27]+ 46 * flag[19]+ 8 * (flag[25] + 9 * flag[0] + 2 * flag[17])+ 63 * flag[10]+ 39 * flag[29]+ 81 * flag[15]+ 51 * flag[13]+ 31 * flag[30]+ 49 * flag[4]+ 3 * flag[22]+ 26 * flag[28]+ 15 * flag[20]+ 89 * flag[2]+ 5 * flag[31]+ 47 * flag[18]+ 19 * flag[23]+ 98 * flag[9] + 15 * flag[16] + 49 * flag[1] == 128223)

x.add(13 * flag[14] + 73 * flag[19] + 99 * flag[7] + 76 * flag[12] + 84 * flag[25]+ 91 * flag[10]+ 67 * flag[22]+ 77 * flag[15]+ 23 * flag[26]+ 38 * flag[4]+ 3 * flag[31]+ 76 * flag[13]+ 50 * flag[0]+ 74 * flag[11]+ 45 * flag[28]+ 58 * flag[29]+ 39 * flag[5]+ 95 * flag[9]+ 26 * flag[16]+ 23 * flag[8]+ 28 * flag[24]+ 89 * flag[1]+ 88 * flag[18]+ 3 * flag[3]+ 59 * flag[20]+ 80 * flag[23]+ 49 * flag[17]+ 56 * flag[21]+ 32 * flag[27]+ 24 * flag[2] + 77 * flag[30] + 18 * flag[6] == 138403)

if x.check() == sat:
    model = x.model()
    s = ''
    for i in range(32):
        s += chr(model[flag[i]].as_long().real)
print(s)
