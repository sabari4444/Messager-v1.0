"/* VERTICAL SCROLLBAR */\n"

""" QScrollBar:vertical {
    border: none;
   background: rgb(45, 45, 68);\n"
    width: 14px;\n"
   margin: 15px 0 15px 0;\n"
   border-radius: 0px;\n"
 }\n"
\n"
/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {    
    background-color: rgb(80, 80, 122);\n"
    min-height: 30px;\n"
    border-radius: 7px;\n"
}\n"
QScrollBar::handle:vertical:hover{    \n"
    background-color: rgb(255, 0, 127);\n"
}\n"
QScrollBar::handle:vertical:pressed {    \n"
    background-color: rgb(185, 0, 92);\n"
}\n"
\n"
/* BTN TOP - SCROLLBAR */\n"
QScrollBar::sub-line:vertical {\n"
    border: none;\n"
   background-color: rgb(59, 59, 90);\n"
   height: 105px;\n"
    border-top-left-radius: 7px;\n"
    border-top-right-radius: 7px;\n"
    subcontrol-position: top;\n"
    subcontrol-origin: margin;\n"
}\n"
QScrollBar::sub-line:vertical:hover {    \n"
   background-color: rgb(255, 0, 127);\n"
}\n"
ScrollBar::sub-line:vertical:pressed {    \n"
    background-color: rgb(185, 0, 92);\n"
}\n"
\n"
/* BTN BOTTOM - SCROLLBAR */\n"
QScrollBar::add-line:vertical {\n"
   border: none;\n"
    background-color: rgb(59, 59, 90);\n"
    height: 105px;\n"
    border-bottom-left-radius: 7px;\n"
    border-bottom-right-radius: 7px;\n"
    subcontrol-position: bottom;\n"
    subcontrol-origin: margin;\n"
\n"
QScrollBar::add-line:vertical:hover {    \n"
    background-color: rgb(255, 0, 127);\n"
}\n"
QScrollBar::add-line:vertical:pressed {    \n"
    background-color: rgb(185, 0, 92);\n"
}\n"
\n"
/* RESET ARROW */\n"
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
   background: none;\n"
}\n"
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
   background: none;\n"
}\n"

/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
QScrollBar:horizontal {
    border: none;
    background-color: rgb(59, 59, 90);
    height: 150px;
    subcontrol-position: bottom;
    
}
QScrollBar::handle:horizontal {\n"
   \n"
}
QScrollBar::add-line:horizontal {"
    
}
QScrollBar::sub-line:horizontal {
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{
    }
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal"""