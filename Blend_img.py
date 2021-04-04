import PIL, math
from PIL import Image

    # The function bellow takes three variables, the pixel value of the Brush, the pixel value of the Texture and the Effect of the blend respetively
    #Result = ((b+(t*e)-(1-e))/e) # This formula can be used instead of the formula in the function bellow, but be aware that the parameterer e have to be the inverted proportion.
    # The formula bellow is the iverse from the above. The effect(e) must be the inverted proportion i.e.: An e=0.08 above must be e=0.92 on the formula bellow
def Hght (b,t,e): # All values must be from a range from [0,1]. b=Brush pixel luminancy t=Texture pixel luminancy e=Strengh of the blend effect
    Result = (b+(t*(1-e))-e)/(1-e) # This Calculus add the brush and texture based on a difference of luminosity within a pre-defined range(variable e).
    return(Result) # The result is a number that can vary bellow 0 and above 1. Numbers between [0,1] indicate a RGB value (0=0 and 1=255). Numbers bellow 0 must clamp to black(0) and above 1 must clamp to white(1)
    #dabA = qBound(0, (dabA + (maskA * (1-pressure)) - (pressure * 255)) / (1 - pressure) , 255);
    
#Start of user's input section

pen = None
while pen != 10 and pen != 50 and pen != 100:
    print('>Enter the pen pressure \n>Choose between 10, 50 or 100')
    p = input('>')
    try:
        pen = int(p)
    except:
        pass
print('-Input the Brush location')
Brush = input('>')
print('-Input the Texture location')
Texture = input('>')

bsh = PIL.Image.open(Brush) # Opening the brush image
bshpx = bsh.load() # Brush image converted to a PixelObject, a Python's PIL module object.
txt = PIL.Image.open(Texture) # Opening the texture image
txtpx = txt.load() # Texture image converted to a PixelObject, a Python's PIL module object.

ImgBlend = Image.new('RGB',(bsh.width,bsh.height),'white') # Creates a blank image at the size of the Brush
pixels = ImgBlend.load() # Loads the new blank image as a PixelObject

efct = None # For each pen pressure available there is a wheight pre-defined. This wheight will defined the Strengh of the Blend effect.
if pen == 100:
    efct = 0.916667 # At 100 pressure the blend effect occours only when the Brush is 91% brighter then the texture.
elif pen == 50:
    efct = 0.826667 # At 50 pressure the blend effect occours only when the Brush is 82% brighter then the texture.
elif pen == 10:
    efct = 0.226667 # At 10 pressure the blend effect occours only when the Brush is 22% brighter then the texture.

#End of user's input section

for c in range(ImgBlend.width): # For loop responsible for sampling and writing the pixels of each column
    for r in range(ImgBlend.height): # For loop responsible for sampling and writing the pixels of each row
        bpx = ((bshpx[c,r][0])/255) # Taking the value of the pixel from the Brush. The value is between [0,255], so is being divided by 255 to give a range of [0,1]
        tpx = ((txtpx[c,r][0])/255) # Taking the value of the pixel from the Texture. The value is between [0,255], so is being divided by 255 to give a range of [0,1]
        R = Hght(bpx,tpx,efct) # Function that Blend the 2 pixels from the Brush and Texture, then return the Pixel value of the blend.
        BP = math.ceil(R*255) # The function Hght() return a float, but the pixel must be a integer. This line converts the value into a RGB range(0,255), and clamp the float number into the next higher integer.
        pixels[c,r] = (BP,BP,BP) # Here the blended pixel is writen into the blank image

ImgBlend.save('Height_Blend-'+str(pen)+'.png','png') # The new blended image is saved in the folder the scprit is located
#ImgBlend.show()
