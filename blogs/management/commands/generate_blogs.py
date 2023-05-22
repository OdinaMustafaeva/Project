from django.core.management.base import BaseCommand

from factories import BlogFactory, CommentFactory


class Command(BaseCommand):
    help = 'Generate Blogs'

    def handle(self, *args, **options):
        BlogFactory.create_batch(size=10000)
        CommentFactory.create_batch(size=500)
        self.stdout.write(self.style.SUCCESS('Successfully generated Blogs and comments.'))
