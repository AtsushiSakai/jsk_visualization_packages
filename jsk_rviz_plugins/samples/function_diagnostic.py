#!/usr/bin/env python


import roslib
roslib.load_manifest('diagnostic_updater')
import rospy
import diagnostic_updater
import diagnostic_msgs

temperature = 0

def check_temprature(stat):

    #$B%(%i!<H=Dj(B
    if temperature < 10:
        stat.summary(diagnostic_msgs.msg.DiagnosticStatus.OK, "Temperature OK")
    else:
        stat.summary(diagnostic_msgs.msg.DiagnosticStatus.WARN, "Too high")

    #$B%(%i!<>pJs$rDI2C(B
    stat.add("Top-Side Margin", 10 - temperature)
    return stat


if __name__=='__main__':
    rospy.init_node("diagnostic_updater_example2")

    # Updater$B$N%*%V%8%'%/%H$r:n@.(B
    updater = diagnostic_updater.Updater()

    # $B%O!<%I%&%'%"(BID$B$r@_Dj(B
    updater.setHardwareID("Sensor1")

    # $B%O!<%I%(%i!<%A%'%C%/5!G=$NDI2C(B
    updater.add("upper-temperature",check_temprature)

    while not rospy.is_shutdown():
        
        temperature+=0.1
        if temperature>=20:
            temperature=0

        print temperature

        #Topic publish
        updater.update()
        rospy.sleep(0.1)
