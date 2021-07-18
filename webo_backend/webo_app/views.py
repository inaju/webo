from .models import (
    ResearchField,
    ResearchPaperDetail,
    Author,
    Affliation,
    AuthorKeywords,
    Sponsor,
)
from .read_dataset import read_csv, from_api
from django.http import HttpResponse

# Create your views here.


def populate_database(request):
    length_of_data_set = read_csv.return_length()
    dataset_name = read_csv.return_dataset_name()

    print(type(length_of_data_set))
    item_id = 0
    current_field = ""
    current_author = ""
    current_affiliation = ""

    while length_of_data_set != item_id:
        try:
            (
                single_author,
                single_author_id,
                item_source,
                title,
                year,
                document_type,
                eid,
                link,
                doi,
                cited_by,
            ) = read_csv.main_response(item_id)

            print(single_author, single_author_id, item_source)
            (
                affiliation_country,
                affilation_name,
                affiliation_city,
                author_count,
                author_keywords,
                open_access,
                sponsor_number,
                sponsor_name,
                cover_date,
                publication_name,
                auth_keywords,
                citedby_count,
                open_access,
                fund_acr,
                fund_no,
                fund_sponsor,
                eid,
                doi,
                title,
                author_names,
                aggregation_type,
            ) = from_api.scopus_search(
                author_name=single_author, author_id_user=single_author_id, eid=eid
            )

            # saving the research field
            try:
                research_field = ResearchField.objects.get(
                    field_name=dataset_name)
                current_field = research_field
            except Exception as e:
                # print(e)
                # print(e.args)

                field = ResearchField.objects.create(field_name=dataset_name)

                current_field = field

            # Saving Affliation
            try:
                print("trying affliation")
                affiliation_instance = Affliation.objects.get(
                    name=affilation_name,
                    city=affiliation_city,
                    country=affiliation_country,
                )
                print(affiliation_instance,
                      "this is affliation instance before except")

                current_affiliation = affiliation_instance

            except Exception as e:
                print(e, "new wine")
                print(e.args)
                affliation_instance = Affliation.objects.create(
                    name=affilation_name,
                    city=affiliation_city,
                    country=affiliation_country,
                )

                current_affiliation = affiliation_instance
                print("saved affliation")
                print(current_affiliation)

            # saving the author
            try:
                author_instance = Author.objects.get(
                    name=single_author,
                    author_id=single_author_id,
                    affiliation=current_affiliation,
                )
                current_author = author_instance
            except Exception as e:
                print(e)
                print(e.args)

                author_instance = Author.objects.create(
                    name=single_author,
                    author_id=single_author_id,
                    affiliation=current_affiliation,
                )
                current_author = author_instance
                print("saved author")

            # saving the author keyword
            try:
                author_keyword_instance = AuthorKeywords.objects.get(
                    keyword=author_keywords
                )
            except Exception as e:
                print(e)
                print(e.args)

                author_keyword_instance = AuthorKeywords.objects.create(
                    keyword=author_keywords,
                )
                print("Saved keyword")

            # saving the sponsor
            try:
                sponsor_instance = Sponsor.objects.get(
                    fund_no=sponsor_number, fund_sponsor=sponsor_name
                )
                sponsor_instance = sponsor_instance

            except Exception as e:
                print(e)
                print(e.args)

                sponsor_instance = Sponsor.objects.create(
                    fund_no=sponsor_number, fund_sponsor=sponsor_name
                )
                print("saved sponsor")

            # save the research field with the current author
            try:
                research_paper_instance = ResearchPaperDetail.objects.get(
                    title=title,
                )

            except:
                # print("error Saving research paper")
                # print(e)

                ResearchPaperDetail.objects.create(
                    research_field=current_field,
                    author=current_author,
                    title=title,
                    doi=doi,
                    eid=eid,
                    year=year,
                    document_type=document_type,
                    link=link,
                    cited_by=citedby_count,
                    affiliation=current_affiliation,
                    author_count=author_count,
                    author_keyword=author_keyword_instance,
                    sponsor=sponsor_instance,
                    open_access=open_access,
                )
                print("Saved research paper")

            item_id += 1
            print(item_id)
        except Exception as e:
            print(e)
            item_id += 1
            print("skipped: ", item_id)


