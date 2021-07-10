from django.db import models

# Create your models here.


class ResearchField(models.Model):
    field_name = models.CharField(max_length=10000, unique=True)
    total_number_of_papers = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.field_name)


class ResearchPaperDetail(models.Model):
    research_field = models.ForeignKey("ResearchField", on_delete=models.CASCADE)
    affiliation = models.ForeignKey("Affliation", on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="author"
    )
    co_author = models.ForeignKey(
        "CoAuthor", on_delete=models.CASCADE, related_name="co_author", null=True
    )
    title = models.CharField(max_length=1000, unique=True)
    doi = models.CharField(max_length=10000, null=True, blank=True)
    eid = models.CharField(max_length=10000)
    year = models.BigIntegerField(default=0)
    document_type = models.CharField(max_length=10000)
    link = models.CharField(max_length=10000)
    cited_by = models.IntegerField(default=0)
    author_keyword = models.ForeignKey(
        "AuthorKeywords", on_delete=models.CASCADE, blank=True
    )
    sponsor = models.ForeignKey("Sponsor", on_delete=models.CASCADE, blank=True)
    open_access = models.IntegerField()
    author_count = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Author(models.Model):
    name = models.CharField(max_length=10000)
    author_id = models.BigIntegerField()
    affiliation = models.ForeignKey("Affliation", on_delete=models.CASCADE, null=True)
    total_number_of_papers_in_field = models.BigIntegerField(default=0, null=True)

    def __str__(self):
        return str(self.name)


class CoAuthor(models.Model):
    name = models.CharField(max_length=10000)
    author_id = models.BigIntegerField()
    affiliation = models.ForeignKey("Affliation", on_delete=models.CASCADE, null=True)
    total_number_of_papers_in_field = models.BigIntegerField(default=0, null=True)

    def __str__(self):
        return str(self.name)


class Affliation(models.Model):
    name = models.CharField(max_length=10000, unique=True)
    city = models.CharField(max_length=10000, blank=True)
    country = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return str(self.name)


class AuthorKeywords(models.Model):
    keyword = models.CharField(max_length=10000, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.keyword)


class Sponsor(models.Model):
    fund_no = models.CharField(max_length=10000, blank=True, null=True)
    fund_sponsor = models.CharField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return str(self.fund_sponsor)
