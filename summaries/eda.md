# EDA Summary

Summarizes the exploratory data analysis, highlighting key findings, challenges encountered, decisions made,
and the next steps for further analysis.

## Overview

Introduction to the dataset, its structure, and relevant characteristics:

1. **Dataset**:
    * Language: arabic.
    * Size: 7818 rows, 26 columns.
    * Data Types: 11 numerical, 14 categorical, 1 boolean.
    * Missing Values: there is no missing.
    * Duplicated Values: there is no duplication.
    * Bias Exist: yes.


2. **Features**:
    * Category Name: name of the category under which the service is listed.
    * Category URL: link to the category main page which contains list of services.
    * Service Name: name of the service being offered.
    * Service URL: link to the service main page which contains list of offers.
    * Offer Name:  name of the specific offer.
    * Offer URL: link to the offer main page.
    * Offer Stars: average rating in stars from 5 given to the offer.
    * Offer Raters: number of users who have rated the offer.
    * Offer Response Time: average time it takes to respond to inquiries for the offer.
    * Offer Buyers: number of people who have purchased the offer.
    * Pending: number of pending orders or requests for the offer.
    * Price: cost of the offer in $USD.
    * Duration: offer's delivery time to the client.
    * Reviews: number of feedback provided by clients who have used the offer.
    * Available Additions: number of available additional features that can be added with the offer.
    * Additions Price: total price of the additional features, without the original price.
    * Owner Name: name of the person offering the offer (seller).
    * Owner URL: link to the owner's main page.
    * Owner Verified: indicates whether the owner has been verified
    * Owner Level: owner's level or rank in the system.
    * Owner Stars: average rating in stars from 5 given to the owner.
    * Owner Raters: number of users who have rated the owner.
    * Owner Completion Rate: percentage of completed/delivered services by the owner.
    * Owner Services: number of services offered by the owner.
    * Owner Customers: number of clients the owner has served.
    * Owner Response Time: average time it takes for the owner to respond to inquiries.


3. **Data Types**:
    * Category Name: object.
    * Category URL: object.
    * Service Name: object.
    * Service URL: object.
    * Offer Name:  object.
    * Offer URL: object.
    * Offer Stars: float.
    * Offer Raters: integer.
    * Offer Response Time: object.
    * Offer Buyers: integer.
    * Pending: integer.
    * Price: object.
    * Duration: object.
    * Reviews: integer.
    * Available Additions: integer.
    * Additions Price: integer.
    * Owner Name: object.
    * Owner URL: object.
    * Owner Verified: bool.
    * Owner Level: object.
    * Owner Stars: float.
    * Owner Raters: integer.
    * Owner Completion Rate: object.
    * Owner Services: integer.
    * Owner Customers: integer.
    * Owner Response Time: object.


4. **Missing Values**:
   * There are no direct missing values like NaN, but there are values that are considered missing, such as:
     1. ."لم يحسب"
     2. ."لم يحسب بعد"
     
   * Features:
     1. Offer Response Time: 1806 of "لم يحسب" values.  
     2. Owner Response Time: 1258 of "لم يحسب" values.
     3. Owner Completion Rate: 1362 of "لم يحسب بعد" values.


5. **Target**:
    * Price: cost of the offer in $USD.
      1. Min Price: $5.
      2. Max Price: $50.
      3. Intervals: the price intervals are $5.



## Insights
Observations discovered through data exploration:

1. **Most Frequent Values**:
   * Price: $5.
   * Category: "برمجة وتطوير".
   * Duration: "يوم واحد".
   * Offer Response Time: "لم يحسب".
   * Owner Response Time: "لم يحسب".
   * Owner Completion Rate: 100%.
   * Offer Stars: 5.0.
   * Owner Stars: 5.0.
   * Owner Level: "بائع مميز".


2. **Outliers Counts**:
   * Offer Stars: 0.
   * Offer Raters: 867.
   * Offer Response Time: 804.
   * Offer Buyers: 988.
   * Pending: 425.
   * Price: 856.
   * Duration: 916.
   * Reviews: 0.
   * Available Additions: 0.
   * Additions Price: 506.
   * Owner Stars: 1711.
   * Owner Raters: 815.
   * Owner Completion Rate: 432.
   * Owner Services: 523.
   * Owner Customers: 812.
   * Owner Response Time: 719.


3. **Top Correlations (Pearson's R  With Price)**:
   * Service Name: 44.16%
   * Additions Price: 30.80%
   * Owner Level: 29.33%
   * Owner Services: 24.32%
   * Owner Raters: 19.57%
   * Owner Customers: 17.40%
   * Owner Stars: 15.79%
   * Category Name: 14.54%
   * Reviews: 13.95%

   
## Challenges
Data issues, limitations, and obstacles encountered during the analysis:

1. **Data Size**: the data size is a bit small, but so far it is acceptable.


2. **Data Missing**: I've mentioned above that there are no direct missing values like NaN, but there are values that are considered missing, such as: "لم يحسب" and "لم يحسب بعد", and if we calculate the percentage of samples sharing these values relative to the total data size is **15.41%** which is large.


3. **Data Formats**: some features that have a numerical meaning are recorded as text, such as:
   1. Price.
   2. Duration.
   3. Offer Response Time.
   4. Owner Response Time.
   5. Owner Completion Rate.


4. **Data Bias**: there is a reasonable bias in the data.

## Decisions

Actions and strategies will be decided based on the exploratory analysis:

1. **Mapping Utility**: build a utility to convert text-based values into numerical values.


2. **Missing Data Imputation**: experiment with different imputation techniques to identify the most effective method for handling missing data.


3. **Feature Selection**: apply unsupervised learning techniques to identify the most relevant features.


4. **Feature Scaling**: apply feature scaling using the most suitable technique to standardize the data values.


5. **Handling Biased Data**: use unsupervised learning methods to detect and address biased or outlier values.


6. **Encoding Categorical Features**: select the appropriate encoding technique based on the characteristics of the categorical features.

## Next

Planned next steps or tasks to move forward with the exploratory data analysis.

1. **Missing Data Imputation**:
   1. One-Hot Encoding (for categorical features).
   2. KNN Imputation (for numerical features).
   3. Visualize the distributions of Offer Response Time, Owner Response Time, and Owner Completion Rate after imputation.
   

2. **Feature Selection**:  use unsupervised learning techniques (such as *PCA* or feature importance methods) to determine the most relevant features.


3. **Handling Biased Data**: use *Isolation Forest* for anomaly detection to identify and address biased or outlier values.







