fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	
    #split line into list of words
    elems = line.split()
    
    for word in elems :
    	    
    	# check if word in list
        if word not in lst :
    		lst.append(word)
		# if not, append to list

# sort list
lst.sort()
# print list
print lst


# 
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     #split line into list of words
#     elems = line.split()
#     # append words not in list
# #     for i in range(len(elems)):
# #         if elems[i] not in lst:
# # 	 	  lst.append(elems[i])
#     for word in elems :
#         if word not in lst :
#             lst.append(word)
#         
# # sort list
# lst.sort()
# # print list
# print lst