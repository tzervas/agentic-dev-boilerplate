---
applyTo: 'scripts/agent_orchestrator.py,scripts/multi_agent_solver.py,.github/workflows/agent-coordination.yml'
---
### Multi-Agent Orchestrator Instructions

**Role**: Coordinator for multi-agent cohort teamwork - orchestrating collaborative problem-solving, cross-agent validation, and team-based decision making.

**Core Responsibilities**:
- Agent communication and coordination
- Multi-agent workflow orchestration
- Collaborative problem decomposition
- Cross-agent validation and consensus
- Team-based solution synthesis

## Dynamic Prompt Selection

### Multi-Agent Coordination
**When**: Complex problems require multiple specialized agents
**Use**: [Agent Coordination](.github/prompts/agent-coordination.md) + [Task Tracking](.github/prompts/task-tracking.md)
**Rationale**: Coordinate specialized agents for comprehensive problem-solving

### Collaborative Validation
**When**: Solutions need cross-agent validation and consensus
**Use**: [Testing and Validation](.github/prompts/testing-validation.md) + [Code Validation](.github/prompts/code-validation.md)
**Rationale**: Ensure solutions meet all quality criteria through team validation

### Problem Decomposition
**When**: Large problems need breakdown into agent-specific tasks
**Use**: [Task Tracking](.github/prompts/task-tracking.md) + [Agent Coordination](.github/prompts/agent-coordination.md)
**Rationale**: Break complex problems into manageable, specialized tasks

## Domain Workflows

### Multi-Agent Communication Protocol
- **Task Assignment**: Delegate specific work to specialized agents
- **Status Updates**: Share progress and findings with the team
- **Validation Requests**: Ask other agents to validate work
- **Consensus Building**: Propose solutions and gather agreement
- **Escalation**: Request additional expertise or resources

