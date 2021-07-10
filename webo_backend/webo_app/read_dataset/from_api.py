from pybliometrics.scopus import (
    AffiliationSearch,
    AuthorSearch,
    ScopusSearch,
    AuthorRetrieval,
)


def select_one_item(field, delimiter_one, delimiter_two):
    singular_field = ""
    if field == "NoneType":
        pass
    for name in field:
        singular_field += name

        if str(delimiter_one) in name:
            singular_field = singular_field[:-1]
            break

    return singular_field


def affiliation_search():
    query = "AFFIL( Covenant University)"
    s = AffiliationSearch(query)
    print(s.affiliations)


# affiliation_search()


def author_search():
    s = AuthorSearch("FIRST(badejo) and AUTHFIRST(joke)")
    print(s.authors, sep=",")


# author_search()


def scopus_search(author_name, author_id_user, eid, refresh=False, fields=["eid"]):
    print(author_name, author_id_user, eid)
    # q = 'FIRSTAUTH ( '+str(author_name)+' )'
    q = "EID ( " + str(eid) + " )"
    funds = []
    count = 0

    data = ScopusSearch(q, refresh=refresh, integrity_fields=fields).results

    for items in data:

        try:
            author_id = select_one_item(items.author_ids, ";", ",")
            if author_id == str(author_id_user):
                # print(author_id)
                affilation_name = (
                    select_one_item(items.affilname, ";", ";")
                    if select_one_item(items.affilname, ";", ";")
                    else ""
                )

                affiliation_city = (
                    select_one_item(items.affiliation_city, ";", ";")
                    if select_one_item(items.affiliation_city, ";", ";")
                    else ""
                )

                affiliation_country = (
                    select_one_item(items.affiliation_country, ";", ";")
                    if select_one_item(items.affiliation_country, ";", ";")
                    else ""
                )

                author_count = items.author_count
                author_keywords = items.authkeywords
                open_access = items.openaccess
                sponsor_number = items.fund_no
                sponsor_name = items.fund_sponsor
                cover_date = items.coverDate
                publication_name = items.publicationName
                auth_keywords = items.authkeywords
                citedby_count = items.citedby_count
                open_access = items.openaccess
                fund_acr = items.fund_acr
                fund_no = items.fund_no
                fund_sponsor = items.fund_sponsor
                eid = items.eid
                doi = items.doi
                title = items.title
                author_names = select_one_item(items.author_names, ";", ";")
                aggregation_type = items.aggregationType

                return (
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
                )

        except Exception as e:
            print(e, "this error is from from_api.py")
            pass

    # return affilation_name, affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name, cover_date, author_afid, publication_name, auth_keywords, citedby_count, fund_acr, fund_no, fund_sponsor, doi, title, author_names, aggregation_type


# print(scopus_search(author_name="Shi, W",
#                     author_id_user="7402664239", eid="2-s2.0-77956877124"))


def author_retrieval():
    au = AuthorRetrieval(57202237253)

    print(au.indexed_name)
    print(au.citation_count)
    print(au.h_index)
    print(au.orcid)
    print(au.publication_range)
    print(au.affiliation_current)
    # print(au.affiliation_history)
    print(au.get_documents)


# author_retrieval()
