# surfs_up

## Project Overview

In this project I am tasked with assisting a friend,  W.Avy, to assess weather data for a prospective location that he is wanting to examine prior to opening an ice cream and surf shop on the Island of Oahu. W.Avy may want to open other shops around the islands so he has requested that the work be well documented and easy to duplicate the next time we may want to analyze a new location. SQLite was used to store the weather data provided by W.Avy while utilizing SQLAlchemy to connect to the data. Since surfing activities and ice cream sales will be driven by warm, sunny weather, W.Avy wants to analyze the precipitation levels as higher occurences of rain will yield negatively impact potential revenue. The weather data provided by W.Avy was converted into a database and then sorted by date and limited to the previous year's data. Matplotlib was used to create visuals for his upcoming board meeting that would accurately reflect the weather patterns in Oahu. Beyond plotting the precipitation patterns, W.Avy needed statistical analysis of the precipatation figures for the year. I expanded upon his request to also include temperature figures and to convert this into a histogram to display the previous year's temperature data. In order to ensure the data was accessible for the board members, I had to utilize Flask in order for the information to be accessible via a website. For Deliverables 1 and 2 W.Avy requested to have weather analyzed for June and December to assess the year-round viability of the business. 


## Results
June
![alt text](https://github.com/bwengerDU/surfs_up/blob/main/Deliverable%201.png)
December
![alt text](https://github.com/bwengerDU/surfs_up/blob/main/Deliverable%202.png)

-June's average temperate is roughly 4 degrees warmer than December, coming in at 74.94 degrees and 71.04 degrees respectively. 

-December has far more variation in its temperatures. Although the average is only 4 degrees apart, the weather in December can range from 56-83 degrees compared to the 64-85 degree range in June. 

-The standard deviation in December is also nearly .5 higher in December. 


## Summary
Examining the ranges and deviations in weather for December may give W.Avy some concern as there may be a seasonal change in business potential. Although the differences in weather are seemingly minimal, they may have a major impact on the bottom line. What this means is that December has a far higher likelihood of adverse weather that could significantly impact business. June weather is more consistent and warmer. Examining temperatures is not sufficient enough to make any confident assessment for how business may vary between December and June. Precipitation patterns would be important to examine in order to further understand any business deterrent as a drop in 5 degrees temperature is significantly different whether that drop coincides with precipitation. Accumulation patterns would be important to understand as well. It would be good to know if any location is subject to weather patterns where a location has small, frequent precipitation or if it is subject to sporadic, large storms. While a location may experience 10" of rain in a particular month, it would be very helpful to understand if that would impact only a few days of business, or if it would be a more persistent issue. 

While examining the weather in greater detail may be helpful for W.Avy to understand when lulls may be expected to occur in business, he will want to run a multivariate analysis along with understanding general tourism patterns to prospective locations. December weather may be colder, but this may be offset by the fact that many tourists view Hawaii as a very desirable Christmas destination. Also, let's be honest, rain is not likely to be a major deterrent for those visiting Hawaii during certain times of the year. This is relevant more to those travelers coming from cold climates during the winter months. Gaining a stronger understanding of tourism trends alongside weather patterns would be the most beneficial route for W.Avy to predict and prepare for the fluctuations for any potential location. Ben may also want to examine how weather patterns are tied to swells and how surfing conditions would be tied to them. Some conditions may be less ideal for ice cream sales, but they may create more ideal surfing conditions. Despite the two business functions being driven by weather, Ben may want to delve deeper into each business faction to fully understand their driving success factors. 
