# Inceptez Batch-25 Classwork

Welcome to the **Inceptez Batch-25 Classwork Repository**. This README is a concise top-level guide: quick start, folder overview, and pointers to detailed session notebooks inside their respective folders.

---

## Quick start


```bash
git clone https://github.com/Laxminarayen/Inceptez-batch-25-Classwork.git
cd Inceptez-batch-25-Classwork
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. (Optional) Install dependencies for demos/notebooks that include a requirements file:

```bash
pip install -r Demo-Student-Datacollection/requirements.txt
```

4. Launch Jupyter Lab or Notebook and open the notebooks you want to explore:

```bash
jupyter lab
```

---
## How to use this repository

1. Open the folder for the session you want to study.
2. Launch Jupyter and open the notebook (`.ipynb`) for that session.
3. If a notebook lists required packages, install them into your active environment.
4. Run notebook cells sequentially; notebooks include explanations and runnable examples.

---

## Contributing

If you'd like to suggest improvements (typos, clearer examples), open an issue or submit a small PR. Prefer focused changes per PR.

---

## License & Contact

- No license file is included by default. If you want to publish or reuse broadly, consider adding a license (e.g., MIT).
- For questions, contact the repository owner (GitHub user `Laxminarayen`).

---

(End of README)

## 📅 Session 3: Control Statements, Loops & Time Complexity  
📆 Date: 6th July 2025

Introduced control flow statements and loop structures, including real-world examples and performance analysis.

### ✅ Topics:
- `if`, `elif`, `else` with decision-making analogies
- `for`, `while` loops using strings, lists, dicts
- Iteration helpers: `range()`, `enumerate()`, `zip()`, `reversed()`, `sorted()`
- Control tools: `break`, `continue`, `pass`
- Time complexity of patterns (linear, nested, etc.)

📁 Folder:  
[`Python-Class3-ControlStatements-Loops-TimeComplexity`](./Python-Class3-ControlStatements-Loops-TimeComplexity)

📓 Notebook:  
| File | Description |
|------|-------------|
| `Class3_ControlStructures_Explained_WithTimeComplexity.ipynb` | Looping constructs with time complexity and use cases |

---

## 📅 Session 4: Bitwise Operators, Augmented Arithmetic, Functions & Classes  
📆 Date: 12th July 2025

Covered Python’s low-level operators and built up to object-oriented concepts with clear examples and memory impact.

### ✅ Topics:
- **Bitwise Operators**: `&`, `|`, `^`, `~`, `<<`, `>>`
- **Augmented Arithmetic**: `+=`, `-=`, `*=`, etc. and efficiency
- **Functions**: Definition, parameters, return values, scope
- **Function Overloading & Polymorphism**
- **Classes**: `__init__`, methods, objects
- Duck Typing and Pythonic behavior
- Included bonus: Merge Sort & Recursion explanation

📁 Folder:  
[`Python-Class4-BitwiseOperators-AugementedArithmetics-Functions-Classes`](./Python-Class4-BitwiseOperators-AugementedArithmetics-Functions-Classes)

📓 Notebook:  
| File | Description |
|------|-------------|
| `Class4_Bitwise_Augment_Functions_Classes_OrderedFinal.ipynb` | Bitwise, augmented ops, functions, classes, and recursion with merge sort |

---

## 📅 Session 5: Arguments, Function Overloading, Recursion & Searching  
📆 Date: 13th July 2025

We explored flexible ways to define and call functions, revisited recursion deeply with visual logic, and laid the foundation for searching techniques in Python.

### ✅ Topics:
- **Function Arguments**:
  - Positional, default, `*args`, `**kwargs`
- **Function Overloading** in Python using flexible parameters
## Recent / final folders

- `Python-Class15-Hypothesis1-Inferential2-Pandas` — This session built upon our introduction to inferential statistics by focusing on hypothesis testing. Students learned how to frame statistical questions, test claims with data, and interpret results using Pandas and statistical logic.
- `Python-Class16-17-Hypothesis2-Tests-Pandas`
- `Python-Class17-DataPreprocessing`
- `01. Intro-Machine Learning`
- `02. Linear Regression`

---

### ✅ Topics Covered:

- 🧱 **Advanced Classes & OOP Enhancements**  
  - Class vs Instance variables  
  - `@classmethod` and `@staticmethod` usage  
  - Encapsulation and abstraction  
  - Magic (dunder) methods: `__init__`, `__str__`, `__repr__`, `__eq__`, `__len__` etc.  
  - Operator overloading through magic methods  

- 🔤 **String Processing Techniques**  
  - Slicing, indexing, and immutable behavior  
  - Common methods: `split()`, `join()`, `replace()`, `strip()`, `find()`, `count()`  
  - f‑strings and formatted output  
    
📁 **Folder**:  
[`Python-Class7-Classes-Introduction`](./Python-Class7-Classes-Introduction) 

## 📅 Session 9: NumPy & Pandas - Foundation for Data Science  
📆 Date: 27th July 2025

Introduced the core libraries that power Python-based data science: **NumPy** for numerical array operations and **Pandas** for structured data manipulation. Emphasis was placed on understanding the difference between native Python lists and NumPy arrays, and how Pandas helps in working with tabular data efficiently.

### ✅ Topics Covered:
- 📊 **NumPy**:
  - Difference between Lists vs Arrays
  - Creating arrays (`np.array`, `np.arange`, `np.zeros`, etc.)
  - Reshaping, indexing, slicing
  - Broadcasting rules and element-wise operations
  - Speed & memory benefits over Python lists

- 📈 **Pandas**:
  - Creating and working with `Series` and `DataFrame`
  - Reading data from CSV files
  - Viewing and summarizing data (`head()`, `tail()`, `info()`, `describe()`)
  - Filtering, indexing, and column/row access

📁 **Folder**:  
[`Beginner_Numpy_Pandas_Notebook.ipynb`](./Python-Class9-Numpy-Pandas-Intro)


## 📅 Session 10: Pandas Basics 
📆 Date: 02nd August 2025

This class dives into **how pandas stores and represents data** internally, with a focus on different data types and how to work with them effectively.

## 🎯 Learning Objectives
By the end of this class, you should be able to:
- Identify different pandas data types (`int64`, `float64`, `object`, `bool`, `datetime64`, `category`, `string`)
- Convert columns between types using `astype()` and other methods
- Work with **datetime** columns for time-based analysis
- Use **categorical** data for memory efficiency and better performance
- Perform **string operations** directly on DataFrame columns

📁 **Folder**:  
[`Class10_Pandas_Data_Types_Documented.ipynb`](./Python-Class10-Pandas-Basics)

## 📅 Session 11: Pandas Intermediate 
📆 Date: 03rd August 2025

This class builds on your basic Pandas knowledge to cover **intermediate data transformation and wrangling techniques**.  

## 📅 Session 12: Descriptive Statistics (Part 1) with Pandas  
📆 Date: 09th August 2025

This session introduced **Descriptive Statistics** using Python and Pandas. We focused on summarising and understanding datasets through statistical measures rather than just raw data.  

### ✅ Topics Covered:  
- 📊 **Measures of Central Tendency**  
  - Mean, Median, Mode  
  - When to use each measure  
- 📈 **Measures of Dispersion**  
  - Variance, Standard Deviation, Range  
  - Why dispersion matters in real-world datasets  
- 📐 **Shape of Distribution**  
- 🔍 **Exploratory Data Analysis (EDA) with Pandas**  
  - `describe()` method  
  - Custom summary statistics (`.mean()`, `.median()`, `.mode()`, `.var()`, `.std()`)  
- 🧩 **Hands-on Examples**  
  - Applying descriptive statistics on sample datasets  
  - Interpreting results in business & data science contexts  

📁 **Folder**:  
[`Python-Class12-DescriptiveStatistics-Pandas`](./Python-Class12-DescriptiveStatistics-Pandas)  

📓 **Notebook**:  
| File | Description |  
|------|-------------|  
| `DescriptiveStatistics-Classwork.ipynb` | Covers descriptive statistics using Pandas with examples and explanations |  

## 📅 Session 13: Descriptive Statistics (Part 2) with Pandas  
📆 Date: 10th August 2025  

This session continued our in-depth exploration of **Descriptive Statistics** using Pandas, building on the basics covered in Session 12. We focused on richer statistical summaries, relationships between variables, and practical use cases in exploratory data analysis (EDA).  

### ✅ Topics Covered:  
- 🔁 **Review of Descriptive Statistics Basics**  
  - Central tendency (mean, median, mode)  
  - Dispersion (variance, standard deviation, range)  

- 📊 **Advanced Summary Measures**  
  - Percentiles and Quartiles  
  - Interquartile Range (IQR)  
  - Outlier detection using IQR  

- 🔗 **Relationships Between Variables**  
  - Covariance  
  - Correlation (`.corr()`)  
  - Heatmaps and pairwise correlation analysis  

- 🛠 **Hands-on EDA with Pandas**  
  - Applying advanced statistical methods to real datasets  
  - Identifying patterns and relationships in tabular data  
  - Preparing insights for visualisation and hypothesis testing  

📁 **Folder**:  
[`Python-Class13-DescriptiveStatistics2-Pandas`](./Python-Class13-DescriptiveStatistics2-Pandas)  

## 📅 Session 14: Inferential Statistics (Part 1) with Pandas  
📆 Date: 16th August 2025  

This session marked the transition from **Descriptive** to **Inferential Statistics**, focusing on how we move beyond summarizing data to making **predictions and generalizations about populations** using sample data.  

### ✅ Topics Covered:  
- 🔑 **Introduction to Inferential Statistics**  
  - Difference between descriptive and inferential approaches  
  - Population vs Sample concepts  
  - Why we need inference in data science  

- 🎲 **Probability Foundations**  
  - Random variables and distributions  
  - Sampling distributions  
  - Law of Large Numbers & Central Limit Theorem (CLT)  

- 📏 **Estimation Techniques**  

|------|-------------|  
| `OneSampleZ-Classwork.ipynb` | Covers the foundations of hypothesis testing and demonstrates one-sample Z-tests using Pandas |  

## 📅 Session 16 & 17: Hypothesis Testing (Inferential Statistics – Part 3 & 4) with Pandas  
📆 Date: 23rd & 24th August 2025  

These sessions extended our study of **hypothesis testing** by exploring multiple statistical tests beyond the one-sample Z-test. The focus was on selecting the **right test for the right scenario**, applying it in Pandas, and interpreting the results in the context of data-driven decision-making.  

### ✅ Topics Covered:  
- 🔄 **Review of Hypothesis Testing Framework**  
  - Null (H₀) vs Alternative (H₁)  
  - Errors in testing (Type I & II)  
  - Decision rules and p-value interpretation  

- 📊 **Different Hypothesis Tests**  
  - **One-Sample Tests**: Z-test, T-test    
  - **Chi-Square Test** for independence of categorical variables
  - **F-Test** Test for variance

- 📐 **When to Use Which Test?**  
  - Comparing proportions vs means  
  - Parametric vs non-parametric scenarios  
  - Practical business/data applications  

- 🛠 **Hands-on in Pandas & Python**  
  - Performing hypothesis tests step by step  
  - Using datasets to apply Z, T, Chi-Square, and F test
  - Interpreting outputs to form business insights  

📁 **Folder**:  
[`Python-Class16-17-Hypothesis2-Tests-Pandas`](./Python-Class16-17-Hypothesis2-Tests-Pandas)  

📓 **Notebook**:  
| File | Description |  
|------|-------------|  
|| `DifferentHypothesisTests.ipynb` | Demonstrates multiple hypothesis tests (Z, T, Chi-Square, ANOVA) with examples and real-world use cases |  

## 📅 Session 17: Data Preprocessing for Machine Learning  
📆 Date: 30th August 2025  

This session focused on preparing raw data for machine learning algorithms. Data preprocessing is a critical step that directly impacts model performance and accuracy.  

### ✅ Topics Covered:  
- 🧼 **Handling Missing Data**  
  - Identifying missing values with `isnull()` and `isna()`  
  - Strategies: dropping, imputation (mean, median, mode, forward/backward fill)  
  
- 📊 **Data Scaling & Normalization**  
  - StandardScaler (z-score normalization)  
  - MinMaxScaler (range scaling)  
  - When to use which scaler  
  
- 🏷️ **Encoding Categorical Variables**  
  - Label Encoding for ordinal data  
  - One-Hot Encoding for nominal data  
  - `pd.get_dummies()` and sklearn's `OneHotEncoder`  
  
- 🔍 **Feature Engineering Basics**  
  - Creating new features from existing ones  
  - Handling datetime features  
  - Binning and discretization  
  
- ✂️ **Splitting Data**  
  - Train-test split  
  - Importance of random state for reproducibility  

📁 **Folder**:  
[`Python-Class17-DataPreprocessing`](./Python-Class17-DataPreprocessing)  

---

## 📅 EXAM DETAILS

### Part 1 – Online Quiz (MCQs)
👉 Join Quiz Here: https://wayground.com/join?gc=07791682
  - No login required – click the link.
  - 1 minute per question ⏱
  - Covers Python, Pandas, and Statistics (based on our class material).
  - Please attempt all questions in one go. PLEASE DO NOT refresh in the middle!! 
  -  This Quiz link will be active till: Aug 31, 2025, 11:59 AM IST

### Part 2 – Coding Assignment (Application-based)
👉 Download Notebook – 6 Questions
📂 Instructions:
  - Questions link: https://github.com/Laxminarayen/Inceptez-batch-25-Classwork/blob/main/Test-1/InceptezExam1.ipynb
  - Open the .ipynb file in Google Colab (File → Upload Notebook) or Jupyter.
  - Enter your Name at the top.
  - Solve all 6 coding questions – each has clear input, and expected output.
  - Save as YourName_Assessment.ipynb.
  - Upload your completed notebook to this link:
  - 👉 [Upload Link Here] (https://drive.google.com/drive/folders/1duYEIhCOEzk0FbLhaeZgqVwA0QP8O2jx?usp=drive_link)

---

# 🤖 Machine Learning Sessions

## 📅 ML Session 1: Introduction to Machine Learning  
📆 Date: October 25 2025  

This session introduced the fundamentals of Machine Learning, providing a comprehensive overview of what ML is, its types, and real-world applications.  

### ✅ Topics Covered:  
- 🧠 **What is Machine Learning?**  
  - Difference between AI, ML, and Deep Learning  
  - How machines learn from data  
  
- 📋 **Types of Machine Learning**  
  - Supervised Learning (Classification & Regression)  
  - Unsupervised Learning (Clustering & Dimensionality Reduction)  
  - Reinforcement Learning basics  
  
- 🎯 **ML Workflow**  
  - Problem definition  
  - Data collection and preprocessing  
  - Model selection and training  
  - Evaluation and deployment  
  
- 📊 **Real-world Applications**  
  - Recommendation systems  
  - Image recognition  
  - Fraud detection  
  - Predictive analytics  

📁 **Folder**:  
[`01. Intro-Machine Learning`](./01.%20Intro-Machine%20Learning)  

---

## 📅 ML Session 2: Linear Regression  
📆 Date: October 26 2025  

This session covered Linear Regression, one of the fundamental algorithms in machine learning for predicting continuous values.  

### ✅ Topics Covered:  
- 📈 **Linear Regression Fundamentals**  
  - What is regression?  
  - Simple vs Multiple Linear Regression  
  - Assumptions of linear regression  
  
- 📊 **Mathematical Foundation**  
  - Equation of a line: y = mx + b  
  
📁 **Folder**:  
[`02. Linear Regression`](./02.%20Linear%20Regression)  


---

# Inceptez Batch-25 Classwork

Welcome to the **Inceptez Batch-25 Classwork Repository**!  
This repository includes all the class notes, code examples, and practice files used throughout our Data Science & Machine Learning course at Inceptez Technologies.  

---

## 📂 Folder Structure

| Folder | Description |
|--------|-------------|
| [`Python-Class-1-Runningtypes-Identifiers-Variables`](./Python-Class-1-Runningtypes-Identifiers-Variables) | Python setup, execution types, identifiers |
| [`Python-Class2-Memory-Properties-DataStructures`](./Python-Class2-Memory-Properties-DataStructures) | Memory behavior, data structures |
| [`Python-Class3-ControlStatements-Loops-TimeComplexity`](./Python-Class3-ControlStatements-Loops-TimeComplexity) | Control statements and time complexity |
| [`Python-Class4-BitwiseOperators-AugementedArithmetics-Functions-Classes`](./Python-Class4-BitwiseOperators-AugementedArithmetics-Functions-Classes) | Bitwise, functions, classes, recursion |
| [`Python-Class5-Arguments-FunctionOverloading-Recurssion-SearchingAlgos`](./Python-Class5-Arguments-FunctionOverloading-Recurssion-SearchingAlgos) | Function arguments, overloading, recursion, searching algorithms | 
| [`Python-Class6-List-Dictionary-Comprehension-problems`](./Python-Class6-List-Dictionary-Comprehension-problems) | List Comprehension, Dictionary Comprehension, Time Complexity of `list` vs `dict`,  Why dictionaries are optimized for speed |
| [`Python-Class7-Classes-Introduction`](./Python-Class7-Classes-Introduction) |  **classes**, **objects**, and **inheritance** |
| [`Python-Class8-ClassesAdvanced-StringManipulations`](./Python-Class8-ClassesAdvanced-StringManipulations)                                 | Explores class design, variable scoping (LEGB), and string handling in depth |
|  [`Python-Class9-Numpy-Pandas-Intro`](./Python-Class9-Numpy-Pandas-Intro) | Covers basic NumPy & Pandas operations with beginner-friendly explanations, comparisons, and demos |
|  [`Python-Class10-Pandas-Basics`](./Python-Class10-Pandas-Basics) | This class dives into **how pandas stores and represents data** internally, with a focus on different data types and how to work with them effectively. |
|  [`Python-Class11-Pandas-Intermediate`](./Python-Class11-Pandas-Intermediate) | This class builds on your basic Pandas knowledge to cover **intermediate data transformation and wrangling techniques**. |
| [`Python-Class12-Descriptive-Statistics`](./Python-Class12-DescriptiveStatistics-Pandas)` | This session introduced **Descriptive Statistics** using Python and Pandas. We focused on summarising and understanding datasets through statistical measures rather than just raw data.   |  
|[`Python-Class13-DescriptiveStatistics2-Pandas`](./Python-Class13-DescriptiveStatistics2-Pandas)  | This session continued our in-depth exploration of **Descriptive Statistics** using Pandas, building on the basics covered in Session 12. We focused on richer statistical summaries, relationships between variables, and practical use cases in exploratory data analysis (EDA).   |
| [`Python-Class14-Inferential1-Pandas`](./Python-Class14-Inferential1-Pandas)  | This session marked the transition from **Descriptive** to **Inferential Statistics**, focusing on how we move beyond summarizing data to making **predictions and generalizations about populations** using sample data.  | 
| Folder | Description |
|--------|-------------|
| [`Python-Class14-Inferential1-Pandas`](./Python-Class14-Inferential1-Pandas) | This session marked the transition from Descriptive to Inferential Statistics, focusing on how we move beyond summarizing data to making predictions and generalizations about populations using sample data. |
| [`Python-Class15-Hypothesis1-Inferential2-Pandas`](./Python-Class15-Hypothesis1-Inferential2-Pandas) | This session built upon our introduction to inferential statistics by focusing on hypothesis testing. Students learned how to frame statistical questions, test claims with data, and interpret results using Pandas and statistical logic. |
| [`Python-Class16-17-Hypothesis2-Tests-Pandas`](./Python-Class16-17-Hypothesis2-Tests-Pandas) | These sessions extended our study of hypothesis testing by exploring multiple statistical tests beyond the one-sample Z-test. The focus was on selecting the right test for the right scenario, applying it in Pandas, and interpreting the results in the context of data-driven decision-making. |
| [`Python-Class17-DataPreprocessing`](./Python-Class17-DataPreprocessing) | Data preprocessing techniques including handling missing values, scaling, encoding categorical variables, feature engineering, and train-test splitting. |
| [`01. Intro-Machine Learning`](./01.%20Intro-Machine%20Learning) | Introduction to Machine Learning concepts, types (supervised/unsupervised), ML workflow, and real-world applications. |
| [`02. Linear Regression`](./02.%20Linear%20Regression) | Linear Regression fundamentals, mathematical foundations, implementation with sklearn, and model evaluation metrics. |
---

## 🛠 Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/Laxminarayen/Inceptez-batch-25-Classwork.git
   cd Inceptez-batch-25-Classwork
