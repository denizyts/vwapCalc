# Volume Weighted Average Price Indicator

This script allows you to calculate *vwaps* of lists.

If you have any problem send mail to me by using the adress on my profile
*https://github.com/denizyts*

## Table of Contents

- [Why I Implement this VWAP ?](#Why)
- [Details](#Details)
- [Installation](#Installation)
- [Dependencies](#Dependencies)
- [Example Usages](#usage)


## Why I Implement this VWAP ?
At the public codespace there are many libraries for technical analysis but many of them do not have the vwap indicator, some libraries contain vwap but those ones have defects.
Thats why i code the vwap by my own, actually it is very useful if you check my *Backtester* repository (https://github.com/denizyts/Backtester/blob/main/src/strategy.py) there is a strategy class which i used this vwap for trend detection.

## Details

Source: https://www.howthemarketworks.com/volume-weighted-average-price/

The difference between V1 and V2 is return type, V1 returns just a serie which contains vwap value, V2 returns a df which contains upper and lower bands for vwap.

Please check *Example Usage* at the below.


# Installation

Clone the repository with git:

*git clone https://github.com/denizyts/Backtester.git*

or just download the zip.

## Dependencies
Latest versions probably will be enough.

- *Python 3.11.8*
- *pandas 2.1.2*
- *numpy 1.26.0*


## Example Usage of V1

*vwap = vwapCalc.Calculate("Highest Price" , "Lowest Price" ,*
                                                      *"Close Price", "Volume" , anchor = 10);*

Return type is serie.



## Example Usage of V2
*import vwapCalcV2*

*vwap_df = vwapCalcV2.Calculate("Highest Price" , "Lowest Price" ,*
                                                      *"Close Price", "Volume" , anchor = 10 , stdev_multp = 0.1);*

The df has 3 columns those columns are *'vwap'* *'upper_band'* *'lower_band'*












