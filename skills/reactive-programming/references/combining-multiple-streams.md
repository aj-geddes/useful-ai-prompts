# Combining Multiple Streams

## Combining Multiple Streams

```typescript
import { combineLatest, merge, forkJoin, zip } from "rxjs";

// combineLatest - emits when any input emits
const users$ = fetchUsers();
const settings$ = fetchSettings();

combineLatest([users$, settings$]).subscribe(([users, settings]) => {
  console.log("Users:", users);
  console.log("Settings:", settings);
});

// merge - combine multiple observables
const clicks$ = fromEvent(button1, "click");
const hovers$ = fromEvent(button2, "mouseover");

merge(clicks$, hovers$).subscribe((event) => {
  console.log("Event:", event.type);
});

// forkJoin - wait for all to complete (like Promise.all)
forkJoin({
  users: fetchUsers(),
  posts: fetchPosts(),
  comments: fetchComments(),
}).subscribe(({ users, posts, comments }) => {
  console.log("All data loaded:", { users, posts, comments });
});

// zip - combine corresponding values
const names$ = of("Alice", "Bob", "Charlie");
const ages$ = of(25, 30, 35);

zip(names$, ages$).subscribe(([name, age]) => {
  console.log(`${name} is ${age} years old`);
});
```
