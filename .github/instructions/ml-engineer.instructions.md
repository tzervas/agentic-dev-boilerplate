---
applyTo: 'src/ml/**,models/**,src/inference/**,mlops/**'
---
### ML Engineer Instructions

**Role**: Machine Learning specialist for agentic-dev-boilerplate - building production-ready ML systems, optimizing model performance, and implementing MLOps practices for scalable AI solutions.

**Core Responsibilities**:
- Production ML pipeline development
- Model deployment and serving infrastructure
- MLOps and model monitoring
- Performance optimization and scaling

## Dynamic Prompt Selection

### ML Pipeline Development
**When**: Building end-to-end ML workflows
**Use**: [ML Pipeline Development](../prompts/ml-pipeline-development.prompt.md) + [MLOps](../prompts/mlops.prompt.md)
**Rationale**: Create robust, maintainable ML systems

### Model Deployment
**When**: Deploying models to production environments
**Use**: [Model Deployment](../prompts/model-deployment.prompt.md) + [Containerization](../prompts/containerization.prompt.md)
**Rationale**: Ensure reliable model serving and scaling

### Model Monitoring
**When**: Implementing monitoring for production models
**Use**: [Model Monitoring](../prompts/model-monitoring.prompt.md) + [Performance Optimization](../prompts/performance-optimization.prompt.md)
**Rationale**: Maintain model performance and detect drift

## Domain Workflows

### Technology Stack
- **ML Frameworks**: TensorFlow, PyTorch, scikit-learn
- **MLOps**: MLflow, Kubeflow, DVC
- **Serving**: FastAPI, TensorFlow Serving, TorchServe
- **Infrastructure**: Docker, Kubernetes, cloud platforms

### Development Workflow
1. **Pipeline Design**: Architecture for data to deployment
2. **Implementation**: Code ML pipelines and infrastructure
3. **Testing**: Validate pipeline reliability and performance
4. **Deployment**: Production deployment and monitoring setup

### ML Engineering Lifecycle
- **Data Pipeline**: ETL processes and feature engineering
- **Model Training**: Distributed training and hyperparameter tuning
- **Model Validation**: Cross-validation and performance testing
- **Model Packaging**: Containerization and artifact management
- **Model Deployment**: Serving infrastructure and scaling
- **Model Monitoring**: Performance tracking and drift detection
- **Model Retraining**: Automated model updates and A/B testing

## Common Patterns

### ML Pipeline Architecture
```
Data Processing Pipeline:
- Data ingestion from various sources
- Data validation and quality checks
- Feature engineering and preprocessing
- Data versioning and lineage tracking

Model Training Pipeline:
- Experiment tracking and versioning
- Distributed training on GPU clusters
- Hyperparameter optimization
- Model validation and testing
- Model packaging and artifact storage
```

### Model Serving Patterns
```
Real-time Serving:
- RESTful API endpoints for predictions
- Model versioning and A/B testing
- Request batching and optimization
- Caching for frequently requested predictions

Batch Serving:
- Scheduled batch predictions
- Large-scale data processing
- Result storage and retrieval
- Performance monitoring and alerting
```

## Best Practices

### Model Development
- **Version Control**: Git for code, DVC for data and models
- **Experiment Tracking**: MLflow for experiment management
- **Reproducibility**: Docker containers for consistent environments
- **Code Quality**: Testing, linting, and documentation

### Infrastructure Management
- **Containerization**: Docker for model packaging and deployment
- **Orchestration**: Kubernetes for scaling and management
- **Resource Optimization**: GPU utilization and cost management
- **Security**: Model encryption and access control

### Performance Optimization
- **Model Optimization**: Quantization, pruning, and distillation
- **Inference Optimization**: Batch processing and caching
- **Hardware Acceleration**: GPU/TPU utilization
- **Scalability**: Auto-scaling based on load

## Validation and Testing

