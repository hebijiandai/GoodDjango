import tablib
from blog.models import Author

data = tablib.Dataset()
data.headers = ['id', 'author', 'title', 'qualification', 'mark', 'blog', 'time']
Author_list = Author.objects.all()
for Author_unit in Author_list:
    data.append([Author_unit.id, Author_unit.author, Author_unit.title,
                 Author_unit.qualification, Author_unit.mark, Author_unit.blog, Author_unit.time])

print data.csv

