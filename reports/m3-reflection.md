# Vessel Vision Dashboard Reflection

## **1. Implemented part from M2**

We have now basically implemented all the features proposed in the M1 proposal.

Bsed on what we've done in M1, we updated the dashboard according to the suggestion from instructor and TA.

- Reduced file size to improve app loading speed.
- Minimized white space around the map and across the application.
- Modified the map legend for better readability.
- Ensured all application elements fit on a single page without requiring scrolling.
- Made the table responsive to filters, dynamically updating based on selected criteria.

### Trend of Unique Vessels Over Time

This component has been moved below the port table, and the footer and overall white space have been adjusted to ensure the entire page displays without scrolling. As it's dynamic, the table is now scrollable to maintain a clean and organized layout.

### Number of Arrivals & Departures per Por

This component has been modified into a dynamic table that returns results based on the applied filters. Additionally, it reflects the effect of multiple filters simultaneously. 

For example, in the default state with no filters applied, it displays all values; when filtering for the Port of Vancouver, it returns only the departure and arrival data for Vancouver; when filtering for both the Port of Vancouver and the Cargo vessel type, it displays only the departure and arrival data for cargo vessels at Vancouver.

## **2. Corner case**

However, that being said, it may still be slow on render. If it is too slow for you may you please continue to consider viewing on local.

## **3. Reflection on Best Practices of Effective Visualizations**

We have generally followed the best practices of effective visualizations, using the Bootstrap grid for a clean and structured layout and employing vibrant colors for visual guidance. We added an excellent background colour to reduce whitespace additionally and enhance the visual aesthetics of our dashboard

Given the simple and clear overall design, we believe it will be easy for the audience to read and interpret.

## **4. Achievements, Limitations, and Future Potential**

We have created two data filters, with the remaining seven components dynamically updating based on user input, resulting in a rich and interactive experience. 

In the future, we may explore incorporating more dates to further visualize the impact of different time periods.
