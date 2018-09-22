#https://www.quora.com/How-can-I-send-a-push-notification-to-my-Android-phone-with-a-Python-script
#pip install notify-run 
#notify-run register 
#go to the url given if the QR code given cannot be seen properly


from notify_run import Notify
import datetime

def alert_many_users(user_num):
  #user_num += 1
  notify = Notify()
  notify.send("ALERT: Number of users exceeded "+str(user_num)+" !")

#alert_many_users(100)