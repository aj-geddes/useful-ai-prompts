# State Management with Redux

## State Management with Redux

```javascript
import { createSlice, configureStore } from "@reduxjs/toolkit";
import { useSelector, useDispatch } from "react-redux";

const itemsSlice = createSlice({
  name: "items",
  initialState: { list: [], loading: false, error: null },
  reducers: {
    setItems: (state, action) => {
      state.list = action.payload;
      state.loading = false;
    },
    setLoading: (state) => {
      state.loading = true;
    },
    setError: (state, action) => {
      state.error = action.payload;
      state.loading = false;
    },
  },
});

export const store = configureStore({
  reducer: { items: itemsSlice.reducer },
});

export function HomeScreen() {
  const dispatch = useDispatch();
  const { list, loading, error } = useSelector((state) => state.items);

  React.useEffect(() => {
    dispatch(setLoading());
    fetch("https://api.example.com/items")
      .then((r) => r.json())
      .then((data) => dispatch(setItems(data)))
      .catch((err) => dispatch(setError(err.message)));
  }, [dispatch]);

  if (loading) return <ActivityIndicator size="large" />;
  if (error) return <Text>Error: {error}</Text>;

  return (
    <ScrollView>
      {list.map((item) => (
        <ItemCard key={item.id} item={item} />
      ))}
    </ScrollView>
  );
}
```
