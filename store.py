class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body


posts = []


class PostStore:

    def get_all(self):
        return posts

    def add(self, post):
        posts.append(post)

    def get_by_id(self, id):

        for post in posts:
            if post.id == id:
                return post
        return None


    def update(self, id, fields):

        post = self.get_by_id(id)
        post.name = fields['name']
        post.photo_url = fields['photo_url']
        post.body = fields['body']

    def delete(self, id):
        post = self.get_by_id(id)
        posts.remove(post)
