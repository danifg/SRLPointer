import sys



if __name__ == "__main__":
	source_file = open(sys.argv[1], 'r')
	target_file = open(sys.argv[2], 'w')
	debug=False
        max_heads=0
	while True:
		line = source_file.readline()
		if len(line) > 0 and line[0] == '#': continue

		# skip multiple blank lines.
		while len(line) > 0 and len(line.strip()) == 0:
		    line = source_file.readline()
		if len(line) == 0:
		    #print line	
		    break

		lines = []
		while len(line.strip()) > 0:
		    line = line.strip()
		    line = line.decode('utf-8')
		    lines.append(line.split('\t'))
		    line = source_file.readline()

		length = len(lines)
		if length == 0:

		    break


		predicates = []
                frame_predicates = []
		for tokens in lines:
			if tokens[12] == 'Y': 
				predicates.append(int(tokens[0]))

                                frame_predicates.append('Y')


                                


		for tokens in lines:
			if debug: print tokens[0], '\t', tokens[1].encode('utf-8'), '\t', tokens[3].encode('utf-8'), '\t', tokens[5],

			target_file.write('%s\t%s\t%s\t%s' % (tokens[0].encode('utf-8'), tokens[1].encode('utf-8'), tokens[3].encode('utf-8'), tokens[5].encode('utf-8') ))
                        

                        
			
			types=[]
			for i in range(length+1):
				
				types.append('_')

			if tokens[12] == 'Y':
                                types[0]='PREDICATE'
                                

	                num_heads=0
			for i in range(len(predicates)):

				if tokens[i+14]!='_':
					num_heads+=1
					if int(tokens[0])==predicates[i]: #it points to itself
				
                                
						head=0
                                                types[head]=types[head]+'#'+tokens[i+14]
					else:	
						
						head=predicates[i]
					        types[head]=tokens[i+14]

                        

                        if num_heads>max_heads:
                                max_heads=num_heads

			
	

			for t in types:
                                
				
				if debug: print '\t', t,
				target_file.write('\t%s' % (t.encode('utf-8')))
			if debug: print
			target_file.write('\n')




		if debug: print
		target_file.write('\n')
	target_file.close()
        

	

			
	
		
