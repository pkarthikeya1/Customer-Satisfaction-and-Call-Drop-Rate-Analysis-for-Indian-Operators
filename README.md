# Customer Satisfaction and Call Drop Rate Analysis for Indian Telecom Operators


##
![Customers](Plots/Average%20customer%20ratings%20for%20call%20quality%20for%20different%20states%20from%202021%20till%202024.png)

![Customer Satisfaction](Plots/Overall%20call%20drop%20percentage%20for%20each%20operator.png)

## Summary of Insights

### Call Drop Rate:


#### Overall
Call drop rates decreased from 2021 to 2023. MTNL had the highest rate (26.76%), while VI had the lowest (6.68%).

#### RJio 
1. RJio's call drop rates peaked in August 2021 (37.66%) and were lowest in November 2023 (1.21%). The operator consistently experienced higher drop rates in Q2 and Q3 over the three-year period.

2. RJio experienced a 99% call drop rate anomaly in Himachal Pradesh during 2021 from May, requiring further investigation due to limited data. Delhi (October 2021, 0.3%) and Chhattisgarh (February 2021, 0.75%) had the lowest drop rates.

#### Airtel
1. Uttarakhand in 2021 recorded the highest call drop % with 35, but it picked tremendously from then in the next two years with <1% drop rate.

2. Apart from Uttarakhand which had both highest and lowest call drop rates, Kerala had the second lowest overall in three years with 0.67% in 2021. 
 

### Average Rating:

#### Overall
1. Overall highest average customer rating is achieved by VI with 4.3/5 and the lowest average customer rating goes to MTNL with 2.51/5.

2. Statewise, Chhattisgarh possess the highest average customer rating with 4.86/5, followed by Madhya Pradesh with 4.72/5 & Kerala with 4.64/5.

#### RJio
1. For RJio, Chhattisgarh consistently excelled with average ratings above 4.5/5 from 2021-2023. 


![Chattisgarh](Plots/RJio%20Average%20Rating%20for%20Chhattisgarh.png)


2. Karnataka maintained a strong performance above 4/5. Andhra Pradesh declined significantly, from 2.93 to 1.5. Arunachal Pradesh showed the most dramatic improvement, rising from 1 to 5.

#### Airtel
1. Airtel's peak performance was in August 2022 (4.8/5), followed by February 2023 (4.72/5). Ratings declined since June 2023 (4.39/5). 
![Airtel average ratings across years](Plots/Airtel%20average%20rating%20across%20years.png)

2. Madhya Pradesh led in 2022 (5/5), while Jharkhand topped in 2023 (4.78/5).

3. There was a steep dip in ratings in May 2023 which have 1.84/5 ratings, lowest of all the years Airtel has seen.Most of these are coming from Maharashtra, specifically of 4G network

## Recommendations & Next steps:
 ### RJio : 
 1. Investigate the anamoly of high call drop rates in Himachal Pradesh, whether there is an issue with the network congestion or is there any natural calamity happened which resulted in destruction of infrastructure. To further narrow down, should have geodecoding that can result in area/district specific call drop rates.

 2. To get to the in detailed picture and more clarity, there should be more effort in collecting the feedback with as 70% of the feedback corresponds to only 2021.

 3. Further stregthen the network in Chhattrisgarh and Karnataka and not to lose to the competition. Also, understand how these regions are getting very good ratings, meet with the operations team to use the case study for other states

### Airtel :
1. Investigate Network Upgrades in Maharashtra: Examine if the dip in performance is due to network upgrades, requiring more detailed information than just the state name.

2. Analyze Madhya Pradesh's and Uttarakhand Strategy: Study the operational team’s strategy in Madhya Pradesh to identify successful practices.





- #### Caveat : For the above insights, we have considered only the states which have atleast 1000 samples overall, there are some states which have 5 star rating overall but with 10 samples, those were discarded from the analysis.



``` This dataset is sourced from the TRAI website and is used for academic purposes only. The author has no affiliation with any telecom operator. The insights presented are based on the author's analysis of the data and do not necessarily reflect the official position of any organization. While all efforts have been made to ensure data accuracy, the analysis is based on the available data as provided by TRAI and may contain errors or omissions.```
