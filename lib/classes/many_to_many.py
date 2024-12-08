class Article:
    all_articles = []  # Stores all instances of Article

    def __init__(self, author, magazine, title):
        self.author = author  
        self.magazine = magazine  
        self._title = title  #make the title private
        
        Article.all_articles.append(self)  # Add a single article to article array

    @property  
    def title(self):
        return self._title  # Return article's title

class Author:
    def __init__(self, name):
        self._name = name  # keep name privately

    @property
    def name(self):
        return self._name  # Return author name

    def articles(self):
        # Return articles written by an author
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        # Return a list of specific magazines the author has written for ..
        return list({article.magazine for article in Article.all_articles if article.author == self})

    def add_article(self, magazine, title):
        # Allow the author to add an article to a magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return a list of unique topics/categories of magazines the author has written for
        topic_areas = {magazine.category for magazine in self.magazines()}
        return list(topic_areas) if topic_areas else None 
    # Return the topics if they exist, otherwise None

class Magazine:
    def __init__(self, name, category):
        self._name = None  # Initialize the magazine's name privately
        self._category = None  # Initialize the magazine's category privately
        self.name = name  # Set the magazine's name
        self.category = category  # Set the magazine's category

    @property
    def name(self):
        return self._name  # Return the magazine's name

    @name.setter
    def name(self, value):
        # magazine name must be a string
        if not isinstance(value, str):
            raise ValueError("Magazine name must be a string.")
        self._name = value  # Set the magazine's name

    @property
    def category(self):
        return self._category  # Return magazine category

    @category.setter
    def category(self, value):
        # category is an string not not an empty
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if not value:
            raise ValueError("Category cannot be empty.")
        self._category = value 
        # Set the magazine's category

    def articles(self):
        # show all articles published in a single magazine
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        # return a list of unique authors who have contributed to this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Return the titles of all articles published in this magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None  # Return titles if they exist, otherwise None

    def contributing_authors(self):
        # Count no. of authors who have written for the magazine
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        # return authors with more than two articles in a magazine
        return [author for author, count in author_counts.items() if count > 2] or None

# # INSTANCES FOR ALL CLASSES AND ASSOCIATIONS
# Create some magazines
# magazine1 = Magazine("What xmass Is As We Grow Up!", "Ville")
# magazine2 = Magazine("Red Love", "Love")

# # Create an author
# author1 = Author("Charles Dickens")

# # Author adds articles to magazines
# article1 = author1.add_article(magazine1, "The World Today")
# article2 = author1.add_article(magazine2, "Corona Virus")

# # Show the articles the author has written
# print(f"{author1.name}'s Articles: {[article.title for article in author1.articles()]}")

# # Show the magazines the author has contributed to
# print(f"{author1.name}'s Magazines: {[magazine.name for magazine in author1.magazines()]}")

# # Show the topic areas (categories) of the magazines the author has written for
# print(f"{author1.name}'s Topic Areas: {author1.topic_areas()}")

# # Show articles in a specific magazine
# print(f"Articles in {magazine1.name}: {[article.title for article in magazine1.articles()]}")

# # Show contributors to a specific magazine
# print(f"Contributors to {magazine1.name}: {[author.name for author in magazine1.contributors()]}")

# # Show the authors who have contributed more than 2 articles to a magazine
# # In this case, since we only have 2 articles, this will return None
# print(f"Authors who contributed more than 2 articles to {magazine1.name}: {magazine1.contributing_authors()}")
