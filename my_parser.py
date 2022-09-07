from http.client import HTTPResponse
from bs4 import BeautifulSoup, Tag, ResultSet
from urllib.request import urlopen
from file_manager import FileManager


class Parser:
    DOMAIN: str = "https://www.hyperia.sk/"
    JOBS_PATH: str = "kariera/"

    def __init__(self):
        self.file_manager: FileManager = FileManager()

    def find_jobs(self) -> None:
        """Finds all job offers on the site,
        gains more information by opening url in href at each job offer,
        saves data to json file.
        """
        soup: BeautifulSoup = self.__open_path(self.JOBS_PATH)
        positions_section: Tag = soup.find(id='positions')
        positions_div: Tag = positions_section.find('div', class_='row')
        positions: ResultSet = positions_div.find_all('div', class_='offset-lg-1')
        for pos_div in positions:
            info_path: str = pos_div.a['href']
            info_soup: BeautifulSoup = self.__open_path(info_path)
            title, locality, salary, contract_type = self.__find_info(info_soup)
            contact: str = self.__find_contact(info_soup)
            dictionary: dict = {
                "title": title,
                "locality": locality,
                "salary": salary,
                "contract_type": contract_type,
                "contact": contact
            }
            self.file_manager.write_file(dictionary)

    def __open_path(self, path: str) -> BeautifulSoup:
        """opens a certain path within the website"""
        page: HTTPResponse = urlopen(self.DOMAIN + path)
        content: str = page.read().decode('utf-8')
        soup: BeautifulSoup = BeautifulSoup(content, "lxml")
        return soup

    def __find_info(self, soup: BeautifulSoup) -> [str, str, str]:
        """finds title, location, salary and contract type information"""
        section: Tag = soup.find(class_='position-hero')
        title: str = section.h1.text
        info_div: Tag = section.find('div', class_='row')
        locality, salary, contract_type = (div.p.contents[-1].text for div in info_div.find_all('div'))
        if '€' not in salary:      # if there is additional info after salary, step back
            salary: str = info_div.find_all('div')[1].p.contents[-3].text
        return title, locality, salary, contract_type

    def __find_contact(self, soup: BeautifulSoup) -> str:
        """Finds contact mail separately, because it is in another section"""
        contact_div: Tag = soup.find('div', class_='position-contact')
        contact: str = contact_div.p.strong.text
        return contact
