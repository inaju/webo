from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ResearchPaperSerializer, ResearchFieldSerializer
from webo_app.models import ResearchPaperDetail, Author, Affliation, ResearchField, Sponsor
import collections


def get_frequency(frequency_list):

    x_values = []
    y_values = []

    response_data = {
        "x": x_values,
        "y": y_values,
    }

    frequency = collections.Counter(frequency_list)
    frequency = dict(frequency)
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for items, v in sorted_items:
        if items == "[No source information available]":
            pass

        if count == 10:
            break
        x_values.append(items),
        y_values.append(v)

        count += 1

    return response_data


@api_view(['POST'])
def GeneralPagePostApi(request):
    year_frequency = []
    x_values = []
    y_values = []
    document_type_frequency = []
    author_frequency = []
    open_access_frequency = []
    affiliation_frequency = []
    sponsor_list = []

    number_of_papers = 0
    number_of_authors = 0
    top_paper_dict = {}
    response_data = {
        "x": x_values,
        "y": y_values,
    }

    citation_final = 0
    max_response = 20

    if request.method == "POST":
        request_field = request.data
        print(request_field)

        research_field_request = ResearchField.objects.get(
            field_name=request_field)

        research_paper_Detail = ResearchPaperDetail.objects.filter(
            research_field=research_field_request)

        top_paper = ResearchPaperDetail.objects.filter(
            research_field=research_field_request).order_by('-cited_by')

        count = 0
        for items in top_paper:
            # print(items.title, items.cited_by, items.author, items.affiliation)
            top_paper_dict[str(count)] = {
                "title": items.title,
                "cited_by": items.cited_by,
                "author": items.author.name,
                "affiliation": items.affiliation.name
            }

            if count == 20:
                break
            count += 1

        data = ResearchPaperSerializer(research_paper_Detail, many=True).data

        number_of_papers = len(data)

        for i in range(len(data)):
            year = str(data[i]["year"])
            citation = data[i]["cited_by"]
            author_count = data[i]["author_count"]
            document_type = str(data[i]["document_type"])
            author = str(data[i]["author"])
            open_access = str(data[i]["open_access"])
            affiliation = str(data[i]["affiliation"])
            sponsor = str(data[i]["sponsor"])

            if open_access == '0':
                open_access = 'Paid'
            else:
                open_access = 'Free'

            citation_final += citation
            number_of_authors += author_count

            year_frequency.append(year)

            author = Author.objects.get(id=author)
            affiliation = Affliation.objects.get(id=affiliation)
            Sponsor_from_database = Sponsor.objects.get(id=sponsor)

            if Sponsor_from_database.fund_sponsor == None:
                pass
            else:
                sponsor_list.append(Sponsor_from_database.fund_sponsor)

            open_access_frequency.append(open_access)
            document_type_frequency.append(document_type)
            author_frequency.append(author.name)
            affiliation_frequency.append(affiliation.name)

        author_frequency_response = get_frequency(author_frequency)
        open_access_response = get_frequency(open_access_frequency)
        affiliation_response = get_frequency(affiliation_frequency)
        sponsor_response = get_frequency(sponsor_list)

        document_type_response = get_frequency(
            document_type_frequency)
        frequency = collections.Counter(year_frequency)
        frequency = dict(frequency)

        for items, v in frequency.items():

            x_values.append(items),
            y_values.append(v)

        x_values = x_values.sort(reverse=False)
        y_values = y_values.sort(reverse=False)

        # print(x_values, y_values, number_of_papers)
        author_per_paper = number_of_authors / number_of_papers
        citation_per_paper = citation_final / number_of_papers

        author_per_paper = round(author_per_paper, 2)
        citation_per_paper = round(citation_per_paper, 2)

        response_data["number_of_papers"] = number_of_papers
        response_data["number_of_citations"] = citation_per_paper
        response_data["author_per_paper"] = author_per_paper
        response_data["document_type"] = document_type_response

        response_data["author_frequency"] = author_frequency_response
        response_data["open_access"] = open_access_response
        response_data["affliation_response"] = affiliation_response
        response_data["sponsor_response"] = sponsor_response
        response_data["top_papers"] = top_paper_dict

        # print(response_data)
        return Response(response_data)


