import numpy #även fast np värkar va standard så föredrar jag att bara ha hela namnet

#Uppgift 1
print("\nUppgift1")
integerArray = numpy.array([1,2,3], dtype="i") #dtype="i" är int32 det går att skriva dtype="int64" ifall man vill 64 bit integers, men i detta fall så är int32 mycket mer en vad som behövs 
floatArray = numpy.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0], dtype="f") #samma som int går det att skriva dtype="float64"
print(integerArray.dtype) #int32
print(floatArray.dtype) #float32

#Uppgift 2

print("\nUppgift2")
t2DIntArray = numpy.array([[1,2,3],[4,5,6],[7,8,9]], dtype="i")
t2DFloatArray = numpy.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]], dtype="f") #hittade inte hur denna skulle se ut men hoppas detta fungerar
print(t2DIntArray)

#uppgift 3
print("\nUppgift3")
b = numpy.array([[1, 2, 3], [4, 5, 6]], float)
print(f"{type(b)} med värden : \n{b} \nmed datatypen {b.dtype}")

#uppgift 4
print("\nUppgift4")
a= numpy.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
reshapedA = a.reshape(-1) # -1 = "plattar" arrayen
print(reshapedA)

#uppgift 5
print("\nUppgift5")
piArray = numpy.empty(101, dtype="float64")
maxValue = numpy.pi
rangeCenter = 50
piIntervall = maxValue / rangeCenter #är relativt säker att centret måste vara 0, alltså att det går från - till + 

for i in range(1, rangeCenter+1): #så att i börjar med 1 så att värdet inte multipliceras med 0
    value = piIntervall * i
    piArray[rangeCenter-i] = -value
    piArray[rangeCenter+i] = value
piArray[50] = 0
print(piArray)