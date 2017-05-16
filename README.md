# CarSalesPrediction

Given car sales data, reviews data over the past ten years, we build a model to predict the sales volume for each car.

## Procedure of Our Work

### 1 Data PreProcessing
#### 1.1 Data Source
1) Dealing with the data given</br>
2) Crawling Data from the Internet
#### 1.2 Data Transformation
1) Concert string values into num values</br>
2) Convert Attribute with multi values into Multi Attributes with single values</br>
3) Data Normalization
#### 1.3 Data Cleaning
1) Noise & Outlier Data Detection 
#### 1.4 Data Integration
1) Join Tables on 'car_id'

### 2 Feature Engineering
1) car_bd_index - monthly average baidu index for each car </br>
2) car_comment - monthly average number of bbs comments for each car </br>
3) car_info - each car info </br>

### 3 Model Selection & Training Models
1) Linear Method: Linear Regression</br>
2) Probability Method: Bayes Regression</br>
3) Neural Network Method: Multilayer Perceptron Regression (MLPR)</br>

### 4 Result Evaluation
1) Mean Square Error</br>

## Project File Structure
1) data/ - Data given & Data crawled on the Internet</br>
2) src/ - source code</br>
3) outputs/ - outputs</br>