# class GeneralPageApi(APIView):
#     def get(self, request, field=''):

#         print(field)
#         print(field)
#         print(field)

#         year_frequency = []
#         x_values = []
#         y_values = []
#         number_of_papers = 0
#         number_of_authors = 0

#         response_data = {
#             "x": x_values,
#             "y": y_values,
#         }

#         citation_final = 0
#         max_response = 20
#         research_paper_Detail = ResearchPaperDetail.objects.all()
#         data = ResearchPaperSerializer(research_paper_Detail, many=True).data
#         number_of_papers = len(data)

#         for i in range(len(data)):
#             year = str(data[i]["year"])
#             citation = data[i]["cited_by"]
#             author_count = data[i]["author_count"]
#             citation_final += citation
#             number_of_authors += author_count

#             year_frequency.append(year)

#         frequency = collections.Counter(year_frequency)
#         frequency = dict(frequency)

#         for items, v in frequency.items():
#             x_values.append(items),
#             y_values.append(v)

#         x_values = x_values.sort(reverse=False)
#         y_values = y_values.sort(reverse=False)

#         print(x_values, y_values, number_of_papers)
#         author_per_paper = number_of_authors / number_of_papers
#         citation_per_paper = citation_final / number_of_papers

#         author_per_paper = round(author_per_paper, 2)
#         citation_per_paper = round(citation_per_paper, 2)

#         response_data["number_of_papers"] = number_of_papers
#         response_data["number_of_citations"] = citation_per_paper
#         response_data["author_per_paper"] = author_per_paper

#         return Response(response_data)


# class VisualizationPageApi(APIView):
#     def get(self, request):

#         document_type_frequency = []
#         author_frequency = []
#         open_access_frequency = []
#         affiliation_frequency = []

#         x_values = []
#         y_values = []

#         number_of_papers = 0
#         number_of_authors = 0

#         response_data = {
#             "x": x_values,
#             "y": y_values,
#         }

#         citation_final = 0
#         max_response = 20
#         research_paper_Detail = ResearchPaperDetail.objects.all()

#         data = ResearchPaperSerializer(research_paper_Detail, many=True).data
#         number_of_papers = len(data)

#         for i in range(len(data)):
#             document_type = str(data[i]["document_type"])
#             author = str(data[i]["author"])
#             open_access = str(data[i]["open_access"])
#             affiliation = str(data[i]["affiliation"])
#             if open_access == '0':
#                 open_access = 'Paid'
#             else:
#                 open_access = 'Free'

#             author = Author.objects.get(id=author)
#             affiliation = Affliation.objects.get(id=affiliation)

#             open_access_frequency.append(open_access)
#             document_type_frequency.append(document_type)
#             author_frequency.append(author.name)
#             affiliation_frequency.append(affiliation.name)
#         # print(affiliation_frequency)

#         author_frequency_response = get_frequency(author_frequency)
#         open_access_response = get_frequency(open_access_frequency)
#         affiliation_response = get_frequency(affiliation_frequency)

#         # print(affiliation_response)

#         frequency = collections.Counter(document_type_frequency)
#         frequency = dict(frequency)

#         for items, v in frequency.items():
#             if items == "[No source information available]":
#                 pass
#             else:
#                 x_values.append(items),
#                 y_values.append(v)

#         x_values = x_values.sort(reverse=False)
#         y_values = y_values.sort(reverse=False)

#         response_data["author_frequency"] = author_frequency_response
#         response_data["open_access"] = open_access_response
#         response_data["affliation_response"] = affiliation_response

#         return Response(response_data)
