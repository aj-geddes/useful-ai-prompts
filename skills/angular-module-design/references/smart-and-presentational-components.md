# Smart and Presentational Components

## Smart and Presentational Components

```typescript
// users-list.component.ts (Smart)
import { Component, OnInit } from "@angular/core";
import { Observable } from "rxjs";
import { UsersService } from "../../services/users.service";

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: "app-users-list",
  template: `
    <div>
      <h2>Users</h2>
      <button (click)="addUser()">Add User</button>
      <app-user-item
        *ngFor="let user of users$ | async"
        [user]="user"
        (delete)="deleteUser($event)"
      ></app-user-item>
    </div>
  `,
})
export class UsersListComponent implements OnInit {
  users$: Observable<User[]>;

  constructor(private usersService: UsersService) {
    this.users$ = this.usersService.users$;
  }

  ngOnInit(): void {
    this.usersService.getUsers().subscribe();
  }

  addUser(): void {
    // Navigation or modal logic
  }

  deleteUser(id: number): void {
    this.usersService.deleteUser(id).subscribe();
  }
}

// user-item.component.ts (Presentational)
import { Component, Input, Output, EventEmitter } from "@angular/core";

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: "app-user-item",
  template: `
    <div class="user-item">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <button (click)="onDelete()">Delete</button>
    </div>
  `,
  styleUrls: ["./user-item.component.css"],
})
export class UserItemComponent {
  @Input() user!: User;
  @Output() delete = new EventEmitter<number>();

  onDelete(): void {
    this.delete.emit(this.user.id);
  }
}
```
