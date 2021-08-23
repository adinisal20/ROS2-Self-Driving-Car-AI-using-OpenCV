import cv2
from numpy import interp
import numpy as np

from .config import config
from .Detection.Lanes.Lane_Detection import detect_Lane
from .Detection.Signs.SignDetectionApi import detect_Signs
# from .Detection.Signs.a_Localization.TLD import detect_TrafficLight
from .Detection.Signs.a_Localization.ObjDet_cascade_classified import detect_TrafficLights
from .Control.special import Drive_Car
from .Control.Control_TrafficL_Nd_LeftTurn import Control

from geometry_msgs.msg import Twist
from rclpy.node import Node 
from cv_bridge import CvBridge 
from sensor_msgs.msg import Image 
import rclpy 


control = Control() 
class Video_feed_in(Node):
    def __init__(self):

        super().__init__('video_subscriber')
        self.subscriber = self.create_subscription(Image,'/camera/image_raw',self.process_data,10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 40)
        timer_period = 0.5;self.timer = self.create_timer(timer_period, self.send_cmd_vel)

        self.velocity=Twist()
        self.bridge = CvBridge() # converting ros images to opencv data
        


    def send_cmd_vel(self):
        self.publisher.publish(self.velocity)
        
    def process_data(self, data): 
        
        frame = self.bridge.imgmsg_to_cv2(data,'bgr8') # performing conversion
        img = frame[0:640,238:1042] 
        img = cv2.resize(img,(320,240))
        img_orig = img.copy()
        #Traffic_State = detect_TrafficLight(img,frame_draw)
        Traffic_State, CloseProximity = detect_TrafficLights(img_orig.copy())

        distance, Curvature = detect_Lane(img)
        Mode , Tracked_class = detect_Signs(img_orig,img)

        distance,Curvature = control.Obey_LeftTurn(distance,Curvature,Mode,Tracked_class)

        Current_State = [distance, Curvature , img , Mode , Tracked_class]
        a,b = Drive_Car(Current_State)

        a=interp(a,[30,120],[0.5,-0.5])
        b=interp(b,[50,90],[1,2])
        print("\n\nA = ",a,"   B = ", b,"\n\n")

        a,b = control.OBEY_TrafficLights(a,b,Traffic_State,CloseProximity)
        print("After Obeying TrafficLights")
        print("\n\nA = ",a,"   B = ", b,"\n\n")

        self.velocity.linear.x = b        
        self.velocity.angular.z = a

        cv2.putText(img,Traffic_State,(20,60),cv2.FONT_HERSHEY_COMPLEX,0.5,255)
        cv2.putText(img,"Angle = "+str(np.round(a,3))+" , Speed = " + str(np.round(b,3)) ,(20,80),cv2.FONT_HERSHEY_COMPLEX,0.5,255)

        cv2.imshow("Frame",img)
        cv2.waitKey(1)
        
 
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = Video_feed_in()
  rclpy.spin(image_subscriber)
  rclpy.shutdown()

if __name__ == '__main__':
	main()