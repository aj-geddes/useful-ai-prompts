# CSS Safety Guidelines - Preventing Button & Interaction Breakage

## 🚨 CRITICAL RULES - NEVER VIOLATE

### 1. Pointer Events Management
```css
/* ❌ NEVER DO THIS - Blocks all interactions */
.container {
    pointer-events: none;
}

/* ✅ CORRECT - Specific control */
.container {
    pointer-events: auto; /* Default behavior */
}

.container::before {
    pointer-events: none; /* Only pseudo-elements */
}
```

### 2. Z-Index Hierarchy
```css
/* ✅ APPROVED Z-INDEX LEVELS */
/* Background elements: -1 to 0 */
/* Content cards: 1-5 */
/* Interactive buttons: 10-20 */
/* Dropdowns/modals: 100-1000 */
/* Notifications: 1000-9999 */
/* Critical overlays: 10000+ */

/* ❌ NEVER use arbitrary high z-index values */
.some-element {
    z-index: 999999; /* WRONG - breaks hierarchy */
}

/* ✅ CORRECT - Follow the scale */
.btn-primary {
    z-index: 15; /* Interactive element level */
}
```

### 3. Interactive Element Safety
```css
/* ✅ REQUIRED for all clickable elements */
.btn, .btn-primary, .btn-secondary, 
button, a[href], [onclick] {
    pointer-events: auto !important;
    cursor: pointer !important;
    position: relative !important;
    z-index: 10 !important; /* Minimum for buttons */
}
```

## 🛡️ SAFETY CHECKS BEFORE CSS DEPLOYMENT

### Pre-Deployment Checklist
- [ ] All buttons have `pointer-events: auto`
- [ ] Interactive elements have appropriate z-index (10+)
- [ ] No fixed/absolute elements block content areas
- [ ] Pseudo-elements use `pointer-events: none`
- [ ] Overlays are properly scoped with display controls

### Testing Protocol
1. **Manual Click Test**: Verify every "View Prompt" button works
2. **Z-Index Validation**: Check computed styles in DevTools
3. **Mobile Test**: Ensure touch targets are 44px+ and clickable
4. **Overlay Test**: Verify dropdowns don't block content when closed

## 🔧 EMERGENCY REPAIR PATTERNS

### Pattern 1: Button Rescue
```css
/* Emergency button fix - use sparingly */
.btn-primary {
    pointer-events: auto !important;
    z-index: 20 !important;
    position: relative !important;
    cursor: pointer !important;
}
```

### Pattern 2: Card Interaction Fix
```css
/* Card container allows interaction */
.prompt-card {
    pointer-events: auto !important;
}

/* But pseudo-elements stay non-interactive */
.prompt-card::before,
.prompt-card::after {
    pointer-events: none !important;
    z-index: -1 !important;
}
```

### Pattern 3: Overlay Management
```css
/* Hidden overlays must not interfere */
.overlay:not(.show),
.dropdown:not(.active) {
    pointer-events: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
}
```

## 📋 CSS FILE SAFETY ZONES

### Safe for Modifications
- Typography (fonts, sizes, colors)
- Spacing (margins, padding)
- Visual effects (shadows, gradients)
- Animations (transforms, transitions)

### DANGER ZONES - Require Extra Review
- `pointer-events` properties
- `z-index` values
- `position: fixed/absolute`
- `overflow: hidden` on containers
- `display: none` on interactive elements

## 🚫 FORBIDDEN PRACTICES

### Never Apply These to Interactive Elements:
```css
/* ❌ BREAKS FUNCTIONALITY */
.interactive-element {
    pointer-events: none;        /* Blocks clicks */
    z-index: -1;                /* Hides behind content */
    opacity: 0;                 /* Makes invisible */
    visibility: hidden;         /* Removes from interaction */
    display: none;              /* Completely hides */
    overflow: hidden;           /* Can clip content */
}
```

### Never Use These Z-Index Values:
- Below 0 for interactive elements
- Above 10000 without justification
- Arbitrary large numbers (99999, etc.)

## 🔄 RECOVERY PROCEDURES

### If Buttons Stop Working:
1. **Immediate**: Add emergency CSS fixes from Pattern 1
2. **Investigate**: Use browser DevTools to check computed styles
3. **Identify**: Find conflicting CSS rules
4. **Fix**: Remove or override problematic styles
5. **Test**: Verify functionality across devices

### CSS Conflict Resolution Order:
1. Check `pointer-events` values
2. Verify z-index hierarchy
3. Look for overlapping fixed elements
4. Test pseudo-element interference
5. Validate responsive behavior

## 📊 MONITORING & VALIDATION

### Required Browser Testing:
- Chrome Desktop
- Safari Desktop  
- Chrome Mobile
- Safari Mobile
- Firefox Desktop

### Critical User Journeys:
1. Homepage → Category → Prompt Details
2. Search → Results → Prompt Selection
3. Mobile navigation and interactions

### Performance Monitoring:
- Core Web Vitals impact
- First Input Delay (FID)
- Cumulative Layout Shift (CLS)

## 🚀 DEPLOYMENT SAFETY

### Before Going Live:
1. Run emergency test page: `/emergency-button-test.html`
2. Verify all test cases pass
3. Check browser console for errors
4. Test on actual devices, not just DevTools

### Post-Deployment Monitoring:
- User interaction analytics
- Error rate monitoring
- Manual spot checks every 24 hours

---

**Remember**: When in doubt, prioritize user interaction over visual perfection. A working button is better than a broken beautiful button.

**Emergency Contact**: Check this file before making ANY changes to pointer-events, z-index, or position properties.