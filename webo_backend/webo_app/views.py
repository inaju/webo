from .models import ResearchField,ResearchPaperDetail, Author, Affliation,AuthorKeywords, Sponsor
from .read_dataset import read_csv, from_api
from django.http import HttpResponse
# Create your views here.

def populate_database(request):

    length_of_data_set=read_csv.return_length()
    dataset_name=read_csv.return_dataset_name()

    print(type(length_of_data_set))
    item_id=0   
    current_field=''
    current_author=''
    current_affiliation=''

    try:
        research_field=ResearchField.objects.get(field_name=dataset_name)
        current_field=research_field
    except:
        print('researh field not present, saving now')
        field=ResearchField.objects.create(field_name=dataset_name)
        
        current_field=field

    #save the research field if it's not present in the database
    # while length_of_data_set != item_id:
        # if length_of_data_set == item_id:
        #     print("done populating the database")
        #     break
        # else:
    while length_of_data_set != item_id:

        single_author, single_author_id, item_source, title, year, document_type, eid, link,doi, cited_by=read_csv.main_response(item_id)
        check_for_title = ResearchPaperDetail.objects.filter(title=title)
        print(check_for_title)
        
        if check_for_title:
            print(item_id,'present') 
            break
        else:
            print(item_id,title," not present")

        # try:
        #     affilation_name,affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name=from_api.scopus_search(author_name=str(single_author),author_id_user=str(single_author_id), eid=str(eid))
        #     print(check_for_title)
        # except Exception as e:
        #     print(e)
            affilation_name,affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name="","","","","","","",""
            # affilation_name,affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name=from_api.scopus_search(author_name=str(single_author),author_id_user=str(single_author_id), eid=str(eid))
            print(affilation_name)
            
            #save the affiliation 
            try:

                affiliation_instance = Affliation.objects.get(
                            name=str(affilation_name),
                            city=str(affiliation_city),
                            country=str(affiliation_country),)

                current_affiliation=affiliation_instance

            except:
                affliation_instance = Affliation.objects.create(
                            name=str(affilation_name),
                            city=str(affiliation_city),
                            country=str(affiliation_country),

                            )
                current_affiliation=affiliation_instance


            #save the author 
            try:
                author_instance = Author.objects.get(name=single_author,author_id=single_author_id,affiliation=current_affiliation)
                current_author=author_instance
            except:
                author_instance=Author.objects.create(name=single_author,author_id=single_author_id,affiliation=current_affiliation)
                current_author=author_instance

            authors_keywords = AuthorKeywords.objects.create(
            keyword=author_keywords,
            )

            sponsor_instance = Sponsor.objects.create(
            fund_no = sponsor_number,
            fund_sponsor = sponsor_name
            )

        
            #get the current author model object
            current_author= Author.objects.filter(
                author_id=single_author_id
                )

            #save the research field with the current author 
            research_field_instance=ResearchPaperDetail.objects.create(
                research_field=current_field,
                author=current_author[0],
                title = title,
                doi = doi,
                eid = eid,
                year = year,
                document_type = document_type,
                link = link,
                cited_by=cited_by if type(cited_by)==int else 0,
                affiliation=current_affiliation,
                # author_count=author_count,
                author_keyword=authors_keywords,
                sponsor=sponsor_instance,
                # open_access=open_access,
            )

            print(item_id," title: "+str(check_for_title)) 
            
            item_id+=1

            #check for duplicates and delete only one record
            count=0
            for item in check_for_title:
                id=item.id
                count+=1
                if count == 2:
                    ResearchPaperDetail.objects.get(pk=id).delete()


    return HttpResponse(str(length_of_data_set)) 

    # return HttpResponse(str(check_author)+" is available")


def field_count(request):
    field_count = ResearchPaperDetail.objects.count()
    print(field_count)
    return HttpResponse(field_count)

