from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ArticleLocators:
    MAIN_CONTAINER = (By.XPATH, "//div[starts-with(@class, 'view view-articles view-id-articles ')]")
    INSIDE_CONTAINER = (By.XPATH, "div[@class='view-content']")
    INSIDE_EMPTY = (By.XPATH, "//div[@class='view-empty']")
    ARTICLES = (By.XPATH, "div[starts-with(@class, 'views-row')]")
    TITLE = (By.XPATH, "//h3[@class='title']/a[starts-with(@href, 'https')]")
    TAGS = (By.XPATH, "//div[@class='tags margin-top2']")


NoneExistText = "Brak wyników"


class Article:
    def __init__(self):
        self.title = ""
        self.title1 = ""
        self.tags = []


class ArticlesSummaryPage(BasePage):

    def get_articles_list(self):
        articles = []
        container = self.driver.find_element(*ArticleLocators.MAIN_CONTAINER)
        try:
            container_in = container.find_element(*ArticleLocators.INSIDE_CONTAINER)
            # if container_in.eq != None:
            items = container_in.find_elements(*ArticleLocators.ARTICLES)
            if len(items) > 0:
                for i in range(len(items)):
                    article = Article()
                    fullname = items[i].find_element(*ArticleLocators.TITLE)
                    category = fullname.find_element(By.TAG_NAME, "span")
                    article.title = fullname.text.replace(category.text, '').strip()
                    article.title1 = category.text[2:].strip()
                    tags = items[i].find_element(*ArticleLocators.TAGS)
                    tags_elem = tags.find_elements(By.TAG_NAME, "li")
                    for j in range(len(tags_elem)):
                        article.tags.append(tags_elem[j].text.strip)
                    articles.append(article)
        except NoSuchElementException:  # brak listy elementów
            try:
                container.find_element(*ArticleLocators.INSIDE_EMPTY)
                article = Article()
                article.title = NoneExistText
                articles.append(article)
            except NoSuchElementException:
                pass
            pass
        return articles
