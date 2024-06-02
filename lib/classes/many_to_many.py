class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class")



class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.author is  self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author is self})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author is self}
        return list(categories) if categories else None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        authors = {article.author for article in self.articles() if isinstance(article.author, Author)}
        return list(authors) if authors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        qualified_authors = [author for author in authors if authors.count(author) > 2]
        return qualified_authors if qualified_authors else None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(2, 17):
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
