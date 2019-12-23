from .database import Database

class BlogPost(Database):
    def getAllPosts(self):
        return self.select("SELECT * FROM blog_post WHERE active = 1")
    def getPost(self, id):
        return self.select("SELECT * FROM blog_post WHERE `id` = %s", (id,))
    def createPost(self, title, text):
        query = "INSERT INTO blog_post (title, text) VALUES (%s, %s)"
        values = (title, text)
        self.insert(query, values)
    def togglePost(self, id, value):
        query = "UPDATE blog_post SET active = %s WHERE `id` = %s"
        values = (value, id)
        self.insert(query, values)
        
