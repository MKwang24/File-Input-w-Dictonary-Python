def minmp(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements and properties and a compound_formula. Returns a tuple where the first element is the lowest melting point element in the compound and the second element is it's corresponding melting point.
    >>>minmp("elements.txt", "K1Fe4")
    'K', 336
    >>>minmp("elements.txt", "Fe6Cr1")
    'Fe', 1811
    """
    #open the file, take out the content
    myfile = open(filename,'r')
    content = myfile.read()
    elements = []
    Melting_point= []
    dictionary_with_melt={}
    for i in range(len(content)):
        if content[i-1] == '\n' :
            for tab in range(3):
                if content[i+tab] == '\t' :
                    elements.append(content[i:i+tab])
        if content[i-1] == '\t' :
            for sec_tab in range(5):
                if content[i+sec_tab] == '\t' :
                    Melting_point.append(int(content[i:i+sec_tab]))  
    for e in range(len(elements)):
        dictionary_with_melt[elements[e]] = Melting_point[e]
        
    input_compound = list(molform(compound_formula).keys())
    result = []
    result_melt_point=[]
    for test_element in input_compound:
        if test_element in dictionary_with_melt:
            result.append(test_element)
            result_melt_point.append(dictionary_with_melt[test_element])
        if test_element not in dictionary_with_melt:
            continue
    for num in range(len(result)):
        if result_melt_point[num] == min(result_melt_point):
            return result[num],result_melt_point[num]
    myfile.close()        
    #for i in range(len(content)):
        #if content[i] = '/n':
            #print('hi')
        
    #transfer the content into a dictionary
    
    #find the elements involved
    #compare the different melting point
    
    
def molform(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary with a string of the element symbol as the key and the number of atoms of that element as the value.
    >>>molform("C2H6O1")
    {'C':2, 'H':6, 'O':1}
    >>>molfor("C1H4")
    {'C':1, 'H':4}
    """
    dictionary= {}
    elements = []
    digits = []
    for i in range(len(compound_formula)-1):
        if compound_formula[i].isalpha():
            
            element = ''
            
            element += compound_formula[i]
            
            if compound_formula[i+1].isalpha():
            
                element += compound_formula[i+1]
            elements.append(element) 
        
        if compound_formula[i].isdigit():
            if not (compound_formula[i-1].isdigit()) and  not (compound_formula[i+1].isdigit()):
                digit = ''
                digit += compound_formula[i]
                digits.append(int(digit))
            if compound_formula[i+1].isdigit():
                digit = compound_formula[i]
                digit += compound_formula[i+1]
                digits.append(int(digit))
    if compound_formula[-1].isdigit():
        digits.append(int(compound_formula[-1]))
    elements1 = tuple(elements)
    for e in range(len(elements1)-1):
        for element in (elements1[:e]+elements1[e+1:]):
            if element.isupper():
                continue
            if element in elements1[e]:
                if not element in elements:
                    break
                elements.remove(element)
    for j in range(len(elements)):
        dictionary[elements[j]]= digits[j]
    
    return dictionary
           
        