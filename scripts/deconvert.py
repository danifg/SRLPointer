import sys



if __name__ == "__main__":
	source_file = open(sys.argv[1], 'r')
	target_file = open(sys.argv[2], 'w')
	debug=False
        num_sents=1

	while True:
		line = source_file.readline()
		if len(line) > 0 and line[0] == '#': continue

		# skip multiple blank lines.
		while len(line) > 0 and len(line.strip()) == 0:
		    line = source_file.readline()
		if len(line) == 0:

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
                tops = []
		for tokens in lines:

                        for i in range(len(lines)+1):
                                if tokens[4+i] != '_':
                                        if i==0:
                                                tops.append(int(tokens[0]))
                                                continue




                num_sents+=1
		for tokens in lines:
			if debug: print tokens[0], '\t', tokens[1].encode('utf-8'), '\t', tokens[2].encode('utf-8'), '\t', tokens[3],

			target_file.write('%s\t%s\t_\t%s\t_\t%s\t_\t_\t0\t0\t_\t_' % (tokens[0].encode('utf-8'), tokens[1].encode('utf-8'), tokens[2].encode('utf-8'), tokens[3].encode('utf-8')))

			if int(tokens[0]) in tops:
				if debug: print '\t', 'ROOT',
				target_file.write('\tY')
			else:
				if debug: print '\t', '_', 
				target_file.write('\t_')
                        labels=[]
                        if int(tokens[0]) in tops:# predicates:
                                labels=tokens[4].encode('utf-8').split('#')
                                target_file.write('\t%s.%s' % (tokens[2].encode('utf-8'),labels[0]))
                        else:
                                target_file.write('\t_')
                                
			
			types=[]

							

	                for i in tops:
                                if i == int(tokens[0]) and  len(labels)>1:
                                        types.append(labels[1])
                                else:
                                        types.append(tokens[i+4])

                        
                                



			for t in types:
				
				if debug: print '\t', t,
				target_file.write('\t%s' % (t.encode('utf-8')))
			if debug: print
			target_file.write('\n')




		if debug: print
		target_file.write('\n')
	target_file.close()


	

			
	
		
