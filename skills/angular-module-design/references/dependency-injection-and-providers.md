# Dependency Injection and Providers

## Dependency Injection and Providers

```typescript
// config.service.ts
import { Injectable } from "@angular/core";

interface AppConfig {
  apiUrl: string;
  environment: string;
}

@Injectable({ providedIn: "root" })
export class ConfigService {
  private config: AppConfig = {
    apiUrl: "https://api.example.com",
    environment: "production",
  };

  get(key: keyof AppConfig): any {
    return this.config[key];
  }
}

// app.module.ts with providers
import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";
import { ConfigService } from "./services/config.service";
import { AuthInterceptor } from "./interceptors/auth.interceptor";

@NgModule({
  imports: [BrowserModule, HttpClientModule],
  providers: [
    ConfigService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
  ],
})
export class AppModule {}
```
