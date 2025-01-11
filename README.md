# Khamsat Predictor

Utilizing web scraping and machine learning techniques to accurately
predict <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>
service
prices.

[Data-Driven Optimization of Pricing Strategies on Microservice Platforms: Insights From Khamsat](paper.pdf)

## Overview

Present the **Khamsat Predictor**, a machine learning model aimed at addressing challenges in the freelance marketplace.
By analyzing data
from <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>,
the largest platform for Arab freelancers, the model provides price estimates based on service characteristics. While
the current version faces challenges like data limitations and overfitting, it offers a foundation to improve
transparency and help alleviate price-related concerns for both sellers and clients. The model employs classical machine
learning techniques and follows structured methodologies for data collection, training, and deployment, with plans for
future enhancements through better data acquisition and advanced techniques.

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
> You can find the exploratory data analysis (EDA), data preprocessing, modeling phases in the [notebooks](notebooks).
>

## Modules

This shows the project's skeleton.

```zsh
khamsat-predictor
 ├── charts
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
 ├── paper.pdf
 ├── README.md
 ├── requirements.txt
 └── requirements-dev.txt
```

Here is a summary for the purpose of each major module or component in the project.

<details>
  <summary>Click to see</summary>

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
|      `paper.pdf`       | Provides a detailed overview of the project, including its objectives, methodology, experiments, results, and conclusions, serving as the primary documentation.                              |
|   `requieremnts.txt`   | Lists the dependencies required to run the application, ensuring that all necessary libraries and tools are installed.                                                                        |
| `requierments-dev.txt` | Specifies additional dependencies for development purposes.                                                                                                                                   |
|        `charts`        | Contains the images of all charts/plots.                                                                                                                                                      |

</details>

## Technologies

Technologies and tools used.


<div align="center">

<a href="https://selenium-python.readthedocs.io" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Selenium" title="Selenium" height="30"></a>
<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" title="FastAPI" height="30"></a>
<a href="https://scikit-learn.org" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit-Learn" title="Scikit-Learn" height="30"></a>
<a href="https://pandas.pydata.org" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" alt="Pandas" title="Pandas" height="30"></a>
<a href="https://numpy.org" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1200px-NumPy_logo_2020.svg.png" alt="NumPy" title="NumPy" height="30"></a>
<a href="https://matplotlib.org" target="_blank"><img src="https://www.jumpingrivers.com/blog/customising-matplotlib/matplot_title_logo.png" alt="Matplotlib" title="Matplotlib" height="30"></a>
<a href="https://seaborn.pydata.org" target="_blank"><img src="https://seaborn.pydata.org/_images/logo-wide-lightbg.svg" alt="Seaborn" title="Seaborn" height="30"></a>
<a href="https://mlflow.org" target="_blank"><img src="https://mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" alt="MLflow" title="MLflow" height="30"></a>
<a href="https://optuna.org" target="_blank"><img src="https://raw.githubusercontent.com/optuna/optuna/master/docs/image/optuna-logo.png" alt="Optuna" title="Optuna" height="30"></a>
</div>



Here is a summary for the purpose of each tool used in the project.

<details>
  <summary>Click to see</summary>

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

</details>


## Experiments

In this project, we adopt a multimodal approach, evaluating and optimizing several machine
learning algorithms through hyperparameter tuning. The experiments carried out aimed to
evaluate model performance on both the original imbalanced dataset and a balanced version
created by random oversampling. Both experimental setups were tracked using MLflow library, ensuring
reproducibility and optimization of the model workflows.

Optuna library was used for hyperparameter optimization, conducting
up to 50 trials for each model to maximize the F1-score. Tables 1 and 2 summarize
the hyperparameters tuned for each model.

**Table 1: Hyperparameters tuned on the original clean imbalanced dataset.**

