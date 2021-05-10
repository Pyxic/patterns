from abc import ABC, abstractmethod


class Page(ABC):

    def __init__(self, renderer):
        self._renderer = renderer

    def change_render(self, renderer):
        self._renderer = renderer

    @abstractmethod
    def view(self):
        pass


class SimplePage(Page):

    def __init__(self, renderer, title, content):
        super().__init__(renderer)
        self._title = title
        self._content = content

    def view(self):
        return self._renderer.render_parts([
            self._renderer.render_header(),
            self._renderer.render_title(self._title),
            self._renderer.render_text_block(self._content),
            self._renderer.render_footer()
        ])


class ProductPage(Page):

    def __init__(self, renderer, product):
        super().__init__(renderer)
        self._product = product

    def view(self):
        return self._renderer.render_parts([
            self._renderer.render_header(),
            self._renderer.render_title(self._product.title),
            self._renderer.render_text_block(self._product.description),
            self._renderer.render_image(self._product.image),
            self._renderer.render_link("/cart/add/" + self._product.id, "Add to cart"),
            self._renderer.render_footer()
        ])


class Product:

    def __init__(self, id, title, description, image, price):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__image = image
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def image(self):
        return self.__image

    @property
    def price(self):
        return self.__price


class Renderer(ABC):

    def render_title(self, title):
        pass

    def render_text_block(self, text):
        pass

    def render_image(self, url):
        pass

    def render_link(self, url, title):
        pass

    def render_header(self):
        pass

    def render_footer(self):
        pass

    def render_parts(self, parts: list):
        pass


class HTMLRenderer(Renderer):

    def render_title(self, title):
        return f"<h1>{title}</h1>"

    def render_text_block(self, text):
        return f"<div>{text}</div>"

    def render_image(self, url):
        return f"<img src='{url}'>"

    def render_link(self, url, title):
        return f"<a href='{url}'>{title}</a>"

    def render_header(self):
        return "<html><body>"

    def render_footer(self):
        return "</body></html>"

    def render_parts(self, parts: list):
        return "\n".join(parts)


html_renderer = HTMLRenderer()
page = SimplePage(html_renderer, 'Main', "welcome to web-site")
print(page.view())

product = Product('123', 'hat', "red hat with ...", "img/red_hat.jpeg", 450)
page = ProductPage(html_renderer, product)
print(page.view())
