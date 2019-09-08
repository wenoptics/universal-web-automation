from cefpython3 import cefpython as cef


def main():
    cef.Initialize()
    browser = cef.CreateBrowserSync(
        url="http://www.html-kit.com/tools/cookietester/",
        window_title="Network cookies")
    browser.SetClientHandler(RequestHandler())
    cef.MessageLoop()
    del browser
    cef.Shutdown()


class RequestHandler:

    def OnBeforeResourceLoad(self, browser: cef.PyBrowser, frame: cef.PyFrame, request: cef.PyRequest) -> bool:
        """
        Called on the IO thread before a resource request is loaded. The |request| object may be modified. To cancel the
         request return true otherwise return false.
        :param browser:
        :param frame:
        :param request:
        :return:
        """

        print(f'[OnBeforeResourceLoad] {request.GetMethod()} - {request.GetUrl()}')

        cancel = False
        return cancel


if __name__ == '__main__':
    main()
