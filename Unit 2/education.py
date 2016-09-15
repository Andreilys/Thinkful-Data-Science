from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#
# print(soup.prettify)
# print(soup.get_text())
#
# for string in soup.stripped_strings:
#     print((string).encode('utf-8'))

def getSoup():
    url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

#getting the clean headedef getHeader(soup):
def getHeader(soup):
    lheader = soup.find_all("tr", class_="lheader")
    lheader_text = lheader[0].get_text()
    lheader_list = lheader_text.split("\n")
    lheader_clean_list = []
    # iterate through the header list to get rid of unicode and empty spaces
    for i in range(len(lheader_list)):
        if len(lheader_list[i]) > 0:
            lheader_clean_list.append(str(lheader_list[i]))
    return lheader_clean_list

def getData(soup, column_names):
    data_tables = soup.find_all("table")
    data_rows = soup.find_all("tr", class_="tcont")
    data_rows_list = []
    # going through the tcont soup text to add to a new clean list
    for i in range(len(data_rows)):
        # this gets each data_row and returns it in a messy format
        data_cell = data_rows[i].find_all("td")
        clean_list = [u"a", u"d", u"c", u"b", u"e", u"f", u"g", u"h" u"\xc2\xa0", u"\xa0", u"\xa0", u""]
        data_list = [value.text for value in data_cell if value.text not in clean_list]
        # turning unicode into integers
        try:
            data_list[1] = int(data_list[1])
            data_list[2] = int(data_list[2])
            data_list[3] = int(data_list[3])
            data_list[4] = int(data_list[4])
            data_rows_list.append(data_list)
        except:
            break
    # get rid of last few rows that aren't necessary to add
    data_rows_list = data_rows_list[0:93]
    df_countries = pd.DataFrame(data_rows_list, columns=column_names)
    return df_countries

def main():
    soup = getSoup()
    column_names = getHeader(soup)
    data_rows = getData(soup, column_names)
    # plt.figure()
    print(data_rows['Total'].mean())
    print(data_rows['Total'].median())
    # plt.show()

main()
# print(soup.contents[0])
#
# for tag in soup.find_all(re.compile("tr")):
#     print(tag)
