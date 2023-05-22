import factory


class ParentCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'categories.Category'

    title = factory.Faker("word")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'categories.Category'

    title = factory.Faker("word")
    parent = factory.SubFactory(ParentCategoryFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    first_name = factory.Faker("word")
    email = factory.Faker('word')
    age = factory.Faker("pyint")
    password = f"{factory.Faker('pyint')}{factory.Faker('word')}"


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blogs.Blog'

    title = factory.Faker("word")
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    body = factory.Faker("first_name")


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blogs.Comments'

    blog = factory.SubFactory(BlogFactory)
    user = factory.SubFactory(UserFactory)
    body = factory.Faker("word")
