import wcag_contrast_ratio as contrast
#from varname import varname

#list all colors in palette
blue = (0,66,118)
mildBlue = (65,123,184)
lightBlue = (194,219,242)
gold = (248,151,31)
red = (167,30,35)
brown = (59,49,42)
black = (0, 0, 0)
white = (255, 255, 255)

#create color palette
colorSet = [blue, mildBlue, lightBlue, gold, red, brown,black,white]

#check for valid combinations
def checkColor():
  for i in range(len(colorSet)):
    for j in range(i+1, len(colorSet)):
      color1 = tuple(n/255 for n in colorSet[i])
      color2 = tuple(n/255 for n in colorSet[j])
      ratio = contrast.rgb(color1, color2)
      isAAready = contrast.passes_AA(ratio)
      isAAAready = contrast.passes_AAA(ratio) 

      
      if isAAready:
          print('The ratio of ' + str(colorSet[i]) + ' and ' + str(colorSet[j]) + ' is '+ str(ratio))
          print ("This combo pass AA")
          if isAAAready:
              print("This combo pass AAA")
          print("------------------------------")
      else:
        #print("This combo does not meet standards.")
        pass 
      


checkColor()


