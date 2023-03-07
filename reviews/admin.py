from django.contrib.admin import AdminSite
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin App'
    site_header = 'Bookr Admin App'
    index_title = 'Bookr Admin App'

admin_site=BookrAdminSite(name='bookr')

# Register your models here
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
