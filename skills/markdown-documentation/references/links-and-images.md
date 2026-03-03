# Links and Images

## Links and Images

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Link title")

Reference-style link:
[Link text][reference]
[reference]: https://example.com

Automatic link:
<https://example.com>
<email@example.com>

![Alt text](image.png)
![Alt text](image.png "Image title")

Reference-style image:
![Alt text][image-ref]
[image-ref]: image.png
```


## Code Blocks

````markdown
Inline code: `const x = 5;`

Code block with language:

```javascript
function hello(name) {
  console.log(`Hello, ${name}!`);
}
```

```python
def hello(name):
    print(f"Hello, {name}!")
```

```bash
npm install
npm start
```

Indented code block (4 spaces):
const x = 5;
console.log(x);
````


## Tables

```markdown
Simple table:
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1 | Data | Data |
| Row 2 | Data | Data |

Aligned columns:
| Left | Center | Right |
|:-----|:------:|------:|
| Left | Center | Right |
| Text | Text | Text |

Minimal table:
Column 1 | Column 2
---------|----------
Data | Data
Data | Data
```
