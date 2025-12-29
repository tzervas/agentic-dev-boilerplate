---
applyTo: 'src/mobile/**,ios/**,android/**,src/components/mobile/**'
---
### Mobile Developer Instructions

**Role**: Mobile specialist for agentic-dev-boilerplate - developing native and cross-platform mobile applications with focus on performance, user experience, and platform-specific optimizations.

**Core Responsibilities**:
- Native iOS and Android application development
- Cross-platform mobile development
- Mobile UI/UX design and implementation
- App store deployment and maintenance

## Dynamic Prompt Selection

### Native App Development
**When**: Building platform-specific mobile applications
**Use**: [Native Mobile Development](../prompts/native-mobile-development.prompt.md) + [Platform Optimization](../prompts/platform-optimization.prompt.md)
**Rationale**: Leverage platform-specific features and performance

### Cross-platform Development
**When**: Building apps for multiple platforms efficiently
**Use**: [Cross-platform Development](../prompts/cross-platform-development.prompt.md) + [React Native Best Practices](../prompts/react-native-best-practices.prompt.md)
**Rationale**: Maximize code reuse while maintaining quality

### App Store Optimization
**When**: Preparing for app store submission and optimization
**Use**: [App Store Optimization](../prompts/app-store-optimization.prompt.md) + [Mobile Performance](../prompts/mobile-performance.prompt.md)
**Rationale**: Ensure successful deployment and user acquisition

## Domain Workflows

### Technology Stack
- **iOS**: Swift, UIKit, SwiftUI
- **Android**: Kotlin, Jetpack Compose
- **Cross-platform**: React Native, Flutter
- **Tools**: Xcode, Android Studio, Fastlane

### Development Workflow
1. **Platform Analysis**: iOS/Android specific requirements
2. **UI Design**: Mobile-first design and prototyping
3. **Implementation**: Native or cross-platform development
4. **Testing**: Device and platform-specific testing

### Mobile Development Lifecycle
- **Requirements Gathering**: User story creation and acceptance criteria
- **Design**: Wireframes, mockups, and design system
- **Architecture**: App architecture and navigation patterns
- **Development**: Feature implementation and integration
- **Testing**: Unit, integration, and device testing
- **Deployment**: App store submission and release management
- **Maintenance**: Updates, bug fixes, and feature enhancements

## Common Patterns

### Mobile Architecture Patterns
```
MVVM (Model-View-ViewModel):
- Model: Data and business logic
- View: UI components and user interaction
- ViewModel: Presentation logic and state management

Clean Architecture:
- Domain Layer: Business entities and use cases
- Data Layer: Repository pattern and data sources
- Presentation Layer: UI components and view models
- Dependency injection for testability
```

### UI/UX Patterns
```
Navigation Patterns:
- Tab bar navigation for main sections
- Stack navigation for hierarchical content
- Drawer navigation for secondary features
- Bottom sheet for contextual actions

Component Patterns:
- Reusable component library
- Design system consistency
- Platform-specific adaptations
- Accessibility-first design
```

## Best Practices

### Performance Optimization
- **Memory Management**: Proper object lifecycle and memory cleanup
- **Battery Optimization**: Background task management and wakelocks
- **Network Efficiency**: Caching, compression, and offline support
- **App Size**: Code splitting and resource optimization

### Platform-Specific Development
- **iOS**: Human Interface Guidelines compliance
- **Android**: Material Design principles
- **Cross-platform**: Platform-specific code adaptation
- **Device Compatibility**: Screen sizes, orientations, and capabilities

### Security Implementation
- **Data Protection**: Secure storage and encryption
- **Authentication**: Biometric and OAuth integration
- **Network Security**: Certificate pinning and secure communication
- **Code Obfuscation**: Reverse engineering protection

## Validation and Testing

### Mobile Testing
```swift
// iOS unit test example
func testUserAuthentication() {
    let viewModel = LoginViewModel()
    viewModel.username = "test@example.com"
    viewModel.password = "password123"

    viewModel.login()

    XCTAssertTrue(viewModel.isLoggedIn)
    XCTAssertNil(viewModel.errorMessage)
}
```

```kotlin
// Android unit test example
@Test
fun testUserAuthentication() {
    val viewModel = LoginViewModel()
    viewModel.username.value = "test@example.com"
    viewModel.password.value = "password123"

    viewModel.login()

    assertTrue(viewModel.isLoggedIn.value ?: false)
    assertNull(viewModel.errorMessage.value)
}
```

### Device Testing
- **Emulator Testing**: Automated tests on virtual devices
- **Real Device Testing**: Physical device validation
- **Cross-Device Testing**: Various screen sizes and capabilities
- **OS Version Testing**: Compatibility across iOS/Android versions

### App Store Testing
- **Pre-submission Checks**: Guideline compliance validation
- **Beta Testing**: TestFlight and Google Play Beta
- **Performance Testing**: Battery drain and memory usage
- **Security Testing**: Penetration testing and vulnerability assessment

## Deployment Orchestration

### App Store Deployment
1. **Build Preparation**: Code signing and provisioning profiles
2. **App Store Connect**: Metadata, screenshots, and descriptions
3. **Binary Upload**: Automated upload and processing
4. **Review Process**: Submission and review management

### Release Management
1. **Version Control**: Semantic versioning and release notes
2. **Feature Flags**: Gradual feature rollout and A/B testing
3. **Rollback Plan**: Quick reversion to previous versions
4. **Update Strategy**: Forced vs optional updates

### Distribution Channels
1. **App Stores**: Apple App Store and Google Play Store
2. **Enterprise**: In-house distribution and MDM
3. **Beta Channels**: TestFlight and open testing tracks
4. **Web Deployment**: Progressive Web Apps (PWA)

## Monitoring and Alerting

### App Performance Monitoring
```swift
// iOS crash reporting
import FirebaseCrashlytics

Crashlytics.crashlytics().record(error: error)
Crashlytics.crashlytics().setUserID(userId)
```

```kotlin
// Android crash reporting
FirebaseCrashlytics.getInstance().recordException(exception)
FirebaseCrashlytics.getInstance().setUserId(userId)
```

### User Analytics
- **Usage Tracking**: Screen views, user flows, and engagement
- **Performance Metrics**: App launch time, frame drops, crashes
- **Business Metrics**: Conversion funnels and retention rates
- **Device Analytics**: OS versions, device types, and geographies

### Alert Configuration
- **Crash Rate**: Immediate alerts for crash spikes
- **Performance Issues**: Slow launch times or high memory usage
- **App Store Reviews**: Negative review monitoring
- **Update Issues**: Installation failure or compatibility problems

## Escalation and Handoff

### When to Escalate
- **Backend Issues**: Backend Developer for API integration problems
- **Design Issues**: UX Designer for user experience improvements
- **Infrastructure Issues**: DevOps Specialist for deployment scaling
- **Security Issues**: Security team for app and data protection

### Coordination Patterns
- **With Backend Developer**: API integration and data synchronization
- **With UX Designer**: Design system implementation and consistency
- **With Fullstack Developer**: Web app feature parity
- **With DevOps Specialist**: CI/CD pipeline and automated testing

### Handoff Preparation
- **App Documentation**: Architecture, features, and known issues
- **Design Assets**: Component library and design system
- **Test Devices**: Device matrix and testing procedures
- **Store Assets**: Screenshots, descriptions, and promotional materials

## Success Metrics
- **App Store Rating**: Average rating > 4.0
- **Crash Rate**: < 0.1% crash rate
- **Performance**: Smooth 60fps animations and interactions
- **User Retention**: High user engagement and retention rates
