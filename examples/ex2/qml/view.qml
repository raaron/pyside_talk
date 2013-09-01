import QtQuick 1.0

Rectangle {
    id: window
    width: 200; height: 150

    Rectangle {
        id: button
        x: 30; y: 30; width: 150; height: 30
        radius: 8
        border { width: 1; color: "grey" }

        color: {
            if (buttonMouseArea.pressed)
                return "grey"
            else
                return "lightgrey"
        }

        Text {
            id: buttonLabel
            anchors.centerIn: parent
            text: "Hide label"
        }

        MouseArea {
            id: buttonMouseArea
            anchors.fill: parent
            onClicked: counterLabel.visible = false
        }
    }

    Text {
        x: 30; y: 90
        id: counterLabel
        text: "Label to hide..."
    }

}