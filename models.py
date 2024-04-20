from django.db import models
class Author(models.Model):
    fullname=models.CharField(max_length=50)
    born_date=models.CharField(max_length=50)
    born_location=models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class Tag(models.Model):
    name=models.CharField(max_length=30,null=False,unique=True)
class Quote(models.Model):
    quote=models.TextField()
    tags=models.ManyToManyField(Tag)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    dependencies=[]
    operations=[
        migration.CreatedModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAuthorField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    )
                )
                ("fullname", models.CharField(max_length=50)),
                ("born_date", models.CharField(max_length=50)),
                ("born_location", models.CharField(max_length=150)),
                ("description", models.TextField(max_length=50)),
                ("fullname", models.DateTimeField(auto_now_add=True)),
            ]
        )
    ]