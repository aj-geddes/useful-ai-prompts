# Search with Debounce

## Search with Debounce

```typescript
import { fromEvent } from "rxjs";
import {
  debounceTime,
  distinctUntilChanged,
  switchMap,
  catchError,
} from "rxjs/operators";
import { of } from "rxjs";

const searchInput = document.querySelector("#search") as HTMLInputElement;

const search$ = fromEvent(searchInput, "input").pipe(
  map((event: Event) => (event.target as HTMLInputElement).value),
  debounceTime(300), // Wait 300ms after typing
  distinctUntilChanged(), // Only if value changed
  switchMap((query) => {
    if (!query) return of([]);

    return fetch(`/api/search?q=${query}`)
      .then((res) => res.json())
      .catch(() => of([]));
  }),
  catchError((error) => {
    console.error("Search error:", error);
    return of([]);
  }),
);

search$.subscribe((results) => {
  console.log("Search results:", results);
  displayResults(results);
});

function displayResults(results: any[]) {
  // Update UI
}
```
