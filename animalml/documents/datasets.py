import requests
from bs4 import BeautifulSoup
import json
import os


def get_lila_dataset_info():
    r = requests.get("https://lila.science/datasets")
    if r.status_code == 200:
        # print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        article_list = soup.find_all('article')


        article_info_list = []
        for article in article_list:
            title_element = article.find('h2', class_='entry-title')
            # print(title_element)
            link = title_element.find('a').get('href') if title_element else "No title element found"
            # print(link)

            if '/datasets/' not in link:
                continue
            else:
                # title_element should have both link and name
                summary_element = article.find('div', class_='entry-summary')

                title = title_element.text.strip() if title_element else "No title element found"
                summary = summary_element.text.strip() if summary_element else "No summary element found"

                # append tuple of these things to a list?
                article_info = (title, link, summary)
                article_info_list.append(article_info)
    return article_info_list

def get_cloud_download_links(link):
    """"Finds download links on Lila data pages, saves them to a json or text file 
    for later use."""
    r = requests.get(link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        # looking for ul and li within the ul to get the text for each link. 
        # order always appears to be google, amazon, azure
        link_list = soup.find_all('li')
        text_links = []
        for down_link in link_list:
            if '/' not in str(down_link.text.strip()):
                continue
            else:
                text_links.append(down_link.text.strip())
        # list comp to remove anything after a space in the now text strings
        new_text_links = [x.split()[0] for x in text_links]
        if len(new_text_links) < 3:
            # need to back fill these with "No link found" for each missing link
            num_links = len(new_text_links)
            if num_links == 0:
                new_text_links.extend(["No link found", "No link found", "No link found"])
            elif num_links == 1:
                new_text_links.extend(["No link found", "No link found"])
            elif num_links == 2:
                new_text_links.append("No link found")
        # print(new_text_links)
    return new_text_links





def build_dataset_database():
    # this will be a first time booting up / periodic by choice thing to scrape 
    # all the data from Lila, and hold it in a text file internally for later use
    # this is to prevent overuse of scraping / keeping to fair use for lila
    all_article_list = []
    article_info = get_lila_dataset_info()
    for article in article_info:
        page_link = article[1]
        download_links = get_cloud_download_links(page_link)
        # rebuild the tuple to save to a file? 
        # new_article_info = (article, download_links)
        # full_info.append(new_article_info)
        article_dict = {'datasetName' : article[0],
                        'pageLink' : article[1],
                        'summary' : article[2],
                        'gsDownload' : download_links[0],
                        's3Download': download_links[1],
                         'azureDownload' : download_links[2]
                         }
        all_article_list.append(article_dict)
        # I might want to edit this to be a json actually, where we use the name as the primary key?

    return all_article_list

def download_lila_data(): # probably wants a dataset as input?
    return None
    # print(article_info_list)

def save_to_json(data, filename='database.json'):
    file_path = os.path.join('../data', filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
def load_from_json(filename='database.json'):
    file_path = os.path.join('../data', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)


def main():
    # get_cloud_download_links('https://lila.science/datasets/nacti')
    all_article_list = build_dataset_database()
    # save it as a json for now / in the future?
    save_to_json(all_article_list)

if __name__ == "__main__":
    main()
    # links 
    # html_list = soup.find_all('a')
    # link_list = []
    # for link in html_list:
    #     link_ref = link.get('href')
    #     if '/datasets/' not in link_ref:
    #         continue
    #         # print(link_ref)
    #     else:
    #         link_list.append(link_ref)
    # OK so now have the list to serve to the html, but also want to get the names for simplicity?

    # names
    



# So now have the links, need the names, and once have those need to get the links for download
# info is in the  <div class="entry-summary"> tag
# name is in <h2 class="entry-title">
# Downloading the data is the section these are kept in, and typically have the following syntax
# Images are available in the following cloud storage folders:
#    gs://public-datasets-lila/nacti-unzipped (GCP)
#    s3://us-west-2.opendata.source.coop/agentmorris/lila-wildlife/nacti-unzipped (AWS)
#    https://lilawildlife.blob.core.windows.net/lila-wildlife/nacti-unzipped (Azure)


# this gives us the raw html, from there I might be able to do some regex? 
# so, want to take that webpage, extract the names of datasets to populate the dropdown with
# associate the correct href link with the name
# and probably store the description with them too, for display alongside in a text box