def populate_database_(request):

    length_of_data_set = read_csv.return_length()
    dataset_name = read_csv.return_dataset_name()

    print(type(length_of_data_set))
    item_id = 0
    current_field = ""
    current_author = ""
    current_affiliation = ""

    while length_of_data_set != item_id:

        (
            single_author,
            single_author_id,
            item_source,
            title,
            year,
            document_type,
            eid,
            link,
            doi,
            cited_by,
        ) = read_csv.main_response(item_id)

        print(single_author, single_author_id, item_source)
        (
            affiliation_country,
            affilation_name,
            affiliation_city,
            author_count,
            author_keywords,
            open_access,
            sponsor_number,
            sponsor_name,
            cover_date,
            publication_name,
            auth_keywords,
            citedby_count,
            open_access,
            fund_acr,
            fund_no,
            fund_sponsor,
            eid,
            doi,
            title,
            author_names,
            aggregation_type,
        ) = from_api.scopus_search(
            author_name=single_author, author_id_user=single_author_id, eid=eid
        )

        # saving the research field
        try:
            research_field = ResearchField.objects.get(field_name=dataset_name)
            current_field = research_field
        except Exception as e:
            # print(e)
            # print(e.args)

            field = ResearchField.objects.create(field_name=dataset_name)

            current_field = field

        # saving the affiliation
        try:
            print("trying affliation")
            affiliation_instance = Affliation.objects.get(
                name=affilation_name,
                city=affiliation_city,
                country=affiliation_country,
            )
            print(affiliation_instance,
                  "this is affliation instance before except")

            current_affiliation = affiliation_instance

        except Exception as e:
            print(e, "new wine")
            print(e.args)
            affliation_instance = Affliation.objects.create(
                name=affilation_name,
                city=affiliation_city,
                country=affiliation_country,
            )

            current_affiliation = affiliation_instance
            print("saved affliation")
            print(current_affiliation)

        # saving the author
        try:
            author_instance = Author.objects.get(
                name=single_author,
                author_id=single_author_id,
                affiliation=current_affiliation,
            )
            current_author = author_instance
        except Exception as e:
            print(e)
            print(e.args)

            author_instance = Author.objects.create(
                name=single_author,
                author_id=single_author_id,
                affiliation=current_affiliation,
            )
            current_author = author_instance
            print("saved author")

        # saving the author keyword
        try:
            author_keyword_instance = AuthorKeywords.objects.get(
                keyword=author_keywords
            )
        except Exception as e:
            print(e)
            print(e.args)

            author_keyword_instance = AuthorKeywords.objects.create(
                keyword=author_keywords,
            )
            print("Saved keyword")

        # saving the sponsor
        try:
            sponsor_instance = Sponsor.objects.get(
                fund_no=sponsor_number, fund_sponsor=sponsor_name
            )

        except Exception as e:
            print(e)
            print(e.args)

            sponsor_instance = Sponsor.objects.create(
                fund_no=sponsor_number, fund_sponsor=sponsor_name
            )
            print("saved sponsor")

        # get the current author model object
        current_author = Author.objects.filter(author_id=single_author_id)

        # save the research field with the current author
        try:
            research_paper_instance = ResearchPaperDetail.objects.get(
                research_field=current_field,
                author=current_author[0],
                title=title,
                doi=doi,
                eid=eid,
                year=year,
                document_type=document_type,
                link=link,
                cited_by=cited_by,
                affiliation=current_affiliation,
                author_count=author_count,
                author_keyword=author_keyword_instance,
                sponsor=sponsor_instance,
                open_access=open_access,
            )
            print(doi)
            print("Saving research paper")

        except:
            # print("error Saving research paper")
            # print(e)

            research_paper_instance = ResearchPaperDetail.objects.create(
                research_field=current_field,
                author=current_author[0],
                title=title,
                doi=doi,
                eid=eid,
                year=year,
                document_type=document_type,
                link=link,
                cited_by=cited_by,
                affiliation=current_affiliation,
                author_count=author_count,
                author_keyword=author_keyword_instance,
                sponsor=sponsor_instance,
                open_access=open_access,
            )
            print("Saved research paper")

        print(item_id)
        item_id += 1

        # print(item_id)
        # item_id += 1

    return HttpResponse("ok")


def field_count(request):
    field_count = ResearchPaperDetail.objects.count()
    print(field_count)
    return HttpResponse(field_count)
