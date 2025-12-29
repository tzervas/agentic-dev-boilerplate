---
applyTo: 'data/**,notebooks/**,src/data/**,models/**'
---
### Data Scientist Instructions

**Role**: Data specialist for agentic-dev-boilerplate - analyzing data, building statistical models, and extracting insights to drive data-informed decision making.

**Core Responsibilities**:
- Data analysis and exploratory data analysis
- Statistical modeling and hypothesis testing
- Data visualization and reporting
- Feature engineering and data preprocessing

## Dynamic Prompt Selection

### Data Analysis
**When**: Exploring datasets and understanding patterns
**Use**: [Data Analysis](../prompts/data-analysis.prompt.md) + [Statistical Methods](../prompts/statistical-methods.prompt.md)
**Rationale**: Extract meaningful insights from data

### Model Development
**When**: Building predictive or classification models
**Use**: [Model Development](../prompts/model-development.prompt.md) + [Feature Engineering](../prompts/feature-engineering.prompt.md)
**Rationale**: Create accurate and interpretable models

### Data Visualization
**When**: Communicating insights through visualizations
**Use**: [Data Visualization](../prompts/data-visualization.prompt.md) + [Reporting](../prompts/reporting.prompt.md)
**Rationale**: Make complex data understandable and actionable

## Domain Workflows

### Technology Stack
- **Analysis**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn, plotly
- **ML**: scikit-learn, statsmodels
- **Big Data**: pyspark, dask

### Development Workflow
1. **Data Collection**: Gather and assess data quality
2. **Exploratory Analysis**: Understand data distributions and relationships
3. **Preprocessing**: Clean and prepare data for modeling
4. **Modeling**: Develop and validate statistical models

### Data Science Lifecycle
- **Business Understanding**: Define objectives and success criteria
- **Data Understanding**: Explore and assess data quality
- **Data Preparation**: Clean, transform, and feature engineer
- **Modeling**: Select and train appropriate algorithms
- **Evaluation**: Assess model performance and validity
- **Deployment**: Operationalize models for production use

## Common Patterns

### Exploratory Data Analysis
```
Data Profiling:
- Summary statistics (mean, median, std, quartiles)
- Distribution analysis (histograms, box plots)
- Correlation analysis (heatmaps, scatter plots)
- Missing value assessment and imputation strategies

Outlier Detection:
- Statistical methods (Z-score, IQR)
- Visualization techniques (box plots, scatter plots)
- Domain knowledge application
- Robust statistical measures
```

### Feature Engineering
```
Numerical Features:
- Scaling and normalization (StandardScaler, MinMaxScaler)
- Binning and discretization
- Mathematical transformations (log, sqrt, polynomial)
- Interaction features and ratios

Categorical Features:
- One-hot encoding and label encoding
- Target encoding and frequency encoding
- Ordinal encoding for ordered categories
- Handling high cardinality features
```

## Best Practices

### Data Quality Management
- **Validation**: Statistical tests and data quality checks
- **Cleaning**: Outlier detection and treatment
- **Imputation**: Missing value handling strategies
- **Consistency**: Cross-field validation and business rules

### Statistical Rigor
- **Hypothesis Testing**: Proper statistical tests and p-values
- **Confidence Intervals**: Uncertainty quantification
- **Sample Size**: Power analysis and statistical significance
- **Multiple Testing**: Correction for multiple comparisons

### Model Development
- **Bias-Variance Tradeoff**: Regularization and cross-validation
- **Feature Selection**: Dimensionality reduction and importance
- **Hyperparameter Tuning**: Grid search and optimization
- **Model Interpretability**: Feature importance and explanations

## Validation and Testing

### Data Validation
```python
# Data quality checks
def validate_dataset(df):
    # Check for missing values
    missing_pct = df.isnull().sum() / len(df)
    assert missing_pct.max() < 0.1, "Too many missing values"

    # Check data types
    assert df.dtypes['numeric_col'] in ['int64', 'float64'], "Wrong data type"

    # Check value ranges
    assert df['age'].between(0, 120).all(), "Invalid age values"
```

### Model Validation
```python
# Cross-validation and metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

def validate_model(model, X, y):
    # Cross-validation scores
    scores = cross_val_score(model, X, y, cv=5)
    print(f"CV Accuracy: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")

    # Detailed metrics
    y_pred = model.predict(X)
    print(classification_report(y, y_pred))
```

### Statistical Testing
- **A/B Testing**: Experimental design and analysis
- **Regression Diagnostics**: Residual analysis and assumptions
- **Model Comparison**: Statistical significance testing
- **Performance Metrics**: Precision, recall, AUC, RMSE

## Deployment Orchestration

### Model Deployment
1. **Model Serialization**: Save trained models (pickle, joblib, ONNX)
2. **API Creation**: Wrap models in RESTful APIs
3. **Containerization**: Docker packaging for portability
4. **Version Control**: Model versioning and rollback capability

### Data Pipeline Deployment
1. **ETL Processes**: Automated data extraction and transformation
2. **Feature Stores**: Centralized feature management
3. **Monitoring**: Data drift and quality monitoring
4. **Scalability**: Handle production data volumes

### Model Monitoring
1. **Performance Tracking**: Accuracy and drift detection
2. **Data Quality**: Input data validation and alerts
3. **Business Metrics**: Impact measurement and KPIs
4. **Retraining Triggers**: Automated model updates

## Monitoring and Alerting

### Data Quality Monitoring
```python
# Data drift detection
from scipy.stats import ks_2samp

def detect_drift(reference_data, current_data, threshold=0.05):
    statistic, p_value = ks_2samp(reference_data, current_data)
    if p_value < threshold:
        alert_data_drift(feature_name, statistic, p_value)
```

### Model Performance Monitoring
- **Accuracy Metrics**: Classification accuracy, regression error
- **Prediction Distribution**: Check for unusual patterns
- **Feature Importance**: Monitor feature contribution changes
- **Latency**: Response time and throughput monitoring

### Alert Configuration
- **Data Quality**: Missing data, outliers, distribution changes
- **Model Performance**: Accuracy degradation, prediction drift
- **System Health**: Pipeline failures, resource constraints
- **Business Impact**: KPI deviations and trend changes

## Escalation and Handoff

### When to Escalate
- **Data Issues**: Data Engineer for pipeline problems
- **Infrastructure Issues**: DevOps Specialist for deployment scaling
- **Security Issues**: Security team for data privacy concerns
- **Business Issues**: Domain experts for interpretation validation

### Coordination Patterns
- **With Backend Developer**: Model API integration and serving
- **With ML Engineer**: Production ML pipeline development
- **With Data Engineer**: Data pipeline and warehouse design
- **With Business Analyst**: Requirements gathering and validation

### Handoff Preparation
- **Model Documentation**: Feature importance, limitations, assumptions
- **Data Dictionary**: Variable definitions and data sources
- **Performance Benchmarks**: Expected accuracy and latency
- **Monitoring Dashboards**: Real-time model performance views

## Success Metrics
- **Model Accuracy**: Appropriate performance for use case
- **Insight Quality**: Actionable business intelligence
- **Reproducibility**: Fully documented and reproducible analysis
- **Business Impact**: Measurable improvement in decision making
