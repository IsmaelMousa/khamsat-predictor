# Khamsat Predictor

Utilizing web scraping and machine learning techniques to accurately
predict <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>
service
prices. 

Read the official paper: [khamsat predictor paper](paper.pdf).

> [!IMPORTANT]
>
> The data utilized in this project is the property of
> the <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>
> platform, with all associated rights reserved to
> them. This project, however, is an independent endeavor and solely owned by me, with no affiliation to any institution
> or organization.
>

## Overview

Present the **Khamsat Predictor**, a machine learning model designed to address challenges in the freelance marketplace.
By analyzing data
from <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>,
the largest platform for Arab freelancers, the predictor
offers accurate
price estimates based on service characteristics. This ensures transparency, fosters trust, and alleviates price-related
anxiety for both sellers and clients. The model integrates classical machine learning techniques, employing structured
methodologies from data collection to deployment.

https://github.com/user-attachments/assets/9e36ea66-0ea7-42d9-af46-dbe825b250a1

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

> [!NOTE]
>
> You can find the exploratory data analysis (EDA), data preprocessing, modeling phases in the [notebooks](notebooks) directory.
>

## Modules

This shows the project's skeleton.

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

#### Follow the instructions bellow to use the Khamsat Predictor:

1. Clone this repository to your local machine:

```zsh
git clone git@github.com:IsmaelMousa/khamsat-predictor.git
```

2. Navigate to the khamsat-predictor directory

```zsh
cd khamsat-predictor
```

3. Setup virtual environment

```zsh
python3 -m venv .venv
```

4. Activate the virtual environment

```zsh
source .venv/bin/activate
```

5. Install the required dependencies

```zsh
pip install -r requirements.txt
```

6. Run the server program

```
uvicorn main:app --host localhost --port 8080
```

7. Navigate to [http://localhost:8080](http://localhost:8080), and start using it.

--- 

## Acknowledgments

I'm grateful to [Prof. Adnan Salman](https://scholar.google.com/citations?user=MXOIQ3cAAAAJ&hl=en)
and [Eng. Samer Huwari](https://www.linkedin.com/in/samerhuwari) for their fruitful
comments, corrections and inspiration.
