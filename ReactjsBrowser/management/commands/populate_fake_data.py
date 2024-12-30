from django.core.management.base import BaseCommand
from ReactjsBrowser.models import Blog, Author, Entry
import random
from datetime import date, timedelta
from faker import Faker

class Command(BaseCommand):
    help = 'Populate fake data for the application'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Create a Blog instance
        Blog.objects.all().delete()
        Author.objects.all().delete()
        Entry.objects.all().delete()

        # Generate Blogs
        blogs = []
        for _ in range(10):
            blog = Blog.objects.create(
                name=fake.company(),
                tagline=fake.catch_phrase(),
            )
            blogs.append(blog)

        # Generate Authors
        authors = []
        for _ in range(20):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.email(),
            )
            authors.append(author)

        # Generate Entries
        for _ in range(50):
            entry = Entry.objects.create(
                blog=random.choice(blogs),
                headline=fake.sentence(nb_words=6),
                body_text=fake.paragraph(nb_sentences=5),
                pub_date=fake.date_between(start_date="-2y", end_date="today"),
                mod_date=date.today() - timedelta(days=random.randint(0, 30)),
                number_of_comments=random.randint(0, 100),
                number_of_pingbacks=random.randint(0, 50),
                rating=random.randint(1, 10),
            )
            entry.authors.add(*random.sample(authors, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS("Successfully created 50 entries, 10 blogs, and 20 authors!"))
