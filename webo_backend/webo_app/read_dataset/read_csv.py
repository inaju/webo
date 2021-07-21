from pybliometrics.scopus import (
    AuthorRetrieval,
    AffiliationRetrieval,
    CitationOverview,
    PlumXMetrics,
    AbstractRetrieval,
)
import os
import pandas as pd

parent_path = os.getcwd()
print(parent_path)

dataset_path = (
    parent_path + r"\webo_app\read_dataset\datasets\Communications_and_networking.csv"
)
dataset_name = "Communications And Networking"


def select_one_item(field, delimiter_one, delimiter_two):
    singular_field = ""
    for name in field:
        singular_field += name

        if str(delimiter_one) in name:
            singular_field = singular_field[:-1]
            break

        # if str(delimiter_one) and str(delimiter_two) in name:
        #     singular_field=singular_field[:-1]
        #     break

    # print(singular_field.title())
    return singular_field


def return_length():
    df = pd.read_csv(dataset_path, sep=",", delimiter=",")
    # df = df[0].str.split(',', expand=True)

    length_of_rows = len(df.index)
    # print(length_of_rows+1)
    return int(length_of_rows)


def return_dataset_name():
    return str(dataset_name)


def main_response(item_id):

    df = pd.read_csv(dataset_path, sep=",", delimiter=",")
    length_of_rows = len(df.index)

    for number in range(length_of_rows):

        author = df["Authors"][item_id]
        author_id = df["Author(s) ID"][item_id]
        title = df["Title"][item_id]
        year = df["Year"][item_id]
        source_title = df["Source title"][item_id]
        cited_by = df["Cited by"][item_id]
        doi = df["DOI"][item_id]
        document_type = df["Document Type"][item_id]
        eid = df["EID"][item_id]
        link = df["Link"][item_id]

        # ab = AbstractRetrieval(str(eid))
        # au = AuthorRetrieval(str(select_one_item(author_id,';',';')))

        # print(au.document_count)
        # print(au.h_index)
        # print(au.citation_count)
        # print(author)

        single_author = select_one_item(author, ".", ",")
        # single_author_id = select_one_item(author_id, ';', ';') if type(
        #     select_one_item(author_id, ';', ';')) == int else

        # single_author_id = select_one_item(author_id, ';', ';')
        if select_one_item(author_id, ";", ";") == "[No author id available]":
            single_author_id = 0
        else:
            single_author_id = select_one_item(author_id, ";", ";")

        if single_author == "[No author name available]":
            single_author = ""
        else:
            single_author = select_one_item(author, ".", ",")

        item_source = select_one_item(source_title, ",", ";")

        # print(title)
        # print(year)
        # print(document_type)
        # print(eid)
        # print(link)
        # print(doi)

        return (
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
        )


print(main_response(3))
# print(return_length())
