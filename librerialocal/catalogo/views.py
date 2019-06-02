from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
	'''
	Función vista para para la página inicio del sitio
	'''
	#Genera contadores de algunos de los objetos principales
	var_num_libros = Book.objects.all().count()
	var_num_instances = BookInstance.objects.all().count()

	#Libros disponibles: campo status='a'
	var_num_libros_disponibles = BookInstance.objects.filter(status__exact='a').count()
	var_num_libros_con_inferno = BookInstance.objects.filter(book__title__exact='Inferno').count() #nótese como va al objeto book desde InstanceBook
	var_num_autores = Author.objects.count()
	var_num_generos = Genre.objects.count()

	return render(request,
		'index.html',
		context = {
			'var_num_libros': var_num_libros, 
			'var_num_instances': var_num_instances, 
			'var_num_libros_disponibles': var_num_libros_disponibles, 
			'var_num_autores': var_num_autores,
			'var_num_generos': var_num_generos,
			'var_num_libros_con_inferno': var_num_libros_con_inferno,
			},
		)

def BookListView(generic.ListView):
	model = Book

