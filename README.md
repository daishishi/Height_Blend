# Height_Blend
Causal Model replicating the Height blend from Photoshop Brushes

This scprit Blend two gray scale images of same size into a new one. The Blend mode use a formula that try to replicate the Height mode found in Photoshop's brushes.
The formula as derived from Final images produced in photoshop with the desired mode applied, this means this is a causal model. Is expected that using different brushes and/or texture may result in images different that ones produced in Photoshop.

While theorically the texture influence may vary between 0% to 100%, this script uses 3 virtual pen pressures with three different texture weight. A relationship between Pen pressure and texture influence/weight was derived from a single sample image.
The percentage of texture influence was defined by the percentage of the final image that shows the texture. Values bellow this treshold clamp to pure black, and above clamp to white.

100% Pen Pressure = 6.645% texture weight

50% Pen Pressure = 16.666% texture weight

10% Pen Pressure = 70% texture weight

![53c53bd136c06c465efdc57373b1052e3cb4a430](https://user-images.githubusercontent.com/7233354/112707769-8a318980-8e8c-11eb-830b-c757e6af4870.jpeg)
Image Source:I9S(https://krita-artists.org/u/I9S)
