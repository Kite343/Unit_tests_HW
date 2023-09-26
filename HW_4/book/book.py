class Book():
    def __init__(self, id, title, author):
        self._id = id
        self._title = title
        self._author = author
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return f'title: {self._title}, author: {self._author}'
    
