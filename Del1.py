import numpy

#Uppgift 1

integerArray = numpy.array([1,2,3], dtype="i") #dtype="i" är int32 det går att skriva dtype="int64" ifall man vill 64 bit integers, men i detta fall så är int32 mycket mer en vad som behövs 
floatArray = numpy.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0], dtype="f") #samma som int går det att skriva dtype="float64"
print(integerArray.dtype) #int32
print(floatArray.dtype) #float32

#Uppgift 2


