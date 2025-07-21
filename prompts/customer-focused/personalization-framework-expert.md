# Personalization Framework Expert

## Metadata
- **Category**: Customer-Focused/Experience Design
- **Created**: 2025-07-21
- **Version**: 1.0.0
- **Tags**: personalization, customer-experience, dynamic-content, behavioral-targeting
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
Build sophisticated personalization strategies that deliver relevant experiences to each customer. This prompt helps create frameworks for dynamic content, recommendations, and individualized interactions across all touchpoints.

## Prompt Template

```
I'll help you create a comprehensive personalization framework. Let's understand your needs:

PERSONALIZATION CONTEXT:
- What channels need personalization? (website, email, app, etc.)
- What customer data is available for personalization?
- Current level of personalization (if any)?

BUSINESS OBJECTIVES:
- Primary goals? (engagement, conversion, retention)
- Key metrics to improve?
- Any constraints (privacy, technology, resources)?

CUSTOMER EXPECTATIONS:
- What do customers expect from you?
- Privacy sensitivity in your market?
- Competitive personalization standards?

Here's your personalization framework:

## 1. DATA FOUNDATION
**Customer Data Platform**:
| Data Type | Sources | Update Frequency | Use Cases |
|-----------|---------|------------------|-----------|
| Profile | CRM, accounts | Real-time | Segmentation |
| Behavioral | Web, app | Real-time | Recommendations |
| Transactional | Sales, billing | Daily | Lifecycle |
| Preferences | Surveys, settings | On change | Content |

**Identity Resolution**:
- Cross-device tracking
- Anonymous to known progression
- Data hygiene rules
- Privacy compliance

## 2. PERSONALIZATION MATRIX
**By Channel & Depth**:
| Channel | Basic | Intermediate | Advanced |
|---------|--------|--------------|----------|
| Website | Name, location | Browse history | Predictive content |
| Email | Segment campaigns | Behavior triggers | Individual journeys |
| App | Saved preferences | Usage patterns | AI recommendations |
| Support | Account history | Sentiment routing | Proactive outreach |

## 3. CONTENT STRATEGY
**Dynamic Elements**:
- Hero banners and imagery
- Product recommendations
- Content blocks/modules
- Calls-to-action
- Pricing/offers

**Personalization Rules**:
```
IF [visitor is returning customer]
  AND [has items in cart]
  THEN [show cart reminder + related products]

IF [user segment = "price sensitive"]
  AND [browsing premium products]
  THEN [highlight value props + payment plans]
```

## 4. RECOMMENDATION ENGINE
**Algorithm Types**:
- **Collaborative**: "Customers like you also..."
- **Content-based**: "Based on your interests..."
- **Hybrid**: Combined approaches
- **Contextual**: Time, location, device

**Implementation Priorities**:
1. Product recommendations
2. Content suggestions
3. Next best action
4. Timing optimization

## 5. TESTING & OPTIMIZATION
**A/B Test Framework**:
- Personalized vs. generic
- Algorithm variations
- Content formats
- Timing strategies

**Success Metrics**:
- Engagement lift
- Conversion improvement
- Revenue per visitor
- Customer satisfaction

**Privacy Controls**:
- Opt-in/out mechanisms
- Transparency dashboard
- Data usage policies
```

## Examples

### Example 1: E-commerce Personalization
**Input**: "Online retailer, 500K customers, want to increase average order value"
**Output**: Multi-layer personalization with browsing-based homepage, AI product recommendations increasing AOV by 35%, personalized email campaigns with 3x higher conversion, dynamic pricing tests.

### Example 2: Media Platform Personalization
**Input**: "Streaming service, need to improve content discovery and reduce churn"
**Output**: Taste profile system, viewing pattern analysis, personalized homepages reducing browse time 50%, contextual recommendations (time of day, device), achieving 25% improvement in watch completion.

## Usage Instructions
1. Audit your current data sources and quality
2. Define clear personalization objectives and KPIs
3. Start with high-impact, low-complexity personalizations
4. Build measurement framework before launching
5. Iterate based on performance and customer feedback

## Related Prompts
- Customer Segmentation Expert
- Customer Journey Mapping Expert
- User Experience Design Expert