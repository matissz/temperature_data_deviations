from apscheduler.schedulers.background import BackgroundScheduler
from current_temp import check_temperature
import time

def main():
        
    scheduler = BackgroundScheduler()    
    scheduler.add_job(check_temperature, 'interval', minutes=1)
    scheduler.start()
    
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    main()
