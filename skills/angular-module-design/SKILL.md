---
name: angular-module-design
description: Design Angular modules using feature modules, lazy loading, and dependency injection. Use when organizing large Angular applications with proper separation of concerns.
---

# Angular Module Design

## Overview

Architect scalable Angular applications using feature modules, lazy loading, services, and RxJS for reactive programming patterns.

## When to Use

- Large Angular applications
- Feature-based organization
- Lazy loading optimization
- Dependency injection patterns
- Reactive state management

## Implementation Examples

### 1. **Feature Module Structure**

```typescript
// users.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UsersRoutingModule } from './users-routing.module';
import { UsersListComponent } from './components/users-list/users-list.component';
import { UserDetailComponent } from './components/user-detail/user-detail.component';
import { UsersService } from './services/users.service';

@NgModule({
  declarations: [UsersListComponent, UserDetailComponent],
  imports: [CommonModule, ReactiveFormsModule, UsersRoutingModule],
  providers: [UsersService]
})
export class UsersModule {}
```

### 2. **Lazy Loading Routes**

```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  {
    path: 'users',
    loadChildren: () => import('./features/users/users.module')
      .then(m => m.UsersModule)
  },
  {
    path: 'products',
    loadChildren: () => import('./features/products/products.module')
      .then(m => m.ProductsModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

### 3. **Service with RxJS**

```typescript
// users.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

interface User {
  id: number;
  name: string;
  email: string;
}

@Injectable({ providedIn: 'root' })
export class UsersService {
  private usersSubject = new BehaviorSubject<User[]>([]);
  public users$ = this.usersSubject.asObservable();

  constructor(private http: HttpClient) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users').pipe(
      tap(users => this.usersSubject.next(users)),
      catchError(error => {
        console.error('Error fetching users:', error);
        return throwError(() => new Error('Failed to load users'));
      })
    );
  }

  getUserById(id: number): Observable<User> {
    return this.http.get<User>(`/api/users/${id}`);
  }

  createUser(user: Omit<User, 'id'>): Observable<User> {
    return this.http.post<User>('/api/users', user).pipe(
      tap(newUser => {
        const currentUsers = this.usersSubject.value;
        this.usersSubject.next([...currentUsers, newUser]);
      })
    );
  }

  updateUser(id: number, user: User): Observable<User> {
    return this.http.put<User>(`/api/users/${id}`, user).pipe(
      tap(updatedUser => {
        const currentUsers = this.usersSubject.value;
        const index = currentUsers.findIndex(u => u.id === id);
        if (index !== -1) {
          currentUsers[index] = updatedUser;
          this.usersSubject.next([...currentUsers]);
        }
      })
    );
  }

  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`/api/users/${id}`).pipe(
      tap(() => {
        const currentUsers = this.usersSubject.value;
        this.usersSubject.next(currentUsers.filter(u => u.id !== id));
      })
    );
  }
}
```

### 4. **Smart and Presentational Components**

```typescript
// users-list.component.ts (Smart)
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { UsersService } from '../../services/users.service';

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-users-list',
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
  `
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
import { Component, Input, Output, EventEmitter } from '@angular/core';

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-user-item',
  template: `
    <div class="user-item">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <button (click)="onDelete()">Delete</button>
    </div>
  `,
  styleUrls: ['./user-item.component.css']
})
export class UserItemComponent {
  @Input() user!: User;
  @Output() delete = new EventEmitter<number>();

  onDelete(): void {
    this.delete.emit(this.user.id);
  }
}
```

### 5. **Dependency Injection and Providers**

```typescript
// config.service.ts
import { Injectable } from '@angular/core';

interface AppConfig {
  apiUrl: string;
  environment: string;
}

@Injectable({ providedIn: 'root' })
export class ConfigService {
  private config: AppConfig = {
    apiUrl: 'https://api.example.com',
    environment: 'production'
  };

  get(key: keyof AppConfig): any {
    return this.config[key];
  }
}

// app.module.ts with providers
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { ConfigService } from './services/config.service';
import { AuthInterceptor } from './interceptors/auth.interceptor';

@NgModule({
  imports: [BrowserModule, HttpClientModule],
  providers: [
    ConfigService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ]
})
export class AppModule {}
```

## Best Practices

- Organize by feature modules
- Use lazy loading for large features
- Implement smart/presentational component pattern
- Use services for data and business logic
- Leverage RxJS for reactive patterns
- Use dependency injection for loose coupling
- Implement HTTP interceptors for global handling
- Use typed services and models

## Resources

- [Angular Documentation](https://angular.io/docs)
- [Angular Modules Guide](https://angular.io/guide/ngmodules)
- [RxJS Documentation](https://rxjs.dev)
- [Angular Services](https://angular.io/guide/architecture-services)
