"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "jlithgow"

import rhinoscriptsyntax as rs
import random
random.seed("05_05_19")

options_tideAmount = {
	"min": 3, 
	"max": 10
}

options_tideSize = {
	"min": 25,
	"max": 50
}

options_tideDistance = {
	"min": 5,
	"max": 50
}

options_thickness = 5

class Tide:
	def __init__(self):
		self.distance = random.randint(options_tideDistance["min"],options_tideDistance["max"])
		self.size = random.randint(options_tideSize["min"],options_tideSize["max"])

# Building

### General
centerPoint = (0,0,0)
rs_CenterPoint = rs.AddPoint(centerPoint)
centerAxis = rs.AddLine( (0,0,0),(0,0,1))
tideAmount = random.randint(options_tideAmount["min"],options_tideAmount["max"])


### Degree
degree = 3


### Curve Points
shorePoints = [centerPoint]

##### Flat Bottom
bottomTide = Tide()
shorePoints.append( ((bottomTide.size/2), 0, 0) )
shorePoints.append( (bottomTide.size, 0, 0) )


##### Meat
for count in range(tideAmount):
	tide = Tide()
	
	pointData = {
		"x": tide.size,
		"y": 0,
		"z": tide.distance + shorePoints[count][2]
	}

	point = (pointData["x"], pointData["y"], pointData["z"])
	shorePoints.append(point)

### Top Curve
topCurve = shorePoints[len(shorePoints)-1]

arrPoints = []
for count in range(len(shorePoints)):
	pointData = {
		"x": shorePoints[count][0],
		"y": shorePoints[count][1],
		"z": shorePoints[count][2]
	}

	point = rs.AddPoint( (pointData["x"], pointData["y"], pointData["z"]) )
	arrPoints.append(point)




### Knots
arrKnots = [0,0,0]

knotAmount = ((degree + len(shorePoints)) - 1)
currentKnotAmount = (knotAmount - len(arrKnots)) - 3
print(currentKnotAmount)

for count in range(currentKnotAmount):
	arrKnots.insert(count+3, (count+1))

endNumber = (arrKnots[len(arrKnots)-1])+1
for count in range(3):
	arrKnots.append(endNumber)

### Outline
vaseOutline = rs.AddNurbsCurve(arrPoints, arrKnots, degree)

### Revolve
vaseSurface = rs.AddRevSrf(vaseOutline, centerAxis)

### Thicken Wall
thickness = -1 * options_thickness
vase = rs.OffsetSurface( vaseSurface, thickness, None, False, True )


#DeBugging
print("Point Amount", len(arrPoints))
print("Shore Point Amount", len(shorePoints))
print("Knot Amount", len(arrKnots))
print("arrPoints", arrPoints)
print("arrKnots", shorePoints)
print("arrKnots", arrKnots)


# Output
#a = arrPoints 
#b = shorePoints
#c = vaseSurface
a = vase
