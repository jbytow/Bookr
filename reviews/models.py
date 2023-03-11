from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="Publisher's name")
    website = models.URLField(help_text="Publisher's website")
    email = models.EmailField(help_text="Publisher's e-mail address")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="title")
    publication_date = models.DateField(verbose_name="Publication Date of the book")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)


class Contributor(models.Model):
    first_names = models.CharField(max_length=50, help_text="name or names of authors")
    last_names = models.CharField(max_length=50, help_text="last name or names of authors")
    email = models.EmailField(help_text="author's e-mail")

    def initialled_name(self):
        """ self.first_names='Jerome David', self.last_names='Salinger'
            => 'Salinger, JD' """
        initials = ''.join([name[0] for name
                            in self.first_names.split(' ')])
        return "{}, {}".format(self.last_names, initials)

    def __str__(self):
        return self.initialled_name()


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Role of the contributor", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.CharField(help_text="text of the review", max_length=99999999999)
    rating = models.IntegerField(help_text="user's rating", default=0)
    date_created = models.DateTimeField(auto_now_add=True, help_text="creation date")
    date_edited = models.DateTimeField(auto_now_add=True, help_text="edition date")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="reviewed book")
