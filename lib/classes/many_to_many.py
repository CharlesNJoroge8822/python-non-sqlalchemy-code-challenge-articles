class Article:
    # This class represents an article written by an author for a magazine.

    all = []  # A list to store all articles created.

    def __init__(self, author, magazine, title):
        self.author = author 
        self.magazine = magazine  
        self.title = title  
        Article.all.append(self) 

    @property
    def title(self):
        # Get the title of the article.
        return self._title
    
    @title.setter
    
    def title(self, myTitle):
        # Set the title if it hasn't been set yet, is a string, and its length is between 5 and 50 characters.
        if (not hasattr(self, 'Title')) and isinstance(myTitle, str) and (5 <= len(myTitle) <= 50):
            self._title = myTitle

    @property
    def author(self):
        # Get the author of the article.
        return self._author

    @author.setter
    def author(self, my_author):
        # Set the author if it's an instance of the Author class.
        if isinstance(my_author, Author):
            self._author = my_author

    @property
    def magazine(self):
        # Get the magazine where the article is published.
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_params):
        # Set the magazine if it's an instance of the Magazine class.
        if isinstance(magazine_params, Magazine):
            self._magazine = magazine_params


class Author:
    # This class represents an author who writes articles.

    def __init__(self, name):
        self.name = name  # The name of the author.

    @property
    def name(self):
        # Get the name of the author.
        return self._name

    @name.setter
    def name(self, my_name):
        # Set the name if it hasn't been set yet, is a string, and is not empty.
        if (not hasattr(self, 'name')) and isinstance(my_name, str) and (len(my_name) > 0):
            self._name = my_name

    def articles(self):
        # Get all articles written by this author.
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        # Get all magazines this author has written for (unique list).
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Add a new article written by this author to a specific magazine.
        return Article(self, magazine, title)

    def topic_areas(self):
        # Get a list of categories (topic areas) of the magazines the author has written for.
        if len(self.articles()) == 0:
            return None  # If the author has no articles, return None.
        else:
            return [magazine.category for magazine in self.magazines()]

class Magazine:
    # This class represents a magazine that publishes articles.

    def __init__(self, name, category):
        self.name = name  # The name of the magazine.
        self.category = category  # The category (or topic) of the magazine.

    @property
    def name(self):
        # Get the name of the magazine.
        return self._name
    
    @name.setter
    def name(self, myName):
        # Set the name if it's a string and its length is between 2 and 16 characters.
        if isinstance(myName, str) and (2 <= len(myName) <= 16):
            self._name = myName

    @property
    def category(self):
        # Get the category of the magazine.
        return self._category
    
    @category.setter
    def category(self, my_category):
        # Set the category if it's a string and not empty.
        if isinstance(my_category, str) and (len(my_category) > 0):
            self._category = my_category

    def articles(self):
        # Get all articles published in this magazine.
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        # Get all unique authors who have contributed to this magazine.
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # Get a list of titles of all articles in this magazine.
        if len(self.articles()) == 0:
            return None  # If no articles, return None.
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Get a list of authors who have contributed more than 2 articles to this magazine.
        contributingAuthors = [
            author for author in self.contributors()
            if len([article for article in author.articles() if article.magazine is self]) > 2
        ]
        if len(contributingAuthors) == 0:
            return None  # If no such authors, return None.
        else:
            return contributingAuthors

