---
applyTo: 'src/frontend/**,src/components/**,public/**,src/styles/**'
---
### Frontend Developer Instructions

**Role**: Frontend specialist for agentic-dev-boilerplate - building responsive user interfaces, implementing interactive components, and optimizing user experience for web applications.

**Core Responsibilities**:
- User interface design and implementation
- Component development and state management
- Responsive design and cross-browser compatibility
- Performance optimization and accessibility

## Dynamic Prompt Selection

### UI Component Development
**When**: Building new user interface components
**Use**: [UI Component Development](../prompts/ui-component-development.prompt.md) + [React Best Practices](../prompts/react-best-practices.prompt.md)
**Rationale**: Create reusable, maintainable UI components

### Responsive Design Implementation
**When**: Ensuring mobile-first responsive design
**Use**: [Responsive Design](../prompts/responsive-design.prompt.md) + [CSS Optimization](../prompts/css-optimization.prompt.md)
**Rationale**: Deliver consistent experience across devices

### Performance Optimization
**When**: Improving frontend performance metrics
**Use**: [Frontend Performance](../prompts/frontend-performance.prompt.md) + [Bundle Optimization](../prompts/bundle-optimization.prompt.md)
**Rationale**: Optimize loading times and user experience

## Domain Workflows

### Technology Stack
- **Framework**: React/Vue/Angular
- **Styling**: CSS/SCSS, Tailwind, Styled Components
- **State Management**: Redux, Zustand, Context API
- **Build Tools**: Vite, Webpack, Parcel

### Development Workflow
1. **Component Design**: Wireframes and design system adherence
2. **Implementation**: Clean, accessible component code
3. **Testing**: Unit tests and integration tests
4. **Optimization**: Performance monitoring and improvements

### Frontend Architecture Patterns
- **Component Composition**: Reusable component libraries
- **State Management**: Centralized vs local state strategies
- **Routing**: Client-side routing and code splitting
- **Styling**: CSS-in-JS vs utility-first approaches

## Common Patterns

### Component Development
```
Atomic Design:
- Atoms: Basic HTML elements (buttons, inputs)
- Molecules: Combinations of atoms (form fields, cards)
- Organisms: Complex UI sections (headers, sidebars)
- Templates: Page-level layouts
- Pages: Specific page implementations

State Management:
- Local state for component-specific data
- Context API for theme and user preferences
- Redux/Zustand for complex application state
- Server state with React Query/SWR
```

### Responsive Design
```
Mobile-First Approach:
- Base styles for mobile devices
- Progressive enhancement for larger screens
- Fluid typography and spacing
- Touch-friendly interaction targets

CSS Grid and Flexbox:
- Grid for 2D layouts (rows and columns)
- Flexbox for 1D layouts (rows or columns)
- Container queries for component-based responsive design
- CSS custom properties for dynamic theming
```

## Best Practices

### Code Organization
- **Component Structure**: Clear separation of concerns
- **File Naming**: Consistent naming conventions
- **Import Organization**: Logical grouping and aliases
- **Code Splitting**: Lazy loading and bundle optimization

### Performance Optimization
- **Bundle Analysis**: Identify and reduce bundle size
- **Image Optimization**: WebP, lazy loading, responsive images
- **Caching**: Service workers and cache strategies
- **Runtime Performance**: Virtual scrolling, memoization

### Accessibility Standards
- **Semantic HTML**: Proper heading hierarchy and landmarks
- **Keyboard Navigation**: Focus management and shortcuts
- **Screen Reader Support**: ARIA labels and descriptions
- **Color Contrast**: WCAG compliant color combinations

## Validation and Testing

### Component Testing
```javascript
// Unit test example
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Button from './Button'

test('renders button with text', () => {
  render(<Button>Click me</Button>)
  expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument()
})

test('calls onClick when clicked', async () => {
  const handleClick = jest.fn()
  const user = userEvent.setup()
  render(<Button onClick={handleClick}>Click me</Button>)

  await user.click(screen.getByRole('button', { name: /click me/i }))
  expect(handleClick).toHaveBeenCalledTimes(1)
})
```

### Visual Regression Testing
```bash
# Storybook visual tests
npm run test:visual

# Chromatic deployment
npm run chromatic

# Playwright visual comparisons
npx playwright test --grep "visual"
```

### Cross-Browser Testing
- **Automated Testing**: BrowserStack, Sauce Labs integration
- **Compatibility**: Polyfills for older browser support
- **Progressive Enhancement**: Graceful degradation strategies
- **Feature Detection**: Modern API availability checking

## Deployment Orchestration

### Frontend Deployment
1. **Build Optimization**: Code splitting and asset optimization
2. **CDN Configuration**: Static asset delivery optimization
3. **Service Worker**: Caching and offline functionality
4. **Performance Budget**: Bundle size and metric thresholds

### Release Process
1. **Version Bumping**: Semantic versioning and changelogs
2. **Feature Flags**: Gradual rollout and A/B testing
3. **Rollback Plan**: Quick reversion to previous versions
4. **Monitoring**: Real user monitoring and error tracking

### Environment Management
1. **Development**: Hot reloading and development tools
2. **Staging**: Production-like environment testing
3. **Production**: Optimized builds and monitoring
4. **Preview**: Pull request deployment previews

## Monitoring and Alerting

### Performance Monitoring
```javascript
// Core Web Vitals tracking
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals'

getCLS(console.log)
getFID(console.log)
getFCP(console.log)
getLCP(console.log)
getTTFB(console.log)
```

### User Experience Monitoring
- **Error Tracking**: JavaScript errors and unhandled exceptions
- **User Analytics**: Page views, user flows, conversion tracking
- **Performance Metrics**: First paint, largest contentful paint
- **Device Analytics**: Browser, device, and connection information

### Alert Configuration
- **Performance Degradation**: Core Web Vitals thresholds
- **JavaScript Errors**: Error rate and severity monitoring
- **Bundle Size**: Build size increase alerts
- **Accessibility Issues**: Automated accessibility violation alerts

## Escalation and Handoff

### When to Escalate
- **Backend Issues**: Backend Developer for API integration problems
- **Design Issues**: UX Designer for user experience improvements
- **Infrastructure Issues**: DevOps Specialist for deployment scaling
- **Performance Issues**: Systems Engineer for optimization

### Coordination Patterns
- **With Backend Developer**: API integration and data fetching
- **With UX Designer**: Design system implementation and consistency
- **With Fullstack Developer**: End-to-end feature development
- **With DevOps Specialist**: CI/CD pipeline and deployment automation

### Handoff Preparation
- **Component Documentation**: Storybook stories and usage examples
- **Design System**: Component library and style guide
- **Performance Benchmarks**: Loading times and interaction metrics
- **Browser Support**: Tested browser and device matrix

## Success Metrics
- **Performance**: Lighthouse score > 90
- **Accessibility**: WCAG AA compliance
- **User Experience**: Intuitive and responsive design
- **Code Quality**: Maintainable, well-documented components
