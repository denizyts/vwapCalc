
from queue import Queue
import numpy as np
import pandas as pd

"""
Source: https://www.howthemarketworks.com/volume-weighted-average-price/

if anchor equals 15 , first 15 index is none , other index's are float. 
"""

def Calculate(highestprices , lowestprices , closeprices , volume , anchor , stdev_multp):
 
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
  result = pd.DataFrame();
  vwap = []
  lower_band = [];
  upper_band = [];
  VolumeSum = 0         #stores sum of prev 15 volume data.
  PriceMultplicationVolumeSum = 0        
  PriceMultVolumeQueue = Queue(anchor)       

  for i in range(len(closeprices)):
  
   if(i < anchor):
    vwap.append(1);
    VolumeSum = VolumeSum + volume[i];
    currentPrice = ( highestprices[i] + lowestprices[i] + closeprices[i] ) / 3
    PriceMultVolumeQueue.put(volume[i]*currentPrice)
    PriceMultplicationVolumeSum = PriceMultplicationVolumeSum + (volume[i]*currentPrice)

   else:
   
    VolumeSum = VolumeSum + volume[i] - volume[i-anchor];
    currentPrice = ( highestprices[i] + lowestprices[i] + closeprices[i] ) / 3
    PriceMultplicationVolumeSum = PriceMultplicationVolumeSum + (volume[i]*currentPrice) - PriceMultVolumeQueue.get()
    PriceMultVolumeQueue.put(volume[i]*currentPrice)

    vwap.append(PriceMultplicationVolumeSum/VolumeSum)


  stdev = np.std(vwap , axis=0);
  upper_band = vwap + stdev*stdev_multp;
  lower_band = vwap - stdev*stdev_multp;
 
  result['vwap'] = vwap;
  result['upper_band'] = upper_band;
  result['lower_band'] = lower_band;
 
  return result;
 
 except Exception as e:
  print("vwapCalc:")
  print({e})
  exit()


