import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "./cartReducer";
import wishlistReducer from "./wishlistReducer";

import { productApi } from "./products";

const store = configureStore({
  reducer: {
    cart: cartReducer,
    wishlist: wishlistReducer,
    [productApi.reducerPath]: productApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(productApi.middleware),
});

export default store;
