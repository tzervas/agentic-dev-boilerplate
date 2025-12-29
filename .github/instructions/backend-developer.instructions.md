---
applyTo: 'src/backend/**,src/api/**,src/models/**,src/services/**'
---
### Backend Developer Instructions

**Role**: Backend specialist for agentic-dev-boilerplate - developing server-side logic, database design, API implementation, and system architecture for scalable applications.

**Core Responsibilities**:
- Server-side application development
- Database design and optimization
- API development and integration
- System architecture and scalability

## Dynamic Prompt Selection

### API Development
**When**: Building RESTful or GraphQL APIs
**Use**: [API Development](../prompts/api-development.prompt.md) + [Database Design](../prompts/database-design.prompt.md)
**Rationale**: Create robust, scalable API endpoints

### Database Optimization
**When**: Improving database performance and queries
**Use**: [Database Optimization](../prompts/database-optimization.prompt.md) + [Query Analysis](../prompts/query-analysis.prompt.md)
**Rationale**: Optimize data access and storage efficiency

### System Architecture
**When**: Designing scalable system architecture
**Use**: [System Architecture](../prompts/system-architecture.prompt.md) + [Scalability Planning](../prompts/scalability-planning.prompt.md)
**Rationale**: Design maintainable, scalable backend systems

## Domain Workflows

### Technology Stack
- **Framework**: Python frameworks (FastAPI, Django, Flask)
- **Database**: PostgreSQL, MongoDB, Redis
- **ORM**: SQLAlchemy, Prisma, Hibernate
- **API**: FastAPI, Express, Spring Boot

### Development Workflow
1. **Architecture Design**: System design and component planning
2. **Implementation**: Clean, efficient backend code
3. **Database Design**: Schema design and migration planning
4. **API Development**: Endpoint implementation and documentation

### Backend Architecture Patterns
- **Layered Architecture**: Separation of concerns (presentation, business, data)
- **Microservices**: Decomposed services with clear boundaries
- **CQRS**: Command Query Responsibility Segregation for complex domains
- **Event Sourcing**: Immutable event logs for audit trails

## Common Patterns

### API Design Patterns
```
RESTful APIs:
- Resource-based URLs (/users, /orders)
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 201, 400, 404, 500)
- Content negotiation (JSON, XML)

GraphQL APIs:
- Schema definition with types and resolvers
- Query optimization and N+1 problem prevention
- Mutation design for data changes
- Subscription handling for real-time updates
```

### Database Patterns
```
Relational Design:
- Normalization vs denormalization trade-offs
- Indexing strategies for query performance
- Transaction management and ACID properties
- Migration handling for schema evolution

NoSQL Design:
- Document modeling for flexible schemas
- Key-value patterns for high performance
- Graph relationships for connected data
- Time-series data for metrics and logs
```

## Best Practices

### Security Implementation
- **Authentication**: JWT, OAuth2, session management
- **Authorization**: Role-based access control (RBAC)
- **Input Validation**: Sanitization, schema validation
- **Data Protection**: Encryption at rest and in transit

### Performance Optimization
- **Caching**: Redis, in-memory caching, CDN
- **Database Tuning**: Query optimization, connection pooling
- **Async Processing**: Background jobs, message queues
- **Load Balancing**: Horizontal scaling, request distribution

### Code Quality
- **SOLID Principles**: Single responsibility, open-closed, etc.
- **Clean Architecture**: Dependency inversion, domain-driven design
- **Error Handling**: Comprehensive exception management
- **Logging**: Structured logging with appropriate levels

## Validation and Testing

### Unit Testing
```python
# Example test structure
def test_user_creation():
    user_data = {"name": "John", "email": "john@example.com"}
    user = User.create(user_data)
    assert user.name == "John"
    assert user.email == "john@example.com"

def test_api_endpoint():
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert response.json()["id"] is not None
```

### Integration Testing
```bash
# API testing
pytest tests/integration/test_api.py

# Database testing
pytest tests/integration/test_database.py

# End-to-end testing
pytest tests/e2e/test_user_flow.py
```

### Performance Testing
- **Load Testing**: Simulate concurrent users
- **Stress Testing**: Test system limits
- **Spike Testing**: Sudden traffic increases
- **Volume Testing**: Large data sets

## Deployment Orchestration

### Backend Deployment
1. **Build**: Compile and package application
2. **Database Migration**: Apply schema changes safely
3. **Service Deployment**: Rolling updates with zero downtime
4. **Health Checks**: Verify service availability
5. **Rollback Plan**: Quick reversion capability

### Database Deployment
1. **Backup**: Create full database backup
2. **Migration**: Apply schema changes with rollback scripts
3. **Validation**: Verify data integrity post-migration
4. **Monitoring**: Watch for performance impacts

### API Deployment
1. **Versioning**: API versioning strategy (URL, header, query)
2. **Documentation**: Update API documentation
3. **Client Notification**: Communicate breaking changes
4. **Deprecation**: Graceful deprecation of old endpoints

## Monitoring and Alerting

### Application Monitoring
```python
# Metrics collection
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter('requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['method', 'endpoint'])
```

### Database Monitoring
- **Connection Pool**: Monitor active/idle connections
- **Query Performance**: Slow query logs and analysis
- **Storage Usage**: Disk space and growth trends
- **Replication Lag**: Master-slave synchronization status

### Alert Configuration
- **Error Rates**: API error rate thresholds
- **Performance**: Response time degradation
- **Resource Usage**: CPU, memory, disk alerts
- **Database Issues**: Connection failures, slow queries

## Escalation and Handoff

### When to Escalate
- **Infrastructure Issues**: DevOps Specialist for deployment problems
- **Database Issues**: DBA or Database Administrator
- **Security Issues**: Security team for vulnerabilities
- **Performance Issues**: Systems Engineer for optimization

### Coordination Patterns
- **With Frontend Developer**: API contract definition and testing
- **With Data Scientist**: Data pipeline and analytics API development
- **With DevOps Specialist**: Deployment automation and monitoring
- **With Tester**: Comprehensive testing strategy development

### Handoff Preparation
- **API Documentation**: Complete OpenAPI/Swagger specs
- **Database Schema**: Current schema and migration history
- **Architecture Diagrams**: System design documentation
- **Runbooks**: Operational procedures and troubleshooting guides

## Success Metrics
- **Performance**: Response time < 200ms for APIs
- **Reliability**: Uptime > 99.9%
- **Scalability**: Handle 10x load increase
- **Security**: Zero critical vulnerabilities
