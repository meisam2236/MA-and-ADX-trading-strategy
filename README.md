# MA and ADX trading strategy
(*This is an old code! You may need to change some part of it...*)
This is a trading strategy based on three indicators: 

1. Simple Moving Average
2. Exponential Moving Average
3. Average Directional Movement index 

With collision of moving averages we can trigger sell and buy action; But it lacks somethings... Using moving averages in neutral flow leeds to inappropriate buy and sell actions. 
So I added ADX indicator to take actions in trends. Thus it leeds to better signals compared to simple moving averages! 

Install these four things:  
``` bash
	pip instal pandas
	pip install numpy
	pip install ta
	pip install matplotlib
```
Enjoy :wink:
