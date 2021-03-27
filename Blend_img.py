import PIL, math
from PIL import Image

def Hght (b,t,c,o): # Three variables, the pixel value of the Brush, Texture and the Pen Pressure respectly
    Result = ((b+(t*(c/100))-((100-o)-c))/c)*256 # Calculus
    Rst = math.ceil(Result)
    return(Rst)

def Xln(t,c): # first variable is the pixel value of the texture. The second variable is the constant that weights the texture (the object psr in this code)
    y = (100-t)
    m = (100/(c-(c*0.25)))
    x = y/m
    o = (c-x)-(c*(t/100))
    return(o)


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

bsh = PIL.Image.open(Brush)
bshpx = bsh.load()
txt = PIL.Image.open(Texture)
txtpx = txt.load()

ImgBlend = Image.new('RGB',(bsh.width,bsh.height),'white') # Creates a blank image at the size of the Brush
pixels = ImgBlend.load() # Loads the new blank image as a PixelObject

psr = None # Pen Pressure is not defined by a curve in this demo. For each pen pressure available there is a threshold pre-defined. Here this valued is being defined to ease the computation.
if pen == 100:
    psr = 6.645
elif pen == 50:
    psr = 16.6666
elif pen == 10:
    psr = 70

for c in range(ImgBlend.width):
    for r in range(ImgBlend.height):
        bpx = ((bshpx[c,r][0])/255)*100
        tpx = ((txtpx[c,r][0])/255)*100
        Off = Xln(tpx,psr)
        R = Hght(bpx,tpx,psr,Off) # Function that blend the 2 pixels from the Brush Image and Texture Image and return the Pixel value
        pixels[c,r] = (R,R,R) # R is the result of the blend function. I have to make the function that will calculate R.

ImgBlend.save('Height_Blend-'+str(pen)+'.png','png')
#ImgBlend.show()
