import schedule
import time
from main import main
from log_config import logging

def schedule_tasks():

    scheduling_choice = input("Would you like to schedule the scrapping process? (y/n): ").strip().lower()
        
    if scheduling_choice not in ['y', 'n']:
        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

    if scheduling_choice.lower() == 'y':
        # Schedule scrape_data to run daily at 2 AM
        schedule.every().monday.at("09:00").do(main)
        logging.info("Scrapping process scheduled to run every Monday at 9:00 AM.")
        print("Scraping process scheduled successfully.")
    else:
        print("No scheduling set.")

def start_scheduler():

    schedule_tasks()
    print("Scheduler is running. Press Ctrl+C to stop.")
    
    try:
        while True:
            schedule.run_pending()  
            time.sleep(1)  

    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
        print("Scheduler stopped.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"Failed to schedule. Check logs for details.")
        
if __name__ == "__main__":
    start_scheduler()