



#!/bin/python3

import math
import os
import random
import re
import sys
def ddsadsa(small, big, n): 


    all_pos_moves = [ [[(n-1), (n-1)],], ]

    indexD = 0 

    index_current_layout = 0 # [[4, 4],]

    current_all_pos_moves_length = int(len(all_pos_moves))  

    flag = -1
    for i in range(400): # len(all_pos_move) =  1, i = 0 

        lay_out_i_length = len( all_pos_moves[-1] ) #len( [[4, 4],]  =  1  )

        x = 0
        new_layout  = []  #1 layout de ra 1 layout moi
        for j in range(lay_out_i_length):
            
            last_of_layout = list(all_pos_moves[i][j])     #[4, 4]  #last of layout nay khong thay doi!!
        
            # new_layout.append([last_of_layout[0]-, last_of_layout[1] -1]  )

            
            if   [last_of_layout[0] - small   ,     last_of_layout[1]  - big   ] not in new_layout:
                new_layout.append([last_of_layout[0] - small   ,     last_of_layout[1]  - big   ]     )

            if   [last_of_layout[0] - small   ,     last_of_layout[1]  + big   ] not in new_layout:
                new_layout.append([last_of_layout[0] - small   ,     last_of_layout[1]  + big   ]     )
            
            if  [ last_of_layout[0] - big     ,  last_of_layout[1] - small ] not in new_layout :
                new_layout.append( [ last_of_layout[0] - big     ,  last_of_layout[1] - small ]    )


            if  [last_of_layout[0]  - big   ,  last_of_layout[1] + small ]  not in new_layout :
                new_layout.append(   [last_of_layout[0]  - big   ,  last_of_layout[1] + small ]     )
            
            if [ last_of_layout[0] +  small     ,  last_of_layout[1]  - big  ] not in new_layout :
                new_layout.append([ last_of_layout[0] +  small     ,  last_of_layout[1]  - big  ]     )


            if  [ last_of_layout[0]  +  big  ,    last_of_layout[1] - small  ] not in new_layout:
                new_layout.append(  [ last_of_layout[0]  +  big  ,    last_of_layout[1] - small  ]     )



            if  [ last_of_layout[0] +  small     ,  last_of_layout[1]  + big  ] not in new_layout :
                new_layout.append([ last_of_layout[0] +  small     ,  last_of_layout[1]  + big  ]     )
            if  [ last_of_layout[0]  +  big  ,    last_of_layout[1] + small  ]  not in new_layout:
                new_layout.append(  [ last_of_layout[0]  +  big  ,    last_of_layout[1] + small  ]     )

            if   [0, 0] in new_layout :
                flag = 1
                break 

        all_pos_moves.append(new_layout)
        if flag == 1:
            break 

            
    print(all_pos_moves)



    print("so luong layout: ", len(all_pos_moves))

    # return len(all_pos_moves) - 1  

ddsadsa(1, 5, 7)



# def knightlOnAChessboard(n):

#     ans = []
    
#     for i in range(1, n):
#         ans_row = []
#         for j in range(1, n):
           
#             big = max(i, j)
#             small = min(i,j)

         

#             ans_row.append(ddsadsa(small, big, n) )

            
#         ans.append(ans_row) 
#     return ans 

# def shit():
    
#     n = int(input())

#     result = knightlOnAChessboard(n)

#     print('\n'.join([' '.join(map(str, x)) for x in result]))
#     print('\n')

# shit()
