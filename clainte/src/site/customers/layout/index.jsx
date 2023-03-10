import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import Navbar from "./Navbar";
import Footer from "./Footer";
import CartMenu from "./CartMenu";
import LayoutProvider from "./LayoutContext";
import AccountMenu from "./AccountMenu";
import AccountDialog from "./AccountDialog";
import { useDispatch, useSelector } from "react-redux";
import { useSetGetWishlistMutation } from "../../../features/services/wishlistApiSlice";
import {
  selectWishlists,
  setWishlist,
} from "../../../features/services/wishlistReducer";
import { selectCurrentUser } from "../import";

function Customer({ children }) {
  const { pathname } = useLocation();
  const dispatch = useDispatch();
  const wishlists = useSelector(selectWishlists);
  const user = useSelector(selectCurrentUser);
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  const [setGetWishlist] = useSetGetWishlistMutation();

  useEffect(() => {
    if (user) {
      setGetWishlist({
        post: { products: wishlists.map((product) => product.id) },
      })
        .unwrap()
        .then((wishlistProducts) => {
          dispatch(setWishlist({ products: wishlistProducts }));
        });
    }
  }, [dispatch, setGetWishlist, user, wishlists]);

  return (
    <main>
      <LayoutProvider>
        <AccountDialog />
        <AccountMenu />
        <Navbar />
      </LayoutProvider>
      {children}
      <CartMenu />
      <Footer />
    </main>
  );
}

export default Customer;
