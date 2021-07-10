from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ResearchPaperSerializer
from webo_app.models import ResearchPaperDetail
import collections


class GeneralPageApi(APIView):
    def get(self, request):

        year_frequency = []
        x_values = []
        y_values = []
        number_of_papers = 0
        number_of_authors = 0

        response_data = {
            "x": x_values,
            "y": y_values,
        }

        citation_final = 0
        max_response = 20
        research_paper_Detail = ResearchPaperDetail.objects.all()
        data = ResearchPaperSerializer(research_paper_Detail, many=True).data
        number_of_papers = len(data)

        for i in range(len(data)):
            year = str(data[i]["year"])
            citation = data[i]["cited_by"]
            author_count = data[i]["author_count"]
            citation_final += citation
            number_of_authors += author_count

            year_frequency.append(year)

        frequency = collections.Counter(year_frequency)
        frequency = dict(frequency)

        for items, v in frequency.items():
            x_values.append(items),
            y_values.append(v)

        x_values = x_values.sort(reverse=False)
        y_values = y_values.sort(reverse=False)

        print(x_values, y_values, number_of_papers)
        author_per_paper = number_of_authors / number_of_papers
        author_per_paper = round(author_per_paper, 2)
        response_data["number_of_papers"] = number_of_papers
        response_data["number_of_citations"] = citation_final
        response_data["author_per_paper"] = author_per_paper

        return Response(response_data)


class DocumentType(APIView):
    def get(self, request):

        year_frequency = []
        x_values = []
        y_values = []

        response_data = {
            "x": x_values,
            "y": y_values,
        }

        max_response = 20
        research_paper_Detail = ResearchPaperDetail.objects.all()
        data = ResearchPaperSerializer(research_paper_Detail, many=True).data

        for i in range(max_response):
            year = str(data[i]["document_type"])
            year_frequency.append(year)

        frequency = collections.Counter(year_frequency)
        frequency = dict(frequency)

        for items, v in frequency.items():
            x_values.append(items),
            y_values.append(v)

        print(response_data)
        return Response(response_data)


class Affiliation(APIView):
    def get(self, request):

        year_frequency = []
        x_values = []
        y_values = []

        response_data = {
            "x": x_values,
            "y": y_values,
        }

        max_response = 20
        research_paper_Detail = ResearchPaperDetail.objects.all()
        data = ResearchPaperSerializer(research_paper_Detail, many=True).data

        for i in range(max_response):
            year = str(data[i]["affiliation"])
            print(year)
            year_frequency.append(year)

        frequency = collections.Counter(year_frequency)
        frequency = dict(frequency)

        for items, v in frequency.items():
            x_values.append(items),
            y_values.append(v)

        print(response_data)
        return Response(response_data)
