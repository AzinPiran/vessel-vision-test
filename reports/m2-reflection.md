# Vessel Vision Dashboard Reflection

## **1. Implemented part of M1 Proposal**

We have basically implemented all the features proposed in the M1 proposal, including the Number of Arrivals & Departures per Port table, the Total Number of Unique Vessels, Moving Vessels, and Anchored Vessels cards, the Maximum Time Anchored card, and the Activity Map, with data filtering base for January 1st.

However, based on the discussion in the lab and the teacher's feedback, we did remove the "comparison" part from the dashboard. Initially, we planned to present a comparison between December 31st and January 1st in the dashboard. However, since there is only one day of data, the comparison is not very meaningful. Additionally, using dates as a line chart representation is quite uncommon. Given the large dataset, it is challenging to include multiple dates at this stage of the project. 

As a result, we decided to use a radio button to represent the selected day, and symbolize the potential to scale to more days.

Specifically, for the **Number of Arrivals & Departures per Port**, filtering by Nearest Port does not return data. Logically, if the intent is to view the total Number of Arrivals & Departures for a specific port, there is no need for filtering, as this information is already displayed in the component. Additionally, for anchored vessels, no data is returned either, as they do not have Arrivals or Departures events.

## **2. Not-yet-implemented part of M1 Proposal**

A graph which represented days with different colours in the legend, which would have potentially led to high dimensionality, has been scrapped from development.

## **3. Reflection on Best Practices of Effective Visualizations**

We have generally followed the best practices of effective visualizations, using the Bootstrap grid for a clean and structured layout and employing vibrant colors for visual guidance. 

Given the simple and clear overall design, we believe it will be easy for the audience to read and interpret.

## **4. Achievements, Limitations, and Future Potential**

We have created four data filters, with the remaining six components dynamically updating based on user input, resulting in a rich and interactive experience. 

However, one limitation is the multiple filters, such as filtering by vessel name after selecting a nearest port. As vessel routes and cargo types are generally fixed, the ships appearing near a port are relatively consistent, making such filter combinations possibly not that meaningful. 

In the future, we may explore incorporating more dates to further visualize the impact of different time periods.
