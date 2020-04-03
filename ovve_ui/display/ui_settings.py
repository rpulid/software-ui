from typing import Tuple, Optional

from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TextSetting:
    def __init__(self, fontName: str, fontSize: int, bold: bool):
        if bold:
            self.font = QFont(fontName, fontSize, QFont.Bold)

        else:
            self.font = QFont(fontName, fontSize)


#TODO: Abstract text placement
class FancyButtonSettings:
    def __init__(self,
                 labelSetting: TextSetting = TextSetting("Arial", 12, True),
                 valueSetting: TextSetting = TextSetting("Arial Black", 36, True),
                 unitSetting: TextSetting = TextSetting("Arial", 10, False),
                 fillColor: str ='#f2fff0',
                 borderColor: str = '#c5c5c5',
                 labelColor: str ='#A7A9AA',
                 valueColor: str = '#000000',
                 unitColor: str = '#808080',
                 default_size: Tuple[int, int] = (150, 80)):

        self.labelFont = labelSetting.font
        self.valueFont = valueSetting.font
        self.unitFont = unitSetting.font
        self.fillColor = fillColor
        self.borderColor = borderColor
        self.labelColor = labelColor
        self.valueColor = valueColor
        self.unitColor = unitColor
        self.default_size = default_size

    def getFillBrush(self) -> QBrush:
        return QBrush(QColor(self.fillColor))

    def getBorderPen(self) -> QPen:
        return QPen(QColor(self.borderColor), 1, Qt.SolidLine)

    def getLabelPen(self) -> QPen:
        return QPen(QColor(self.labelColor))

    def getValuePen(self) -> QPen:
        return QPen(QColor(self.valueColor))

    def getUnitPen(self) -> QPen:
        return QPen(QColor(self.unitColor))

class SimpleButtonSettings:
    def __init__(self,
                 valueSetting: TextSetting = TextSetting("Arial Black", 24, False),
                 fillColor: str = '#f2fff0',
                 borderColor: str = '#C5C5C5',
                 valueColor: str = '#000000',
                 default_size: Tuple[int, int] = (115, 65)):

        self.valueFont = valueSetting.font
        self.borderColor = borderColor
        self.fillColor = fillColor
        self.valueColor = valueColor
        self.default_size = default_size

    def getFillBrush(self) -> QBrush:
        return QBrush(QColor(self.fillColor))

    def getBorderPen(self) -> QPen:
        return QPen(QColor(self.borderColor), 1, Qt.SolidLine)

    def getValuePen(self) -> QPen:
        return QPen(QColor(self.valueColor))

class DisplayRectSettings:
    def __init__(self,
                 labelSetting: TextSetting = TextSetting("Arial", 24, True),
                 valueSetting: TextSetting = TextSetting("Arial Black", 52, True),
                 unitSetting: TextSetting = TextSetting("Arial", 18, False),
                 fillColor: str = '#ECFAFF',
                 borderColor: str = '#C5C5C5',
                 labelColor: str = '#29ABE2',
                 valueColor: str = '#000000',
                 unitColor: str = '#7394A0',
                 default_size: Tuple[int, int] = (150, 80)):
        self.labelFont = labelSetting.font
        self.valueFont = valueSetting.font
        self.unitFont = unitSetting.font
        self.fillColor = fillColor
        self.borderColor = borderColor
        self.labelColor = labelColor
        self.valueColor = valueColor
        self.unitColor = unitColor
        self.default_size = default_size

    def getFillBrush(self) -> QBrush:
        return QBrush(QColor(self.fillColor))

    def getBorderPen(self) -> QPen:
        return QPen(QColor(self.borderColor), 1, Qt.SolidLine)

    def getLabelPen(self) -> QPen:
        return QPen(QColor(self.labelColor))

    def getValuePen(self) -> QPen:
        return QPen(QColor(self.valueColor))

    def getUnitPen(self) -> QPen:
        return QPen(QColor(self.unitColor))

class PageSettings:
    def __init__(self,
                 mainLabelSetting: TextSetting = TextSetting("Arial", 40, True),
                 valueSetting: TextSetting = TextSetting("Arial Black", 128, True),
                 unitSetting: TextSetting = TextSetting("Arial", 40, False),
                 unitColor: str = '#C5C5C5',
                 cancelSetting: TextSetting = TextSetting("Arial", 18, False),
                 cancelColor: str = "#ff0000",
                 commitSetting: TextSetting = TextSetting("Arial", 18, False),
                 commitColor: str = "#00FF00",
                 changeButtonTextSetting: TextSetting = TextSetting("Arial", 40, True),
                 changeButtonValueColor: str = '#C5C5C5',
                 changeButtonBorderColor: str = '#C5C5C5'):

        self.mainLabelFont = mainLabelSetting.font
        self.valueFont = valueSetting.font
        self.unitFont = unitSetting.font
        self.unitColor = unitColor
        self.cancelFont = cancelSetting.font
        self.cancelColor = cancelColor
        self.commitFont = commitSetting.font
        self.commitColor = commitColor
        self.changeButtonTextSetting = changeButtonTextSetting
        self.changeButtonValueColor = changeButtonValueColor
        self.changeButtonBorderColor = changeButtonBorderColor

        def getCancelBorderPen(self) -> QPen:
            return QPen(QColor(self.cancelColor))

        def getCommitBorderPen(self) -> QPen:
            return QPen(QColor(self.commitColor))

        def getChangeBorderPen(self) -> QPen:
            return QPen(QColor(self.changeButtonColor))

class UISettings:
    def __init__(self,
                 fancy_button_settings: FancyButtonSettings = FancyButtonSettings(),
                 simple_button_settings: SimpleButtonSettings = SimpleButtonSettings(),
                 display_rect_settings: DisplayRectSettings = DisplayRectSettings(),
                 page_settings: PageSettings = PageSettings()):

        self.fancy_button_settings = fancy_button_settings
        self.simple_button_settings = simple_button_settings
        self.display_rect_settings = display_rect_settings
        self.page_settings = page_settings

    def set_fancy_button_settings(
            self, new_settings: FancyButtonSettings) -> None:
        self.fancy_button_settings = new_settings

    def set_simple_button_settings(
            self, new_settings: SimpleButtonSettings) -> None:
        self.simple_button_settings = new_settings

    def set_display_rect_settings(
            self, new_settings: DisplayRectSettings) -> None:
        self.display_rect_settings = new_settings

    def set_page_settings(
            self, new_settings: PageSettings) -> None:
        self.page_settings = new_settings
