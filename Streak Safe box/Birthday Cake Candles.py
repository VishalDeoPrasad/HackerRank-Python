'''
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
Example
The maximum height candles are  units high. There are  of them, so return .

'''

def birthdayCakeCandles(candles):
    # Write your code here
    maxCandle = candles[0]
    [maxCandle := candle for candle in candles if maxCandle < candle]
    tallest_candle = candles.count(maxCandle)
    return tallest_candle

result = birthdayCakeCandles([4,4,7,3,5,7,6,5])
print(result)