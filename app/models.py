from django.db import models

class User(models.Model):
    
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    # m, f save in database and male, female fore humen

    TYPE_CHOICES = (
        ('R', 'Regular'),
        ('P', 'Premium'),
    )

    username = models.CharField(max_length=50) # always we should use max_length in charfield
    email = models.EmailField()
    signing_date = models.DateTimeField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    account_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    # a function to change account_type when we call it.
    def change_account_type(self):
        if self.account_type == 'R':
            self.account_type = 'P'
        else:
            self.account_type = 'R'
        self.save()




class Post(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, related_name='posts', on_delete=models.SET) # a post object have one writer. one writer can have many posts.
    # writer = models.ManyToManyField(User) # a post can have many writers and a writer can have many posts.
    # writer = models.OneToOneField(User, on_delete=models.CASCADE) # a post can have one writer and each writer can gave just one post.

    # on_delete: if we delete writer of this post what will come to post object. we can use 6 items:
    # CASCADE: delete posts related to that user
    # PROTECT: we cant delete user object if we have related post to that
    # SET_NULL: set Null to writer of that post
    # SET_DEFAULT: if we use default, it will set that
    # SET('alireza'): writer will be 'alireza'
    # DO_NOTHING: nothing will be happen to posts.

# now we can reach writer from post object. for example we have a Post object with name clean_code. we can access writer with: "clean_code.writer" output: robert_martin
# if we want reach post from User: we have User object with name robert_martin. we can access post with: "robert_martin.posts.all()". if we dont have related_name we can use "robert_martin.post_set.all()". (pattern: <lower_case_model_name>_set)
# if we set related_name = '+' we cant have reverse access (from user to post).

# methods:

# create()
# user = User.objects.create(username="john_doe", email="john.doe@example.com", signing_date=timezone.now(),   gender='m', account_type='R')

# save()
# user = User(username="john_doe", email="john.doe@example.com", signing_date=timezone.now(), gender='m', account_type='R') # create an object from User class
# user.save() # save user in database

# delete()
# user.delete() # delete that user object we created


# django ORM:

# all()
# User.objects.all() # returns a queryset from all objects of User.

# filter()
# User.objects.filter(username='Alireza') # returns a queryset from all objects that have given conditions.

# get()
# user1 = User.objects.get(username='Alireza') # returns an object from User that have given conditions.
# user1.email # now we can have access to user1 fields like this.

# exclude()
# User.objects.exclude(username='Alireza') # returns a queryset from all objects except that have given conditions. opposite filter.

# order_by()
# User.objects.order_by('gender') # retuturns a queryset from all objects order by 'gender'. we can use '-gender' to reverse this list.

# count()
# User.objects.count() # returns an integer that count User objects.

# values()
# User.objects.all().values() # returns a list from dicts that have User objects with all content. we can write in values what fields we want: User.objects.all().values('username', 'gender')

# values_list()
# User.objects.all().values_list('id', 'username') # returns a list from tuples that have given fiels inside. if we just needed 'username' we could use flat in values_list: User.objects.all().values_list('username', flat=True)


# Field Lookups

# exact (if we use iexact ali=ALI): default
# Post.objects.filter(writer__username__exact='sajjad') # queryset of Posts that writer is sajjad.

# contains or icontains
# Post.objects.filter(content__contains='sajj') # return querysets that have sajj in content field.

# lt
# User.objects.filter(score__lt=3) # if we had score field in User model, it will return all users have score lower than 3.

# lte
# User.objects.filter(score__lte=3) # like lt just this shows equals too.

# gt 
# User.objects.filter(score__gt=3) # opposite of lt.

# gte 
# User.objects.filter(score__gte=3) # like gt just this shows equals too.

# startswith or istartswith
# User.objects.filter(username__startswith='ad') # return Users that usernames starts with 'ad' like 'admin'.

# endswith or iendswith
# User.objects.filter(username__endswith='n') # return Users that usernames ends with 'n' like 'admin'.

# in
# User.objects.filter(id__in=[1,4,6]) # return users with given id list.