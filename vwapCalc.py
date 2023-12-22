
from queue import Queue

"""
Source: https://www.howthemarketworks.com/volume-weighted-average-price/

if anchor equals 15 , first 15 index is none , other index's are float. 
"""

def Calculate(highestprices , lowestprices , closeprices , volume , anchor):
 
 try:
  
  #avoid some exceptions.
  if(len(highestprices) != len(lowestprices) or len(highestprices) != len(closeprices) or len(lowestprices) != len(closeprices)):
   print("vwapCalc:")
   print("Lenghts of list parameters should be equal.")
   exit()
  if(len(volume) != len(highestprices) or len(volume) != len(lowestprices) or len(volume) != len(closeprices)): 
   print("vwapCalc:")
   print("Lenghts of list parameters should be equal.") 
   exit()
  if(anchor > len(volume)):
   print("vwapCalc:")
   print("Anchor can not be greater than length of other parameters.") 
   exit() 
  
  #calculation
  result = []
  VolumeSum = 0         #stores sum of prev 15 volume data.
  PriceMultplicationVolumeSum = 0        
  PriceMultVolumeQueue = Queue(anchor)       

  for i in range(len(closeprices)):
  
   if(i < anchor):
    result.append(None);
    VolumeSum = VolumeSum + volume[i];
    currentPrice = ( highestprices[i] + lowestprices[i] + closeprices[i] ) / 3
    PriceMultVolumeQueue.put(volume[i]*currentPrice)
    PriceMultplicationVolumeSum = PriceMultplicationVolumeSum + (volume[i]*currentPrice)

   else:
   
    VolumeSum = VolumeSum + volume[i] - volume[i-anchor];
    currentPrice = ( highestprices[i] + lowestprices[i] + closeprices[i] ) / 3
    PriceMultplicationVolumeSum = PriceMultplicationVolumeSum + (volume[i]*currentPrice) - PriceMultVolumeQueue.get()
    PriceMultVolumeQueue.put(volume[i]*currentPrice)

    result.append(PriceMultplicationVolumeSum/VolumeSum)


  return result
 
 except Exception as e:
  print("vwapCalc:")
  print({e})
  exit()

