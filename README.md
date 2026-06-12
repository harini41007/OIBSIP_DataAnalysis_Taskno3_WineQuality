# Wine Quality&nbsp;&nbsp;

### Objective

The objective of this project is to analyze the wine quality dataset and develop a machine learning model capable of predicting wine quality based on its chemical properties.The project aims to preprocess the data,explore key features such as acidity,density,and alcohol content,and convert the quality scores into binary classification problem(good or bad wine). Multiple machine learning algorithms, including Random Forest,Support Vector Classifier(SVC),and SGD Classifier,are applied and compared to identify the most accurate model. Overall,the goal is to build an efficient and reliable predictive model that can assist in assessing wine quality without manual evaluation

### Sample Dataset

<img width="1318" height="448" alt="image" src="https://github.com/user-attachments/assets/6d7f7832-e2b7-4763-889e-c6621a00eaf8" />



### Dataset Overview
+ The dataset used in this project contains chemical properties of wine samples and is commonly used for predicting wine quality
+ Each row represents a wine sample,and each column corresponds to a specific chemical attribute that influences the taste and quality of the wine
+ Each sample is labeled with quality score, which is converted into binary classification (good or bad wine).
+ The dataset is used to build machine learning models to predict wine quality based on its features
 ### Tools and technologies
  The following tools and technologies were used for developing the Wine quality Prediction model:
 
1.Google Colab is used as:
+ Cloud-based environment for running Python code
+ No need for local installation
+ Easy to share and run notebooks

2.Python
+ Python is the core programming language used in this project
+ It provides strong support for data analysis,visualization,and machine learning

3.Pandas
Pandas is used for:
+ Loading the dataset
+ Cleaning and preprocessing data
+ Handling missing values and duplicates
+ Performing data manipulation

4.NumPy
NumPy is used for:
+ Performing numerical computations
-+ Handling arrays and mathematical operations

5.Matplotlib
Matplotlib is used to:
+ Create basic visualizations
+ Plot graphs like charts and distributions

6.Seaborn 
Seaborn is used for:
+ Advanced and attractive visualizations
+ Creating count plots andheatmaps

7.Scikit-learn
Scikit-learn is used for building and evaluating models:
+ train_test_split
+ RandomForestClassifier
+ SVC(Support Vector Classifier)
+ SGD Classifier
+ Accuracy_score
  
                                                
                                             
### Steps in wine Quality Prediction
    
1.Import Libraries
 + Pandas -> data handling
 + NumPy -> numerical computations
 + Seaborn&Matplotlib -> visualization

2.Load dataset 
 + Loaded the dataset using 'pandas.read_csv()'

3.Data Exploration
 + Checked missing values using 'df.isnull.sum()'
 + Checked duplicate rows and removed them if present
 + Viewed dataset information using 'df.info()'

4. Data Visualization
 + Plotted wine quality distribution using countplot
 + Created correlation heatmap to analyze relationships between features

5.Data Transformation
 + Converted wine quality into binary classification:
 + 1 -> Good Quality(quality>7)
 + 0 -> Bad/Average Quality (quality <7)

6. Define Feature and Target
 + Features(X) -> all columns except 'quality'
 + Target (Y) -> 'quality' column

7.Train-Test Split
 + Split data into Training (80%) and Testing (20%)

8.Model Training

Three machine learning models were trained:

1. Random Forest Classifier-Ensemble model using multiple decision trees

2. Support Vector Classifier (SVC)-Separates data using decision boundaries

3. SGD Classifier -Efficient for large -Scale datasets

9.Model Evaluation
 + Predicted results on test data
 + Calculated accuracy using'accuracy_score'
 + Stored accuracy of each model in a dictionary
 + Printed results to identify the best -performing model

10. Feature Importance
 + Used Random Forest to determine which features are most important
 + Visualized feature importance using a bar chart

11. Prediction on New Data
 + Provided a sample wine input
 + Used trained model to predict quality
 + Displays good quality wine or bad quality based on testing data

 ### Outcome

   <img width="533" height="212" alt="image" src="https://github.com/user-attachments/assets/4fea43d9-a60f-4782-9d8f-60636c8e98dc" />



 + The wine quality prediction model was successfully developed and evaluatued using mutiple machine learning algorithms.The models were able to classify wines into good and bad quality based on their chemical properties.
 + Among the models tested,Random Forest Classifier achieved the highest accuracy,making it the most effective models for this dataset. This indicates that ensemble methods perform well in capturing complex relationships between wine feature and quality
 + Visualization, such as the quality distribution plot and correlation heatmap,helped in understanding the data patterns and relationships between differnt features.The feature importance analysis furthur revealed that certain attributes like alcohol,sulphates,and acidity play a significant role in determining its practical usability
 + THe model was also tested with sample input,and it successfully predicted whether the wine is good or bad quality,demonstrating its practical uasability.
  + Overall,the project  shows that machine learning techniques can effectively predict wine quality and reduce the need for manual training
