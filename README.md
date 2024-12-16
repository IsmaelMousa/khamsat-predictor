# Khamsat Predictor

Utilizing web scraping and machine learning techniques to accurately predict [khamsat.com](https://khamsat.com/) service
prices.

> [!IMPORTANT]
>
> The data utilized in this project is the property of the Khamsat platform, with all associated rights reserved to them. This project, however, is an independent endeavor and solely owned by me, with no affiliation to any institution or organization.
> 


## Overview

Present the **Khamsat Predictor**, a machine learning model designed to address challenges in the freelance marketplace.
By analyzing data from [khamsat.com](https://khamsat.com/), the largest platform for Arab freelancers, the predictor
offers accurate
price estimates based on service characteristics. This ensures transparency, fosters trust, and alleviates price-related
anxiety for both sellers and clients. The model integrates classical machine learning techniques, employing structured
methodologies from data collection to deployment.

## Objective

The goal is to develop an AI-based pricing model that predicts accurate prices for freelance
services listed on Khamsat. By analyzing historical data from the platform, the model helps both sellers and clients
make
informed decisions.

## Workflow

The project follows a structured strategy with five key phases:

1. **Data Collection**: Data was scraped from Khamsat using Selenium to handle dynamic elements and navigate through
   menus.
2. **Exploratory Data Analysis (EDA)**: Key patterns were uncovered in the data, identifying correlations and resolving
   format inconsistencies.
3. **Data Preprocessing**: Placeholder values were cleaned, and categorical features were encoded.
4. **Modeling**: Various classical machine learning models (such as SoftMax Regression, Support Vector Classifier, and
   Random Forest Classifier) were trained and optimized.
5. **Deployment**: The trained models were deployed using FastAPI, providing a user-friendly interface for price
   predictions.

## Modules
The project files should be like this.
```zsh
khamsat-predictor
 ├── data
 │   ├── raw
 │   ├── balanced.csv
 │   ├── clean.csv
 │   ├── raw.csv
 │   └── scraper.py
 ├── experiments 
 │   ├── Random Forest Classifier
 │   │   └── 0
 │   │       ├── balanced
 │   │       ├── imbalanced
 │   │       └── meta.yaml
 │   ├── SoftMax Regression
 │   │   └── 0
 │   │       ├── balanced
 │   │       ├── imbalanced
 │   │       └── meta.yaml
 │   └── SVC
 │       └── 0
 │           ├── balanced
 │           ├── imbalanced
 │           └── meta.yaml
 ├── mappers 
 │   ├── to_categorical
 │   │   └── feature_names.json
 │   ├── to_numeric
 │   │   ├── category_name.json
 │   │   ├── duration.json
 │   │   ├── offer_response_time.json
 │   │   ├── owner_level.json
 │   │   ├── owner_response_time.json
 │   │   └── service_name.json
 │   ├── __init__.py
 │   ├── features.py
 │   ├── load_and_map.py
 │   └── one_hot.py
 │   
 ├── models 
 │   ├── __init__.py
 │   └── offer.py
 ├── notebooks
 │   ├── eda.ipynb
 │   ├── preprocessing.ipynb
 │   └── modeling.ipynb
 ├── routers
 │   ├── __init__.py
 │   └── offer.py
 ├── views
 │   ├── images
 │   ├── index.html
 │   ├── index.js
 │   └── style.css     
 ├── .gitignore
 ├── LICENSE.md
 ├── main.py
 ├── README.md
 ├── requirements.txt
 └── requirements-dev.txt
```



Here is a summary for the purpose of each major module or component in the project.

|         Module         | Purpose                                                                                                                                                                                       |
|:----------------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         `data`         | Contains the scraper utility for extracting data and the files representing datasets used in the project.                                                                                     |
|     `experiments`      | Stores the results of experiments, including trained models, hyperparameter configurations, and the metrics associated with their performance.                                                |
|       `mappers`        | Handles the transformation of text-based data into numerical formats, including custom encoding techniques for model compatibility.                                                           |
|        `models`        | Contains Pydantic models (schemas) used for data validation and serialization between different layers of the application.                                                                    |
|      `notebooks`       | Includes Jupyter notebooks that illustrate the workflow across the three phases: data exploration, preprocessing, and modeling, offering a clear representation of the project’s progression. |
|       `routers`        | Manages API route definitions, linking frontend requests to backend functionalities, including data processing and prediction endpoints.                                                      |
|        `views`         | Responsible for rendering frontend templates or static files, providing the visual interface for interacting with the application.                                                            |
|       `main.py`        | Serves as the project's entry point, initializing the application and orchestrating its components.                                                                                           |
|   `requieremnts.txt`   | Lists the dependencies required to run the application, ensuring that all necessary libraries and tools are installed.                                                                        |
| `requierments-dev.txt` | Specifies additional dependencies for development purposes.                                                                                                                                   |

## Technologies

This table shows the technologies and tools that are used in Khamsat Predictor.

|    Dependency     | Usage                                                                                                               | Phase              |
|:-----------------:|---------------------------------------------------------------------------------------------------------------------|--------------------|
|    `selenium`     | Used to interact with Khamsat website and collect (scrap) dynamic content.                                          | Data Collection    |
|     `mlflow`      | Managing the machine learning lifecycle and operations (MLOps), including experiment tracking and model management. | Modeling           |
|     `optuna`      | Used to Tune and optimize model hyperparameters for better performance.                                             | Modeling           |
|  `scikit-learn`   | Implementing the mathematical formulations and implementations of the models.                                       | Modeling           |
|     `pandas`      | Used for handling datasets, cleaning, and preprocessing the data.                                                   | EDA, Preprocessing |
|      `numpy`      | Used for working with arrays and mathematical operations in data processing.                                        | Preprocessing      |
|   `matplotlib`    | Creating plots and graphs for visualizing trends in the data.                                                       | EDA                |
|     `seaborn`     | Used for more advanced and aesthetically pleasing plots.                                                            | EDA                |
| `arabic_reshaper` | Reshaping Arabic text, ensuring that it displays correctly when visualized in plots or graphs.                      | EDA                |
|   `python-bidi`   | Facilitates bidirectional text rendering, useful for displaying Arabic script.                                      | EDA                |
|     `fastapi`     | Used to build the interface for price prediction, allowing the model to interact with users in real-time.           | Deployment         |
|    `Bootstrap`    | Building responsive and visually appealing user interfaces.                                                         | Deployment         |
|   `JavaScript`    | Creating dynamic, interactive elements in the web interface.                                                        | Deployment         |
|       `CSS`       | Format the appearance of the web interface, including layout, colors, and fonts.                                    | Deployment         |
|      `HTML`       | Structure the web interface and content for price prediction.                                                       | Deployment         |

## Results

The project successfully identified key correlations in the dataset, such as the impact of **Service Name**, **Additions
Price**, and **Owner Level** on the price prediction. After cleaning the data and addressing missing values, several
models were trained, and the SVC showed the best performance in terms of accuracy and F1 score. The
model is now capable of providing price predictions based on offer features with high accuracy.

The table here presents the results for each model.

| **Model**                | **Loss** | **Accuracy** | **Precision** | **Recall** | **F1**  |
|:-------------------------|:--------:|:------------:|:-------------:|:----------:|:-------:|
| SoftMax Regression       |   0.95   |     68%      |      66%      |    68%     |   67%   |
| SVC                      |   0.05   |   **98%**    |    **98%**    |  **98%**   | **98%** |
| Random Forest Classifier |   0.23   |     97%      |      97%      |    97%     |   97%   |

## Usage

To use the Khamsat Predictor, simply access the deployed FastAPI interface, where you can input key features of a
service offer, and the model will predict the price for you. The platform ensures seamless and real-time price
predictions based on the features you provide.

[![Subtitle](https://readme-typing-svg.demolab.com?font=Helvetica&weight=600&size=15&pause=1000&color=64B5F6&random=false&width=435&lines=khamsat-predictor.com)](https://github.com/IsmaelMousa/TTL)