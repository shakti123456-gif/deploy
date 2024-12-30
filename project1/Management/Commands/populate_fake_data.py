from django.core.management.base import BaseCommand
from your_app.models import Blog, Author, Entry
from datetime import date

class Command(BaseCommand):
    help = 'Populate fake data'

    def handle(self, *args, **kwargs):
        blog = Blog.objects.create(name="Tech Trends", tagline="Latest updates in technology.")
        author = Author.objects.create(name="John Doe", email="john.doe@example.com")
        entry = Entry.objects.create(
            blog=blog,
            headline="Exploring AI Innovations",
            body_text="AI is advancing rapidly...",
            pub_date=date(2024, 12, 1),
            mod_date=date(2024, 12, 30),
            number_of_comments=10,
            number_of_pingbacks=2,
            rating=8,
        )
        entry.authors.add(author)
        self.stdout.write(self.style.SUCCESS("Fake data populated successfully."))
