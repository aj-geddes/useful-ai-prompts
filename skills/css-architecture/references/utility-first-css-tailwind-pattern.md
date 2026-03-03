# Utility-First CSS (Tailwind Pattern)

## Utility-First CSS (Tailwind Pattern)

```html
<!-- Utility classes provide granular control -->
<div class="flex flex-col gap-4 p-6 bg-white rounded-lg shadow-md">
  <h2 class="text-2xl font-bold text-gray-900">Title</h2>
  <p class="text-gray-600 leading-relaxed">Description</p>

  <div class="flex gap-2">
    <button
      class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
    >
      Primary
    </button>
    <button
      class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 transition"
    >
      Secondary
    </button>
  </div>
</div>

<style>
  /* Utility classes */
  .flex {
    display: flex;
  }
  .flex-col {
    flex-direction: column;
  }
  .gap-4 {
    gap: 1rem;
  }
  .gap-2 {
    gap: 0.5rem;
  }
  .p-6 {
    padding: 1.5rem;
  }
  .px-4 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  .py-2 {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
  .bg-white {
    background-color: white;
  }
  .bg-blue-500 {
    background-color: #3b82f6;
  }
  .text-white {
    color: white;
  }
  .text-gray-900 {
    color: #111827;
  }
  .text-2xl {
    font-size: 1.5rem;
  }
  .font-bold {
    font-weight: bold;
  }
  .rounded {
    border-radius: 0.375rem;
  }
  .rounded-lg {
    border-radius: 0.5rem;
  }
  .shadow-md {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
</style>
```
