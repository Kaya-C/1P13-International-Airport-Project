#Luggage coordinates
xL = 0.0
yL = -0.286
zL = 0.2

#Platform coordinates
xP = -0.384
yP = -0.222
zP = 0.338

#OLd Platform - (0.381, 0.0, 0.083)

#Rejection coordinates
xR = -0.0
yR = 0.317
zR = 0.053

arm.home()
for _ in range(4):
    status = scanner.barcode_check()
    table.rotate_table_angel(90)
    time.sleep(1)
    arm.move_arm(xL, yL, zL)
    time.sleep(2)
    arm.control_gripper(45)
    time.sleep(1)
    
    if status == "Platform":
        arm.move_arm(xP, yP, zP)
        bot.activate.stepper_motor()
        time.sleep(2)
        bot.rotate_stepper_cw(5)
        time.sleep(2)
        arm.control_gripper(-45)
        time.sleep(5)
        bot.rotate_stepper_ccw(5)
    else:
        arm.rotate_shoulder(-25)
        arm.move_arm(xR, yR, zR)
    time.sleep(1)
    arm.home()

arm.terminate_arm()