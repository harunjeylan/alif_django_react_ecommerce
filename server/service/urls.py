from django.urls import path

from service import api

urlpatterns = [

  path("images/remove/", api.removeImage , name="remove_image"),

  path("categories/", api.getAllCategory , name="categories"),

  path("brands/", api.getAllBrands , name="brands"),
  path("brands/add/", api.addBrand , name="new_brand"),
  path("brands/update/", api.updateBrand , name="update_brand"),
  path("brands/delete/", api.deleteBrand , name="delete_brand"),

  path("discounts/", api.getAllDiscounts , name="discounts"),
  path("discounts/add/", api.addDiscount , name="new_discount"),
  path("discounts/update/", api.updateDiscount , name="update_discount"),
  path("discounts/delete/", api.deleteDiscount , name="delete_discount"),

  path("variants/", api.getAllVariants , name="variants"),
  path("variants/add/", api.addVariant , name="new_variant"),
  path("variants/update/", api.updateVariant , name="update_variant"),
  path("variants/delete/", api.deleteVariant , name="delete_variant"),
  path("variants/options/delete/", api.deleteOption , name="delete_option"),

  path("organize/", api.getOrganizes , name="organize"),
  path("organize/add/", api.addOrganize , name="new_organize"),
  path("organize/update/", api.updateOrganize , name="update_organize"),
  path("organize/delete/", api.deleteOrganize , name="delete_organize"),
  path("organize/categories/", api.getAllCategory , name="delete_organize"),

  # ===================================================================
  path("wishlists/", api.getWishlist , name="wishlists"),
  path("wishlists/toggle/", api.toggleWishlist , name="toggle_wishlists"),


  path("orders/", api.getOrders , name="order"),
  path("orders/add/", api.addOrder , name="new_order"),
  path("orders/update/", api.updateOrder , name="update_order"),
  path("orders/<pk>/", api.getOrderDetails , name="order_details"),

  path("admin/dashboard/", api.getDashboardData, name="get_dashboard_data"),
  path("admin/orders/", api.getOrdersForAdmin , name="order_for_admin"),
  path("admin/orders/<pk>/", api.getOrderDetailsForAdmin , name="order_details_for_admin"),
  # path("admin/orders/delete/", api.deleteOrderForAdmin , name="delete_orders_for_admin"),


]