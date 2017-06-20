#Импорт необходимых модулей
import csv,sys,os

#Указываем путь до папки проекта Django в котором находится файл settings.py
project_dir = "/home/webme/Import-CSV-into-Django/project/thesite"

#Добавляем в переменную sys.path путь до проекта Django
sys.path.append(project_dir)

#Определяем переменную с настройками Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#Импортируем модуль Django
import django

#Загружаем настройки Django
django.setup()

#Импортируем модель Post
from blog.models import Post

#Считываем CSV-файл
data = csv.reader(open("/home/webme/Import-CSV-into-Django/project/data.csv"),delimiter=',')

for row in data:
	#Пропускаем заголовки
	if row[0] != 'create_date':
		post = Post()
		post.create_date = row[0]
		post.title = row[1]
		post.content = row[2]
		post.save()