|  **Hyperparameter**   | **SoftMax Regression** | **SVC**  | **Random Forest Classifier** |
|:---------------------:|:----------------------:|:--------:|:----------------------------:|
|   **Class Weight**    |        balanced        | balanced |           balanced           |
|    **Multi Class**    |      multinomial       |    -     |              -               |
|      **Solver**       |         lbfgs          |    -     |              -               |
|      **Kernel**       |           -            |  linear  |              -               |
|       **Gamma**       |           -            |   0.48   |              -               |
|         **C**         |          0.53          |   0.79   |              -               |
|  **Max Iterations**   |          6972          |   8170   |              -               |
| **Decision Function** |           -            |   ovo    |              -               |
|    **Estimators**     |           -            |    -     |             395              |
|       **Depth**       |           -            |    -     |              14              |
|     **Criterion**     |           -            |    -     |           log loss           |

<br>

**Table 2: Hyperparameters tuned on the balanced dataset using random oversampling**

|  **Hyperparameter**   | **SoftMax Regression** | **SVC**  | **Random Forest Classifier** |
|:---------------------:|:----------------------:|:--------:|:----------------------------:|
|   **Class Weight**    |        balanced        | balanced |           balanced           |
|    **Multi Class**    |      multinomial       |    -     |              -               |
|      **Solver**       |         lbfgs          |    -     |              -               |
|      **Kernel**       |           -            |   rbf    |              -               |
|       **Gamma**       |           -            |   0.33   |              -               |
|         **C**         |          0.88          |   0.57   |              -               |
|  **Max Iterations**   |          7356          |   9189   |              -               |
| **Decision Function** |           -            |   ovo    |              -               |
|    **Estimators**     |           -            |    -     |             133              |
|       **Depth**       |           -            |    -     |              22              |
|     **Criterion**     |           -            |    -     |           log loss           |

## Challenges

1. **Overfitting**: The model exhibited signs of overfitting, where it performed well on the training data but struggled
   to generalize to unseen data. This was primarily due to the random oversampling technique used to address class
   imbalance. While oversampling can balance the dataset, it also introduces redundancy and can cause data leakage
   between the training and unseen data. This redundancy might lead the model to memorize specific patterns from the
   training set, which hampers its ability to generalize.


2. **Small and Imbalanced Data**: A significant limitation was the small size of the dataset, which constrained the
   model's ability to learn meaningful patterns. Coupled with this, the data imbalance made it harder for the model to
   learn representations for the underrepresented classes, further compounding the overfitting issue. The imbalance,
   when combined with the small data size, made it difficult for the model to build a reliable generalization from the
   training data.


3. **Challenges in Data Acquisition**: The ability to gather enough high-quality data is critical. Web scraping has been
   limited in our case, making it challenging to acquire a sufficient volume of diverse examples. This limitation is
   expected to persist, and will need to be addressed in the future by either collaborating with Khamsat to obtain more
   data or exploring data augmentation techniques, including synthetic data generation, to simulate additional varied
   examples that better represent the target distribution.

## Results

The performance of the models is assessed using a set of standard evaluation metrics, including Log Loss, Accuracy,
Precision, Recall, and the F1-score.

The results for each model, presented in Tables 3 and 4, highlight the trade-offs between these metrics under different
conditions, offering insight into the strengths and weaknesses of each approach.

**Table 3: Performance metrics on the imbalanced dataset.**

| **Model**                | **Loss** | **Accuracy** | **Precision** | **Recall** | **F1**  |
|:-------------------------|:--------:|:------------:|:-------------:|:----------:|:-------:|
| SoftMax Regression       |   1.62   |     40%      |      17%      |    23%     |   17%   |
| SVC                      |   1.18   |     42%      |      16%      |    18%     |   16%   |
| Random Forest Classifier |   1.28   |   **56%**    |    **22%**    |  **25%**   | **22%** |

<br>

**Table 4: Performance metrics on the balanced dataset.**

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

## Ownership

The data utilized in this project is the property of
the <a href="https://khamsat.com" target="_blank"><img src="./views/images/logo.png" alt="https://khamsat.com" title="موقع خمسات" height="10"></a>
platform, with all associated rights reserved to them. This project, however, is an independent endeavor and solely
owned by me, with no affiliation to any institution or organization.
