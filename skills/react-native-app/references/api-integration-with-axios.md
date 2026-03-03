# API Integration with Axios

## API Integration with Axios

```javascript
import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";

const apiClient = axios.create({
  baseURL: "https://api.example.com",
  timeout: 10000,
});

// Request interceptor for auth
apiClient.interceptors.request.use(
  async (config) => {
    const token = await AsyncStorage.getItem("authToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

// Response interceptor for token refresh
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refreshToken = await AsyncStorage.getItem("refreshToken");
        const { data } = await axios.post(
          "https://api.example.com/auth/refresh",
          { refreshToken },
        );
        await AsyncStorage.setItem("authToken", data.accessToken);
        apiClient.defaults.headers.Authorization = `Bearer ${data.accessToken}`;
        return apiClient(originalRequest);
      } catch (refreshError) {
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  },
);

export const fetchUser = () => apiClient.get("/user/profile");
export const fetchItems = (page) => apiClient.get(`/items?page=${page}`);
export const createItem = (data) => apiClient.post("/items", data);
```
