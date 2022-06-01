from abc import ABC, abstractmethod


class AbstractRequestHandler(ABC):
    @abstractmethod
    def request(self):
        pass


class GetRequestHandler(AbstractRequestHandler):
    def request(self):
        print("Sending GET request")


class PostRequestHandler(AbstractRequestHandler):
    def request(self):
        print("Sending POST request")


class LoggerProxy(AbstractRequestHandler):
    def __init__(self, request_handler: AbstractRequestHandler):
        self._request_handler = request_handler

    def request(self):
        print("LOG: Request")
        result = self._request_handler.request()
        print("-" * 20)
        return result


if __name__ == '__main__':
    get_request_handler = GetRequestHandler()
    post_request_handler = PostRequestHandler()

    get_proxy = LoggerProxy(get_request_handler)
    get_proxy.request()

    post_proxy = LoggerProxy(post_request_handler)
    post_proxy.request()
