from django.contrib import admin

from administrator.models import Author, Book

# created a superuser with this command: python manage.py createsuperuser
# alireza, 123, a@gmail.com

# admin.site.register(Book)
# admin.site.register(Author)

# add an inline class to book that we can see books of author in author section.
class BookInline(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'birth_date', 'country'] # what should be display on admin list, default is just object of class.
    sortable_by = ['first_name', 'last_name'] # we can sort with first_name or last name. just click on first_name or last_name bar.
    list_filter = ['country'] # we added a filter by country.
    list_editable = ['country'] # we can edit country without go to detail of an object.
    search_fields = ['first_name'] # add a search field that we can search first_name in it.
    inlines = [BookInline] # add inline for author that we can see author books too.
    fields = [('first_name', 'last_name'), 'country'] # show just this fields. (firstname and lastname in one row)
    readonly_fields = ['country'] # we cant edit country in author detail.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'public_date', 'pages_count']