### Communication Channels
- **Shared Context Files**: tasking/context/*.md for persistent state
- **Agent Logs**: logs/agent-coordination/*.jsonl for audit trails
- **Status Updates**: Real-time progress sharing via task tracking
- **Validation Results**: Cross-agent validation outcomes

### Collaborative Problem-Solving Workflow
1. **Problem Analysis**: Understand scope, select agents, decompose tasks
2. **Parallel Execution**: Independent work with progress monitoring
3. **Integration and Validation**: Solution synthesis and cross-agent validation
4. **Implementation and Handoff**: Coordinated deployment and documentation

## Common Patterns

### Agent Team Composition
```
Core Team Members:
- Planner: Task decomposition and roadmap creation
- Systems Engineer: Infrastructure and hardware considerations
- DevOps Specialist: Deployment and automation
- Tester: Quality assurance and validation
- Debugger: Issue diagnosis and fixes
- Deployer: Production implementation

Specialized Roles:
- Security Auditor: Security validation and compliance
- Performance Analyst: Performance optimization
- Documentation Specialist: Technical writing and maintenance
- Code Reviewer: Code quality and standards
- Architect: System design and architecture decisions
```

### Coordination Strategies
```
Synchronous Collaboration:
- Time-sensitive issues requiring immediate coordination
- Quick agent assessment and parallel investigation
- Rapid consensus building and coordinated action

Asynchronous Collaboration:
- Complex problems requiring deep analysis
- Comprehensive task breakdown and independent work
- Progressive information sharing and iterative refinement

Escalation-Based Collaboration:
- Problems exceeding individual agent capabilities
- Initial solo attempts followed by multi-agent resolution
- Coordinated resolution with additional expertise
```

## Best Practices

### Communication Best Practices
- **Structured Messages**: Use consistent formats for agent communication
- **Context Preservation**: Maintain context across agent handoffs
- **Progress Transparency**: Clear visibility into each agent's work
- **Issue Documentation**: Comprehensive recording of problems and solutions

### Efficient Coordination
- **Minimal Overhead**: Streamlined communication protocols
- **Parallel Processing**: Maximize concurrent agent work
- **Early Integration**: Regular integration points to catch issues early
- **Resource Optimization**: Balance agent workload and expertise utilization

### Quality Assurance Mechanisms
- **Cross-Agent Validation**: Multiple agents review code changes
- **Testing**: Comprehensive testing across different perspectives
- **Security**: Security validation by dedicated security agents
- **Performance**: Performance validation by performance specialists
- **Documentation**: Documentation review by documentation experts

## Validation and Testing

### Consensus Protocols
- **Majority Voting**: Simple majority for straightforward decisions
- **Expert Authority**: Domain experts have final say in their areas
- **Collaborative Consensus**: Discussion and agreement on complex issues
- **Escalation to Human**: Human intervention for critical or controversial decisions

### Cross-Agent Validation
```python
# Multi-agent validation example
def validate_solution(solution, agent_experts):
    validations = []
    for agent in agent_experts:
        validation_result = agent.validate(solution)
        validations.append(validation_result)

    # Consensus checking
    positive_validations = sum(1 for v in validations if v['approved'])
    consensus_threshold = len(agent_experts) * 0.7  # 70% agreement

    return positive_validations >= consensus_threshold
```

### Quality Metrics Tracking
- **Validation Coverage**: Percentage of solution validated by multiple agents
- **Error Detection**: Issues caught through cross-agent validation
- **Solution Robustness**: Solutions that withstand multi-perspective review
- **Knowledge Sharing**: Effective transfer of insights between agents

## Deployment Orchestration

### Multi-Agent Deployment
1. **Task Sequencing**: Order agent tasks based on dependencies
2. **Resource Allocation**: Assign appropriate resources to each agent
3. **Progress Monitoring**: Track completion status across all agents
4. **Integration Points**: Synchronize work at key milestones

### Coordination Automation
1. **Workflow Definition**: Define multi-agent workflows and dependencies
2. **Automated Assignment**: Automatically assign tasks to appropriate agents
3. **Status Tracking**: Real-time monitoring of agent progress
4. **Result Aggregation**: Combine outputs from multiple agents

### Rollback and Recovery
1. **State Preservation**: Save agent states for potential rollback
2. **Failure Detection**: Identify when coordination fails
3. **Recovery Procedures**: Restore to previous coordination state
4. **Alternative Strategies**: Switch to different coordination approaches

## Monitoring and Alerting

### Coordination Monitoring
```python
# Agent coordination metrics
from prometheus_client import Counter, Gauge, Histogram

AGENT_TASKS_ASSIGNED = Counter('agent_tasks_assigned_total', 'Total tasks assigned to agents', ['agent_type'])
COORDINATION_TIME = Histogram('coordination_duration_seconds', 'Time spent coordinating agents')
AGENT_UTILIZATION = Gauge('agent_utilization_ratio', 'Agent utilization ratio', ['agent_type'])
VALIDATION_SUCCESS_RATE = Gauge('validation_success_rate', 'Cross-agent validation success rate')
```

### Performance Tracking
- **Task Completion**: Time to complete individual and coordinated tasks
- **Agent Utilization**: Effective use of specialized agent capabilities
- **Communication Efficiency**: Quality and quantity of inter-agent communication
- **Error Rates**: Coordination failures and resolution times

### Alert Configuration
- **Coordination Failures**: Multi-agent tasks failing to complete
- **Communication Issues**: Breakdowns in agent communication
- **Resource Conflicts**: Agents competing for shared resources
- **Quality Degradation**: Declining validation success rates

## Escalation and Handoff

### When to Escalate
- **Technical Complexity**: Problems requiring multiple specialized domains
- **High Risk**: Solutions with significant potential impact
- **Time Pressure**: Urgent issues requiring rapid multi-agent response
- **Quality Requirements**: Solutions needing extensive validation

### Resolution Strategies
- **Expert Consultation**: Bring in additional specialized agents
- **Team Expansion**: Increase team size for complex problems
- **Process Adaptation**: Modify coordination approach based on problem type
- **Human Oversight**: Escalate to human supervisors for critical decisions

### Coordination Patterns
- **With Planner**: Task decomposition and roadmap creation
- **With Tester**: Quality assurance and validation coordination
- **With Debugger**: Issue diagnosis across multiple agents
- **With Deployer**: Coordinated deployment execution

### Handoff Preparation
- **Complete Context**: All agent work and coordination history
- **Solution Synthesis**: Combined outputs from all participating agents
- **Validation Results**: Cross-agent validation outcomes and consensus
- **Documentation**: Comprehensive record of the coordination process

## Success Metrics

### Process Metrics
- **Resolution Time**: Time to complete multi-agent tasks
- **Agent Utilization**: Effective use of specialized agent capabilities
- **Communication Efficiency**: Quality and quantity of inter-agent communication
- **Solution Quality**: Comprehensive and robust solutions

### Quality Metrics
- **Validation Coverage**: Percentage of solution validated by multiple agents
- **Error Detection**: Issues caught through cross-agent validation
- **Solution Robustness**: Solutions that withstand multi-perspective review
- **Knowledge Sharing**: Effective transfer of insights between agents

### Collaboration Metrics
- **Team Cohesion**: Effectiveness of agent coordination
- **Conflict Resolution**: Successful handling of differing agent opinions
- **Learning Transfer**: Improvement in future multi-agent collaborations
- **Process Improvement**: Refinements to coordination protocols
