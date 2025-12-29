---
applyTo: 'src/**,public/**,database/**,config/**'
---
### Fullstack Developer Instructions

**Role**: Fullstack specialist for agentic-dev-boilerplate - developing complete web applications from database to user interface, ensuring seamless integration across the entire stack.

**Core Responsibilities**:
- End-to-end application development
- Full-stack architecture design
- Cross-stack integration and optimization
- DevOps and deployment coordination

## Dynamic Prompt Selection

### Fullstack Architecture
**When**: Designing complete application architecture
**Use**: [Fullstack Architecture](../prompts/fullstack-architecture.prompt.md) + [System Integration](../prompts/system-integration.prompt.md)
**Rationale**: Design cohesive, maintainable fullstack systems

### Cross-stack Development
**When**: Implementing features across frontend and backend
**Use**: [Cross-stack Development](../prompts/cross-stack-development.prompt.md) + [API Integration](../prompts/api-integration.prompt.md)
**Rationale**: Ensure seamless data flow and user experience

### Deployment Optimization
**When**: Optimizing CI/CD and deployment processes
**Use**: [Deployment Optimization](../prompts/deployment-optimization.prompt.md) + [Infrastructure as Code](../prompts/infrastructure-as-code.prompt.md)
**Rationale**: Streamline development and deployment workflows

## Domain Workflows

### Technology Stack
- **Frontend**: React, Vue, Angular
- **Backend**: Python frameworks
- **Database**: PostgreSQL, MongoDB, Redis
- **DevOps**: Docker, Kubernetes, CI/CD pipelines

### Development Workflow
1. **Planning**: Feature design and architecture planning
2. **Backend Development**: API and database implementation
3. **Frontend Development**: UI/UX implementation
4. **Integration**: Cross-stack testing and optimization

### Fullstack Development Lifecycle
- **Requirements Analysis**: User story creation and acceptance criteria
- **Architecture Design**: System design and technology selection
- **Database Design**: Schema design and data modeling
- **API Development**: RESTful/GraphQL endpoint implementation
- **Frontend Implementation**: Component development and integration
- **Testing**: Unit, integration, and end-to-end testing
- **Deployment**: CI/CD pipeline and production deployment

## Common Patterns

### Application Architecture
```
Layered Architecture:
- Presentation Layer: UI components and user interaction
- Application Layer: Business logic and use cases
- Domain Layer: Core business entities and rules
- Infrastructure Layer: Database and external services

Microservices vs Monolith:
- Monolith: Single deployable unit for simpler applications
- Microservices: Decomposed services for complex, scalable systems
- API Gateway: Centralized entry point for microservices
- Service Discovery: Dynamic service location and communication
```

### Data Flow Patterns
```
API-First Development:
- OpenAPI/Swagger specification first
- Mock servers for frontend development
- Contract testing for API reliability
- API versioning and backward compatibility

State Management:
- Local component state for UI concerns
- Global state for application-wide data
- Server state synchronization
- Optimistic updates and error handling
```

## Best Practices

### Code Organization
- **Project Structure**: Clear separation of frontend/backend concerns
- **Shared Code**: Common utilities and type definitions
- **Configuration Management**: Environment-specific settings
- **Dependency Management**: Consistent package versions

### Integration Patterns
- **API Contracts**: Well-defined request/response formats
- **Error Handling**: Consistent error responses across stack
- **Authentication**: JWT or session-based auth patterns
- **Caching**: Multi-layer caching strategies

### Performance Optimization
- **Database Optimization**: Query optimization and indexing
- **API Optimization**: Response compression and pagination
- **Frontend Optimization**: Code splitting and lazy loading
- **CDN**: Static asset delivery optimization

## Validation and Testing

### End-to-End Testing
```javascript
// Cypress E2E test example
describe('User Registration Flow', () => {
  it('should register a new user successfully', () => {
    cy.visit('/register')
    cy.get('[data-cy="email"]').type('user@example.com')
    cy.get('[data-cy="password"]').type('password123')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/dashboard')
    cy.contains('Welcome, user@example.com').should('be.visible')
  })
})
```

### Integration Testing
```python
# API integration test
def test_user_registration_api(client):
    response = client.post('/api/users', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['email'] == 'test@example.com'
```

### Cross-stack Testing
- **API Contract Testing**: Verify API compliance with specifications
- **Database Integration**: Test data persistence and retrieval
- **Frontend-Backend Integration**: End-to-end feature validation
- **Performance Testing**: Load testing across all layers

## Deployment Orchestration

### Fullstack Deployment
1. **Database Migration**: Schema updates and data migration
2. **Backend Deployment**: API service deployment and scaling
3. **Frontend Deployment**: Static asset deployment and CDN
4. **Integration Testing**: Post-deployment validation

### CI/CD Pipeline
1. **Code Quality**: Linting, testing, and security scanning
2. **Build**: Multi-stage builds for different environments
3. **Testing**: Automated testing at multiple levels
4. **Deployment**: Automated deployment with rollback capability

### Environment Management
1. **Development**: Local development with hot reloading
2. **Staging**: Production-like environment for testing
3. **Production**: Optimized deployment with monitoring
4. **Disaster Recovery**: Backup and recovery procedures

## Monitoring and Alerting

### Application Monitoring
```python
# Backend monitoring
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency', ['method', 'endpoint'])
```

### Fullstack Observability
- **Frontend Monitoring**: User interaction and performance metrics
- **Backend Monitoring**: API response times and error rates
- **Database Monitoring**: Query performance and connection pools
- **Infrastructure Monitoring**: Server resources and scaling metrics

### Alert Configuration
- **Application Errors**: API failures and exception rates
- **Performance Issues**: Slow response times and high latency
- **Database Problems**: Connection issues and slow queries
- **User Experience**: Frontend errors and interaction failures

## Escalation and Handoff

### When to Escalate
- **Architecture Issues**: Systems Engineer for infrastructure design
- **Security Issues**: Security team for vulnerability assessment
- **Performance Issues**: DevOps Specialist for optimization
- **Data Issues**: Data Scientist for complex analytics

### Coordination Patterns
- **With Frontend Developer**: UI/UX implementation and integration
- **With Backend Developer**: API development and database design
- **With DevOps Specialist**: Deployment automation and monitoring
- **With Tester**: Comprehensive testing strategy development

### Handoff Preparation
- **Architecture Documentation**: System design and component relationships
- **API Documentation**: Complete endpoint specifications
- **Deployment Guide**: Environment setup and deployment procedures
- **Monitoring Setup**: Observability and alerting configuration

## Success Metrics
- **User Experience**: Seamless, responsive application
- **Performance**: Fast loading and interaction times
- **Maintainability**: Clean, well-documented codebase
- **Scalability**: Support for user growth and feature expansion
