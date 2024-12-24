from django.contrib import admin, messages
from django.db.models import F
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
    fieldsets = (
        ('General Info', { # set General Info as title and set these fields inside it.
        'fields': ('title', 'public_date')
    }),
    ('Details', { # set Details as title and set these fields inside it.
        'classes': ('collapse',), # this is a css feature that hide content and we should click to show
        'fields': ('pages_count', 'author')
    })
    )
    
    actions = ['add_pages'] # add an action to do something (Delete selected books is default action and we add this action too).

    # this is a function to add pages_count +2 when we use it.
    def add_pages(self,request,queryset):
        updated = queryset.update(pages_count = F('pages_count') + 2)
        self.message_user( # message we will see after success.
            request, f'{updated} books page added with two', messages.SUCCESS
        )

    add_pages.short_description = 'Add two page to selected books.' # add a description to action. default is method name. (here 'Add pages'.)