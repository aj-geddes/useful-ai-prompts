# Flexbox Responsive Navigation

## Flexbox Responsive Navigation

```html
<!-- HTML -->
<nav class="navbar">
  <div class="navbar-brand">Logo</div>
  <button class="navbar-toggle" id="menuToggle">Menu</button>
  <ul class="navbar-menu" id="navMenu">
    <li><a href="#home">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px;
    background-color: #333;
    color: white;
  }

  .navbar-brand {
    font-size: 24px;
    font-weight: bold;
  }

  .navbar-toggle {
    display: block;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 24px;
  }

  .navbar-menu {
    display: none;
    list-style: none;
    flex-direction: column;
    position: absolute;
    top: 60px;
    left: 0;
    right: 0;
    background-color: #222;
    padding: 16px;
    gap: 8px;
  }

  .navbar-menu.active {
    display: flex;
  }

  @media (min-width: 768px) {
    .navbar-toggle {
      display: none;
    }

    .navbar-menu {
      display: flex;
      flex-direction: row;
      position: static;
      background-color: transparent;
      padding: 0;
      gap: 32px;
    }
  }

  .navbar-menu a {
    color: white;
    text-decoration: none;
  }
</style>
```
