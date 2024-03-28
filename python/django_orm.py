from myapp.models import User, Post, Foo, Captain, Project, Lead

# ################ Simple INSERT queries ###############

# Create a new user
user = User.objects.create(username="alice123", is_admin=True)
# let's assume the default of is_admin is False
print(user.username)  # 'alice123'
print(user.is_admin)  # False

# ################ Simple SELECT queries ###############

# Get all users
users = User.objects.all()

# Get specific fields from all users
users_with_fields = User.objects.values('foo', 'bar')
# Equivalent to SELECT foo, bar FROM ...

# Get specific fields and apply aggregation
users_with_aggregation = User.objects.annotate(n_hats=Count('hats')).values('foo', 'n_hats', 'bar')
books = Book.objects.values('author').annotate(avg_price=Avg('price'))
books = Book.objects.values('author').annotate(total_price=Sum('price'))

# Equivalent to SELECT foo, COUNT(hats) AS n_hats, bar FROM ...

# ################ Applying WHERE clauses ###############

# Get posts with specific conditions
posts = Post.objects.filter(author_id=2)
# Equivalent to SELECT * FROM post WHERE author_id = 2;

from django.db.models import Q

# Get posts with AND conditions
posts_with_and_condition = Post.objects.filter(Q(author_id=12) & Q(status='active'))
# Equivalent to SELECT * FROM post WHERE author_id = 12 AND status = 'active';

# Get posts with OR conditions
posts_with_or_condition = Post.objects.filter(Q(author_id=12) | Q(author_id=13))
# Equivalent to SELECT * FROM post WHERE author_id = 12 OR author_id = 13;

# ################ Operators ###############

from django.db.models import F

# Get posts with specific conditions using operators
posts_with_operators = Post.objects.filter(
    Q(a=5) & Q(b=6) | Q(a=5) | Q(b=6) | Q(some_attribute__exact=3) | Q(some_attribute__isnull=True) |
    Q(some_attribute__isnull=False) | Q(some_attribute__in=[5, 6]) | Q(some_attribute__gt=6) |
    Q(some_attribute__gte=6) | Q(some_attribute__lt=10) | Q(some_attribute__lte=10) |
    Q(some_attribute__range=[6, 10]) | Q(some_attribute__in=[11, 15]) | Q(some_attribute__all=[1, 2]) |
    Q(some_attribute__icontains='hat') | Q(some_attribute__iexact='hat') | Q(some_attribute__istartswith='hat')
)
# Equivalent to corresponding Sequelize query

# ################ Operator Example ###############

# Get foos with specific conditions using operators
foos_with_operator_example = Foo.objects.filter(
    Q(rank__lt=1000) | Q(rank__exact=None) | Q(title__startswith='Boat') |
    Q(description__icontains='boat')
)
# Equivalent to corresponding Sequelize query

# ################ Simple UPDATE queries ###############

# Update users without a last name to "Doe"
User.objects.filter(last_name=None).update(last_name="Doe")

# ################ Simple DELETE queries ###############

# Delete users named "Jane"
User.objects.filter(first_name="Jane").delete()

# ################ Creating in bulk ###############

# Create captains in bulk
captains = Captain.objects.bulk_create([
    Captain(name="Jack Sparrow"),
    Captain(name="Davy Jones")
])

# ################ Grouping ###############

# Group projects by name
projects_grouped_by = Project.objects.values('name').annotate()
# Equivalent to GROUP BY name in Sequelize

# ################ Limits and Pagination ###############

# Skip 5 instances and fetch the 5 after that
projects_paginated = Project.objects.all()[5:10]

# ################ max, min, and sum ###############

# Get max age of users
max_age = User.objects.aggregate(max_age=Max('age'))

# Get min age of users
min_age = User.objects.aggregate(min_age=Min('age'))

# Get sum of ages of users
sum_of_ages = User.objects.aggregate(sum_of_ages=Sum('age'))

# ################ increment, decrement ###############

# Increment age of a user
User.objects.filter(id=1).update(age=F('age') + 5)
# Will increase age to 5

# Decrement age of a user
User.objects.filter(id=1).update(age=F('age') - 5)
# Will decrease age to 5

# ################ count ###############

# Count leads by status
counts_by_status = Lead.objects.values('status').annotate(count=Count('status'))
# Equivalent to SELECT status, COUNT(*) as count FROM Lead GROUP BY status



# Retrieve books and their authors where the author exists
books_with_authors = Book.objects.select_related('author').all()

# Retrieve all authors and their books (including authors with no books)
authors_with_books = Author.objects.prefetch_related('book_set').all()

# Get all books written by authors under a certain publisher
publisher = Publisher.objects.get(name='Publisher Name')
books = Book.objects.filter(author__publisher=publisher)



