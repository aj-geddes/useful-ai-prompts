# Responsive Cards Component

## Responsive Cards Component

```html
<div class="card-grid">
  <div class="card">
    <img src="image.jpg" alt="Card image" class="card-image" />
    <div class="card-content">
      <h3>Card Title</h3>
      <p>Card description goes here</p>
      <a href="#" class="card-link">Learn More</a>
    </div>
  </div>
</div>

<style>
  .card-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
    padding: 16px;
  }

  @media (min-width: 640px) {
    .card-grid {
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      padding: 20px;
    }
  }

  @media (min-width: 1024px) {
    .card-grid {
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      padding: 24px;
    }
  }

  .card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition:
      transform 0.2s,
      box-shadow 0.2s;
  }

  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  }

  .card-image {
    width: 100%;
    height: auto;
    aspect-ratio: 16/9;
    object-fit: cover;
  }

  .card-content {
    padding: 16px;
  }

  .card-content h3 {
    margin: 0 0 8px;
    font-size: 18px;
  }

  .card-content p {
    margin: 0 0 12px;
    color: #666;
    font-size: 14px;
  }

  .card-link {
    display: inline-block;
    color: #0066cc;
    text-decoration: none;
    font-weight: 500;
  }
</style>
```