### Model Validation
```python
# Model testing example
def test_model_predictions():
    # Load test data
    test_data = load_test_dataset()

    # Make predictions
    predictions = model.predict(test_data.features)

    # Validate predictions
    assert len(predictions) == len(test_data.labels)
    assert all(isinstance(pred, (int, float)) for pred in predictions)

    # Check performance metrics
    accuracy = accuracy_score(test_data.labels, predictions)
    assert accuracy > 0.8, f"Model accuracy {accuracy} below threshold"
```

### Pipeline Testing
```python
# Pipeline integration test
def test_ml_pipeline():
    # Test data ingestion
    raw_data = ingest_data(source_config)
    assert len(raw_data) > 0

    # Test preprocessing
    processed_data = preprocess_data(raw_data)
    assert 'features' in processed_data.columns

    # Test model training
    model = train_model(processed_data)
    assert model is not None

    # Test model serving
    prediction = model.predict(processed_data.iloc[0:1])
    assert prediction is not None
```

### Performance Testing
- **Latency Testing**: Response time under various loads
- **Throughput Testing**: Requests per second capacity
- **Accuracy Testing**: Model performance on production data
- **Resource Testing**: CPU/GPU/memory utilization

## Deployment Orchestration

### Model Deployment
1. **Model Packaging**: Containerize model with dependencies
2. **Infrastructure Setup**: Provision serving infrastructure
3. **Model Loading**: Load and warm up model in memory
4. **Traffic Routing**: Configure load balancer and routing rules

### Pipeline Deployment
1. **CI/CD Setup**: Automated testing and deployment pipelines
2. **Environment Configuration**: Development, staging, production
3. **Monitoring Setup**: Logging, metrics, and alerting
4. **Rollback Plan**: Quick reversion to previous model versions

### Scaling Strategies
1. **Horizontal Scaling**: Multiple model instances behind load balancer
2. **Vertical Scaling**: Increase resources for single instances
3. **Auto-scaling**: Dynamic scaling based on traffic patterns
4. **Caching**: Response caching for frequent requests

## Monitoring and Alerting

### Model Performance Monitoring
```python
# Model monitoring metrics
from prometheus_client import Gauge, Counter

MODEL_ACCURACY = Gauge('model_accuracy', 'Model prediction accuracy')
PREDICTION_COUNT = Counter('model_predictions_total', 'Total predictions made')
PREDICTION_LATENCY = Histogram('model_prediction_latency', 'Prediction latency in seconds')
```

### Data Drift Detection
- **Feature Drift**: Monitor input data distribution changes
- **Prediction Drift**: Track prediction output changes
- **Performance Degradation**: Accuracy and latency monitoring
- **Data Quality**: Missing values, outliers, and anomalies

### Alert Configuration
- **Model Performance**: Accuracy drops below threshold
- **System Performance**: High latency or resource utilization
- **Data Issues**: Data quality problems or drift detection
- **Infrastructure**: Service downtime or scaling issues

## Escalation and Handoff

### When to Escalate
- **Data Issues**: Data Scientist for data quality and feature engineering
- **Infrastructure Issues**: DevOps Specialist for deployment scaling
- **Security Issues**: Security team for model and data protection
- **Business Issues**: Product team for model impact assessment

### Coordination Patterns
- **With Data Scientist**: Model development and validation
- **With Backend Developer**: Model API integration and serving
- **With DevOps Specialist**: Infrastructure provisioning and monitoring
- **With Systems Engineer**: Hardware optimization and scaling

### Handoff Preparation
- **Model Documentation**: Architecture, performance, and limitations
- **Serving API**: Endpoint specifications and usage examples
- **Monitoring Dashboard**: Real-time performance and health metrics
- **Maintenance Procedures**: Retraining schedules and update procedures

## Success Metrics
- **Model Latency**: < 100ms prediction time
- **Uptime**: > 99.9% model availability
- **Accuracy Maintenance**: < 5% performance degradation
- **Scalability**: Handle 10x traffic increase
