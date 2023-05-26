import random
from pages.article_summary_page import ArticlesSummaryPage, NoneExistText
from test_data.test_data import RandomData, get_data_from_csv
from tests.base_test import BaseTest


class SearchTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.random_data = RandomData()
        self.articles_summary_page = ArticlesSummaryPage(self.home_page.driver)

    def test_TS03TC01_search_existing_article(self):

        self.valid_articles = get_data_from_csv("../test_data/valid_articles.csv")

        for i in range(len(self.valid_articles)):
            searching_article = self.valid_articles[i]
            self.home_page.enter_search_frase(searching_article[0])
            self.home_page.search_button_clic()
            print("szukany artykuł: ", searching_article[0])
            found_articles = self.articles_summary_page.get_articles_list()
            found = False
            if len(found_articles) > 0:
                for j in range(len(found_articles)):
                    if searching_article[0] in found_articles[j].title:
                        found = True
                        break
            self.assertTrue(found)

    def test_TS03TC02_search_none_existing_article(self):
        searching_article = self.random_data.random_text[:25]
        searching_article = searching_article + " tester1234"  # to be sure it wasn't
        self.home_page.enter_search_frase(searching_article)
        self.home_page.search_button_clic()
        print("szukany artykuł: ", searching_article)
        found_articles = self.articles_summary_page.get_articles_list()
        self.assertTrue(len(found_articles) > 0 and NoneExistText in found_articles[0].title)

    def test_TS03TC03_search_with_category(self):
        items = self.home_page.get_category_list()
        selected_category = random.randrange(0, len(items))
        category = items[selected_category].text
        print("wybrana kategoria: ", category)
        self.home_page.select_category_by_index(selected_category)
        self.home_page.search_button_clic()
        found_articles = self.articles_summary_page.get_articles_list()
        if NoneExistText in found_articles[0].title:
            print("brak atrykułów tej kategorii")
            self.assertTrue(True)
        else:
            not_found = True
            for j in range(len(found_articles)):
                if category not in found_articles[j].tags:
                    found = False
                    break
                self.assertTrue(not_found)

    def test_TS03TC04_search_with_implementation(self):
        items = self.home_page.get_implementation_list()
        selected_implementation = random.randrange(0, len(items))
        implementation = items[selected_implementation].text
        print("wybrany sposób implementacji: ", implementation)
        self.home_page.select_implementation_by_index(selected_implementation)
        self.home_page.search_button_clic()
        found_articles = self.articles_summary_page.get_articles_list()
        if NoneExistText in found_articles[0].title:
            print("brak rozwiązań o tej implementacji")
            self.assertTrue(True)
        else:
            not_found = True
            for j in range(len(found_articles)):
                if implementation not in found_articles[j].tags:
                    found = False
                    break
            self.assertTrue(not_found)


