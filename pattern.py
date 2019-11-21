def pattern_formula(str) :
    i=1
    length = len(str)
    while ( i <= length/2) :
        pattern = str[0:i]
        for j in range(i,length,i):
            if pattern != str[j:j+i] :
                # pattern not repeating until end..so enlarge the pattern to next char
                i=j+1 
                break
            if ( j + i >= length) :
            # matched till end..
                return "(%s)^%d" % (pattern,j/i+1)
    # did not match until end
    return "(%s)^1"%str  
    
    ###### end of function @@@@@@
