"""A simple xblock to reveal html on click."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin


class Click2RevealXBlock(StudioEditableXBlockMixin, XBlock):
    """
    A simple xblock to reveal html on click.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    
    
    img1URL=String(display_name="image 1 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@poster-01.png' ,scope=Scope.settings, help="")
    img2URL=String(display_name="image 2 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@poster-02.png',scope=Scope.settings, help="" )
    img3URL=String(display_name="image 3 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@poster-03.png',scope=Scope.settings, help="" )
    img4URL=String(display_name="image 4 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@poster-04.png',scope=Scope.settings, help="" )
    img5URL=String(display_name="image 5 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@line3.png',scope=Scope.settings, help="" )
    img6URL=String(display_name="image 6 URL",default='/asset-v1:edX+DemoX+Demo_Course+type@asset+block@line2.png',scope=Scope.settings, help="" )


    text1= String(display_name="說明文字1",default='有一天，你無意間中走入一間廢棄的電玩店',scope=Scope.settings, help="")
    text2= String(display_name="說明文字2",default='在好奇心驅使之下，將一台電玩插上插座，沒想到卻被捲入遊戲世界中',scope=Scope.settings, help="")

    text3= String(display_name="說明文字3",default='在遊戲世界中，有許多因缺少程式碼而壞掉遊戲',scope=Scope.settings, help="")
    text4= String(display_name="說明文字4",default='你要扮演遊戲世界的英雄，修復遊戲，讓遊戲世界回復過往的繁榮',scope=Scope.settings, help="")

    text5= String(display_name="說明文字5",default='Game',scope=Scope.settings, help="")


    # Make fields editable in studio
    editable_fields = ('img1URL', 'img2URL', 'img3URL', 'img4URL', 'img5URL', 'img6URL', 'text1','text2','text3','text4','text5' )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html_str = self.resource_string("static/html/c2r.html")
        frag = Fragment(html_str.format(self=self))

        # Load the CSS and JavaScript fragments from within the package
        css_str = self.resource_string( "static/css/c2r.css")
        frag.add_css(css_str)

        js_str = self.resource_string( "static/js/src/c2r.js")
        frag.add_javascript(js_str)

        frag.initialize_js('C2RBlock')
        return frag
