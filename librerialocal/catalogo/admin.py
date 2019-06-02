from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)


class BookInline(admin.TabularInline):
	model = Book 

	
#redefine la clase Admin para el modelo Author
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name','last_name',('date_of_birth','date_of_death')]
	#exclude = ('date_of_death',) #atributo exclude se utiliza para ocultar campos
	inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)



class BooksInstanceInline(admin.TabularInline):
	'''
	Esta clase se utiliza para generar una edición de los Libros de forma masiva
	'''
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]  #muestra Instancias de un libro en el detalle, en forma de lista para edición en línea

	
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None,
			{
				'fields': ('book', 'imprint', 'id')
			}
		),
		('Availability',
			{
				'fields': ('status','due_back')
			}

		)

	)
