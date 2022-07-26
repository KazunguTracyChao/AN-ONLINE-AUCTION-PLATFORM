from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='auctions/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='auctions/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='auctions/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='auctions/password_reset_done.html'), name='password_reset_complete'),

    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),

    path('profile', views.profile, name='profile'),
    path('profile/<int:pk>', views.update_profile, name='update_profile'),
    path("display_watchlist", views.display_watchlist, name="display_watchlist"),
    path("<int:listing_id>/add_watchlist",
         views.add_watchlist, name="add_watchlist"),
    path("<int:listing_id>/remove_watchlist",
         views.remove_watchlist, name="remove_watchlist"),

    path('display_category', views.display_category, name='display_category'),
    path('<int:listing_id>', views.display_listing, name='display_listing'),

    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("create_listing", views.create_listing, name="create_listing"),

    path("<int:listing_id>/new_bid", views.new_bid, name="new_bid"),
    path("<int:listing_id>/close_auction",
         views.close_auction, name="close_auction"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
