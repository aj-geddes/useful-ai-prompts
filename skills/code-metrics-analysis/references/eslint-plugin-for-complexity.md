# ESLint Plugin for Complexity

## ESLint Plugin for Complexity

```javascript
// eslint-plugin-complexity.js
module.exports = {
  rules: {
    "max-complexity": {
      create(context) {
        const maxComplexity = context.options[0] || 10;
        let complexity = 0;

        function increaseComplexity(node) {
          complexity++;
        }

        function checkComplexity(node) {
          if (complexity > maxComplexity) {
            context.report({
              node,
              message: `Function has complexity of ${complexity}. Maximum allowed is ${maxComplexity}.`,
            });
          }
        }

        return {
          FunctionDeclaration(node) {
            complexity = 1;
          },
          "FunctionDeclaration:exit": checkComplexity,

          IfStatement: increaseComplexity,
          SwitchCase: increaseComplexity,
          ForStatement: increaseComplexity,
          WhileStatement: increaseComplexity,
          DoWhileStatement: increaseComplexity,
          ConditionalExpression: increaseComplexity,
          LogicalExpression(node) {
            if (node.operator === "&&" || node.operator === "||") {
              increaseComplexity();
            }
          },
        };
      },
    },
  },
};
```
