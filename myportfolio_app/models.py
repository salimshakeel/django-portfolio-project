from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=50)
    greeting_1 = models.CharField(max_length=10)
    greeting_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to="picture/")

    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class About(models.Model):
    heading = models.CharField(max_length=15)
    career = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    Portfolio_img = models.ImageField(upload_to="portfolo_img/")
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.career


class Porfile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=20)


class Category (models.Model):
    name = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    def __str__(self):
        return self.skill_name

# Portfolio Sections


class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField(max_length=200)

    def __str__(self) -> str:
        return f'Portfolio {self.id}'
