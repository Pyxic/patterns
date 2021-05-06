from abc import abstractmethod, ABC


class Builder(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_title(self, value: str):
        pass

    @abstractmethod
    def set_body(self, value: str):
        pass

    @abstractmethod
    def set_categories(self, values: list):
        pass

    @abstractmethod
    def set_tags(self, values: list):
        pass

    @property
    @abstractmethod
    def blog_post(self):
        pass


class BlogPostBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._blog_post = BlogPost()

    def set_title(self, value: str):
        self._blog_post.title = value

    def set_body(self, value: str):
        self._blog_post.body = value

    def set_categories(self, values: list):
        self._blog_post.categories = values

    def set_tags(self, values: list):
        self._blog_post.tags = values

    @property
    def blog_post(self):
        result = self._blog_post
        self._blog_post = BlogPost()
        return result


class BlogPost:

    def __init__(self):
        self.title = ''
        self.body = ''
        self.categories = []
        self.tags = []

    def show_blog(self):
        print(f"{self.title}\n {self.body} \n\n categories: {', '.join(self.categories)}"
              f", tags: {', '.join(self.tags)}")


class BlogPostManager:
    """aka director"""

    def __init__(self, blog_post_builder: Builder):
        self.blog_post_builder = blog_post_builder

    def create_clean_post(self):
        return self.blog_post_builder.blog_post

    def create_post_it(self):
        self.blog_post_builder.set_title("post about IT")
        self.blog_post_builder.set_body("new post abut IT ...")
        self.blog_post_builder.set_categories(['IT'])
        self.blog_post_builder.set_tags(['tag_it', 'programming'])
        return self.blog_post_builder.blog_post

    def create_post_hobbies(self):
        self.blog_post_builder.set_title("post about hobbies")
        self.blog_post_builder.set_categories(['hobby'])
        self.blog_post_builder.set_tags(['hobby', 'entertainment'])
        return self.blog_post_builder.blog_post


builder = BlogPostBuilder()
manager = BlogPostManager(builder)
post1 = manager.create_clean_post()
post2 = manager.create_post_hobbies()
post3 = manager.create_post_it()

print("post1")
post1.show_blog()
print("post2")
post2.show_blog()
print("post3")
post3.show_blog()


print("\ncustom post\n")
builder.set_title('custom post')
builder.set_body('custom post ...')
custom_post = builder.blog_post
custom_post.show_blog()

