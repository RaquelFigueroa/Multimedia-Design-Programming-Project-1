#Name: Raquel Figueroa
#Date Modified: 10 February 2016
#Desription: First, finds the median color values for each filter to form a photo without the pesky tourist.
#Then median filtered image is converted into its negative color form
#GitHub: https://github.com/RaquelFigueroa/Multimedia-Design-Programming-Project-1.git


pic1 = makePicture("/home/rfig/cst_205/project_1/Project1Images/1.png")
pic2 = makePicture("/home/rfig/cst_205/project_1/Project1Images/2.png")
pic3 = makePicture("/home/rfig/cst_205/project_1/Project1Images/3.png")
pic4 = makePicture("/home/rfig/cst_205/project_1/Project1Images/4.png")
pic5 = makePicture("/home/rfig/cst_205/project_1/Project1Images/5.png")
pic6 = makePicture("/home/rfig/cst_205/project_1/Project1Images/6.png")
pic7 = makePicture("/home/rfig/cst_205/project_1/Project1Images/7.png")
pic8 = makePicture("/home/rfig/cst_205/project_1/Project1Images/8.png")
pic9 = makePicture("/home/rfig/cst_205/project_1/Project1Images/9.png")


#get photo height/width information
height = getHeight(pic1) #557

width = getWidth(pic1) #495 px

#create new empty photo with H=557 and W=495
newPic = makeEmptyPicture(width, height)

for x in range(width):
  for y in range(height):
    px1 = getPixel(pic1, x, y)
    px2 = getPixel(pic2, x, y)
    px3 = getPixel(pic3, x, y)
    px4 = getPixel(pic4, x, y)
    px5 = getPixel(pic5, x, y)
    px6 = getPixel(pic6, x, y)
    px7 = getPixel(pic7, x, y)
    px8 = getPixel(pic8, x, y)
    px9 = getPixel(pic9, x, y)
    pxNew = getPixel(newPic, x, y)
    
    redValues = []
    redValues.append(getRed(px1))
    redValues.append(getRed(px2))
    redValues.append(getRed(px3))
    redValues.append(getRed(px4))
    redValues.append(getRed(px5))
    redValues.append(getRed(px6))
    redValues.append(getRed(px7))
    redValues.append(getRed(px8))
    redValues.append(getRed(px9))
    
    greenValues = []
    greenValues.append(getGreen(px1))
    greenValues.append(getGreen(px2))
    greenValues.append(getGreen(px3))
    greenValues.append(getGreen(px4))
    greenValues.append(getGreen(px5))
    greenValues.append(getGreen(px6))
    greenValues.append(getGreen(px7))
    greenValues.append(getGreen(px8))
    greenValues.append(getGreen(px9))
    
    blueValues = []
    blueValues.append(getBlue(px1))
    blueValues.append(getBlue(px2))
    blueValues.append(getBlue(px3))
    blueValues.append(getBlue(px4))
    blueValues.append(getBlue(px5))
    blueValues.append(getBlue(px6))
    blueValues.append(getBlue(px7))
    blueValues.append(getBlue(px8))
    
    redValues.sort()
    greenValues.sort()
    blueValues.sort()
    
    redColor = redValues[4]
    greenColor = greenValues[4]
    blueColor =  blueValues[4]
    
    newColor = makeColor(255-redColor, 255-greenColor, 255-blueColor)
    setColor(pxNew, newColor)
       
       
show(newPic)#Median photo in negative color form

