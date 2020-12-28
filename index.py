small= 1
big = 2
n = 5 
all_pos_moves = [ [[4, 4],], ]

indexD = 0 

index_current_layout = 0 # [[4, 4],]

current_all_pos_moves_length = int(len(all_pos_moves))  



for i in range(n): # len(all_pos_move) =  1, i = 0 

    lay_out_i_length = len( all_pos_moves[-1] ) #len( [[4, 4],]  =  1  )

    x = 0
    new_layout  = []  #1 layout de ra 1 layout moi
    for j in range(lay_out_i_length):
        
        last_of_layout = list(all_pos_moves[i][j])     #[4, 4]  #last of layout nay khong thay doi!!
       
        # new_layout.append([last_of_layout[0]-, last_of_layout[1] -1]  )

        if  last_of_layout[0] - small >= 0 and last_of_layout[1] -  big >= 0 and  [last_of_layout[0] - small   ,     last_of_layout[1]  - big   ] not in new_layout:
            new_layout.append([last_of_layout[0] - small   ,     last_of_layout[1]  - big   ]     )


        if  last_of_layout[0] - small >= 0 and last_of_layout[1] +  big <= n-1 and  [last_of_layout[0] - small   ,     last_of_layout[1]  + big   ] not in new_layout:
            new_layout.append([last_of_layout[0] - small   ,     last_of_layout[1]  + big   ]     )
        
        if last_of_layout[0] - big >= 0 and last_of_layout[1] - small >= 0 and [ last_of_layout[0] - big     ,  last_of_layout[1] - small ] not in new_layout :
            new_layout.append( [ last_of_layout[0] - big     ,  last_of_layout[1] - small ]    )
        if last_of_layout[0] - big >= 0 and last_of_layout[1] + small <= n-1 and [last_of_layout[0]  - big   ,  last_of_layout[1] + small ]  not in new_layout :
            new_layout.append(   [last_of_layout[0]  - big   ,  last_of_layout[1] + small ]     )
        
        if last_of_layout[0] + small <= n-1 and last_of_layout[1] - big >= 0 and [ last_of_layout[0] +  small     ,  last_of_layout[1]  - big  ] not in new_layout :
            new_layout.append([ last_of_layout[0] +  small     ,  last_of_layout[1]  - big  ]     )
        if last_of_layout[0] + big <= n-1 and last_of_layout[1] - small >= 0 and  [ last_of_layout[0]  +  big  ,    last_of_layout[1] - small  ] not in new_layout:
            new_layout.append(  [ last_of_layout[0]  +  big  ,    last_of_layout[1] - small  ]     )

    all_pos_moves.append(new_layout)
        
print(all_pos_moves)

# for i in range(8):
    


#     currentD = list(d[indexD])  

#     current_len_d = len(currentD)
#     for j in range(current_len_d):
#         if  currentD[j][0] - small >= 0 and lastD[1] - big >= 0 and  [ lastD[0] - small ,       lastD[1] - big   ]  not in d:
#             d[j].append(  [ currentD[j][0] - small ,       currentD[j][0] - big   ]   )
        
        # if  lastD[0] - small >= 0 and lastD[1] +  big <= n-1 and  [lastD[0] - small   ,     lastD[1]  + big   ] not in d:
        #     d.append([lastD[0] - small   ,     lastD[1]  + big   ]     )
        
        # if lastD[0] - big >= 0 and lastD[1] - small >= 0 and [ lastD[0] - big     ,  lastD[1] - small ] not in d :
        #     d.append( [ lastD[0] - big     ,  lastD[1] - small ]    )
        # if lastD[0] - big >= 0 and lastD[1] + small <= n-1 and [lastD[0]  - big   ,  lastD[1] + small ]  not in d :
        #     d.append(   [lastD[0]  - big   ,  lastD[1] + small ]     )
        
        # if lastD[0] + small <= n-1 and lastD[1] - big >= 0 and [ lastD[0] +  small     ,  lastD[1]  - big  ] not in d :
        #     d.append([ lastD[0] +  small     ,  lastD[1]  - big  ]     )
        # if lastD[0] + big <= n-1 and lastD[1] - small >= 0 and  [ lastD[0]  +  big  ,    lastD[1] - small  ] not in d:
        #     d.append(  [ lastD[0]  +  big  ,    lastD[1] - small  ]     )
    

        
    # indexD += 1 
    
# for i  in range(len(d)):
#     d[i] = sum(d[i])
    
# d = list(set(d))
# d.sort()
# print(d)




    #bo 2 dong nay 
#     if lastD[0] + big <= n-1 and lastD[1] + small <= n-1:
#         d.append(  [ lastD[0]  +  big  ,    lastD[1] + small  ]     )
#     if lastD[0] + small <= n-1 and lastD[1]+big<=n-1:
#         d.append(  [ lastD[0]  +  small  ,    lastD[1] + big  ]     )