## Overview

Click [HERE](https://github.com/stackanna/surfs_up./blob/946f4f0c7de001bd02c4259827e2edbb00649300/SurfsUp_Challenge.ipynb) to view [Surfs Up Module Challenge](https://github.com/stackanna/surfs_up./blob/946f4f0c7de001bd02c4259827e2edbb00649300/SurfsUp_Challenge.ipynb)

W. Avy hired us to unveal temperature trends before opening the surf shop In Oahu Hawaii. In specific he wants temperature data for the months of June and December in order to determine if the surf and ice cream shop business is sustainable year-round.

# Resources & Data systems used: Python, Pandas functions and methods, and SQLAlchemy. 

# Overview of Analysis:

We filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December. We converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics for the first part of our mission.

![alt text](https://github.com/stackanna/surfs_up./blob/946f4f0c7de001bd02c4259827e2edbb00649300/December%20Temperatures.png)


# Results

- Our findings showed that there was a minimal difference in temperatures between the months of June & December. Varying slightly at a mean temperature of three degrees. That shouldnt impact the difference of ice cream sales significantly in the month of December, especially compared to many other areas of the world in the winter time. 


![alt text](https://github.com/stackanna/surfs_up./blob/676b6a290703d0826bcda9cc48375534d660b3f8/June%20Temperatures.png)

- The maximum temperatures during the months of December and June in Oahu came in at a variance of only two degrees. That is very minimal difference for summer and winter months. Two degrees should not make a noticible effect on anyone wanting ice cream during the winter months. 

- The minimum variance between temperatures comes in at 8 degrees difference with the minimum being 56 degrees in December while the minimum is 64 degrees. While it is noticible, it isn't impactful.  

# Summary: 

There is only a slight variance between temperatures between the months of July & December in Oahu Hawaii. I believe an ice cream shop should not see a difference in sales during the winter months and can sucessfully operate year round. The slightest difference was in the maximum temperatures while the largest was in the minimum temperatures. 
