from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    resume = models.FileField(upload_to='documents/', null=True, blank=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('PROG', 'Programming Languages'),
        ('FRAM', 'Frameworks'),
        ('TOOL', 'Tools & Technologies'),
        ('SOFT', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 rating

    def __str__(self) -> str:
        category_display = dict(self.CATEGORY_CHOICES).get(self.category, self.category)
        return str(f"{self.name} - {category_display}")

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_pics/', null=True, blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Skill)
    date_completed = models.DateField()

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ['-date_completed']
