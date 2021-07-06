from pybliometrics.scopus import AffiliationSearch, AuthorSearch, ScopusSearch,AuthorRetrieval

def select_one_item(field, delimiter_one,delimiter_two):
    singular_field=''
    for name in field:
        singular_field+=name
        
        if str(delimiter_one) in name:
            singular_field=singular_field[:-1]
            break

    return singular_field

def author_retrieval(author_id):
    au = AuthorRetrieval(author_id)

    print(au.indexed_name)
    print(au.citation_count)
    print(au.h_index)
    print(au.orcid)
    print(au.publication_range)
    print(au.affiliation_current)
    # print(au.affiliation_history)
    print(au.get_documents)

    



def affiliation_search():
    query = "AFFIL( Covenant University)"
    s = AffiliationSearch(query)
    print(s.affiliations)

# affiliation_search()

def author_search():
    s = AuthorSearch('FIRST(badejo) and AUTHFIRST(joke)')
    print(s.authors, sep=",")

# author_search()

def scopus_search(author_name,author_id_user, eid, refresh=False, fields=["eid"]):
    
    q='FIRSTAUTH ( '+str(author_name)+' )'
    funds=[]
    count=0
    
    
    data = ScopusSearch(q, refresh=refresh, integrity_fields=fields).results
    
    for items in data:
        author_id=select_one_item(items.author_ids,";",',')
        # print(items)
        if str(author_id) == str(author_id_user) and eid == str(items.eid):

            affilation_name=str(select_one_item(items.affilname,';',';'))
            affiliation_city=str(select_one_item(items.affiliation_city,';',';'))
            affiliation_country=select_one_item(items.affiliation_country,';',';')
            author_count=items.author_count
            author_keywords=items.authkeywords
            open_access=items.openaccess

            # if items.fund_no != "undefined":
            sponsor_number=items.fund_no
            sponsor_name=items.fund_sponsor

            
            return affilation_name,affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name
        else:
            print("no id")
            # else:
            #     sponsor_number=0
            #     sponsor_name=""




            # print('author_ids: ',items.author_ids)
            # print('eid: ',items.eid)
            # print('doi: ',items.doi)
            # print('pii: ',items.pii)
            # print('pubmed_id: ',items.pubmed_id)
            # print('title: ',items.title)
            # print('creator: ',items.creator)
            # print('affilname: ',select_one_item(items.affilname,';',';'))
            # print('affiliation_city: ',select_one_item(items.affiliation_city,';',';'))
            # print('affiliation_country: ',select_one_item(items.affiliation_country,';',';'))
            # print('author_count: ',items.author_count)
            # print('author_names: ',items.author_names)
            # print('description: ',items.description)
            # print('authkeywords: ',items.authkeywords)
            # print('citedby_count: ',items.citedby_count)
            # print('pubmed_id: ',items.pubmed_id)
            # print('fund_acr: ',items.fund_acr)
            # print('openaccess: ',items.openaccess)
            # print('pageRange: ',items.pageRange)
            # print('fund_no: ',items.fund_no)
            # print('fund_sponsor: ',items.fund_sponsor)

    # return affilation_name,affiliation_city, affiliation_country, author_count, author_keywords, open_access, sponsor_number, sponsor_name

# scopus_search(author_name="Atzori, L",author_id_user="57208011473", eid="2-s2.0-77956877124")

# author_retrieval()
