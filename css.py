"""

Window{
    background-image: url("Resoures//BackGround (1).png");
    background-repeat: no-repeat;
    }
QLineEdit#e0 {
    font-size: 20px;
    color: #fff;
    background: #EE961D;
    border-radius: 10px;
    }
QLineEdit#e1 {
    font-size: 20px;
    color: #FFF;
    border-radius: 4px;
    background: #EE961D;
    }
QPushButton#b0 {
    background: #EE961D;
    border-radius: 10px;
    background-image : url(Resoures//Send.png);
    background-repeat: no-repeat;
    background-position: center;
    }
QPushButton#b0:hover {
    background: #EE961D;
    border-radius: 10px;
    padding: 4px;
    background-image : url(Resoures//Confirm.png);
    background-repeat: no-repeat;
    background-position: center;
    }
QPushButton#b1 {
    background: #EE961D;
    border-radius: 10px;
    background-image : url(Resoures//Edit_pencil.png);
    background-repeat: no-repeat;
    background-position: center;
    }
QLabel#l0 {
    font-family: 'Inter V Light Italic';
    font-size: 24px;
    font-weight: 400;
    }
QLabel#l1 {
    font-family: 'K2d Light';
    font-size: 24px;
    }
QWidget#content  {
    background-color :  transparent;
    }
QLabel#label {
    font-family: 'K2d Light';
    font-size: 16px;
    background-color:lightblue;
}
QLabel#label1 {
    font-family: 'K2d Light';
    font-size: 16px;
}



"""

scroll_area_css = """
QScrollArea {
    background-color:transparent;
    }
QScrollBar:vertical {
    width: 15px;
    margin: 0px 0px 0px 0px;
    border: none;
    } 

"""

label = """
QLabel {
    background-color:blue;
    border-radius: 10px;
    }
"""

msg_label_notme = """
background-color: lightblue;
font-family: 'K2d Light';
font-size: 16px;
border-radius: 10px;
padding: 4px;
"""

msg_label_me = """
background-color: lightgreen;
font-family: 'K2d Light';
font-size: 16px;
border-radius: 10px;
padding: 4px;
"""