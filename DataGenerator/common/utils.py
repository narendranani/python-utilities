import wx


def set_default_font_style(self, elements=[]):
    for element in elements:
        element.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))


def resize_images(image, width, height):
    image = wx.Image(image)
    image.Rescale(width, height)
    return image