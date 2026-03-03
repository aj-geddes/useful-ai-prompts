# Feature Module Structure

## Feature Module Structure

```typescript
// users.module.ts
import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { ReactiveFormsModule } from "@angular/forms";
import { UsersRoutingModule } from "./users-routing.module";
import { UsersListComponent } from "./components/users-list/users-list.component";
import { UserDetailComponent } from "./components/user-detail/user-detail.component";
import { UsersService } from "./services/users.service";

@NgModule({
  declarations: [UsersListComponent, UserDetailComponent],
  imports: [CommonModule, ReactiveFormsModule, UsersRoutingModule],
  providers: [UsersService],
})
export class UsersModule {}
```
