# **FDA Drug Information Scraper**
This project is an FDA Drug Information Scraper that extracts detailed drug information from the [FDA Website](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=020892) and stores the data in MongoDB. The scraper captures essential details about drugs and metadata, offering traceability and optional automation for periodic scraping.

## **Features**

**Drug Data Extraction:**
- Captures detailed drug information including:
Drug Name, Active Ingredients, Strength, Dosage Form/Route, Marketing Status, TE Code, RLD, and RS.

**Metadata Collection:**
- Stores metadata for full traceability, including:
  - Timestamp of data extraction
  - Source URL
  - Number of records extracted

**MongoDB Integration:**
- Saves scraped data and metadata into MongoDB in a well-organized structure for easy querying.

**Error Handling and Logging:**
- Implements retry mechanisms for handling network or structural issues.
- Logs the scraping process, errors, and database interactions in a dedicated log file.

**File Downloads:**
- Optionally downloads associated documents (e.g., drug labels and letters) as PDFs into a local directory.

**Scheduling:**
- Automates the scraping process using a scheduler.

## **Project Structure**
```
Web_Scrapper/
├── lib/                  # Core project logic
│   ├── main.py           # Orchestrates scraping tasks
│   ├── scraper.py        # Handles scraping logic
│   ├── database.py       # Manages MongoDB interactions
│   ├── scheduler.py      # Scheduling logic
│   ├── log_config.py     # Logging configuration
├── logs/                 # Log files
│   └── application.log   # Logs for debugging and monitoring
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── venv/                 # Virtual environment
```

## **Prerequisites**
Ensure the following tools are installed:

1. Python: Version 3.8 or above.
2. MongoDB: Installed locally or accessible via MongoDB Atlas.

## **Running the Project**

**1. Set Up the Virtual Environment**<br>
Activate the environment:

bash
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

**2. Install Dependencies**<br>
Install the required libraries:

bash
```
pip install -r requirements.txt
```

**3. Configure Environment Variables**<br>
Create a .env file in the root directory with the following:
```
MONGO_URI=your_mongodb_connection_string
```

**4. Run the Scraper**<br>
Start the scraping process:

bash
```
python lib/main.py
```

**5. Enable Scheduling**<br>
To schedule periodic scraping tasks:

bash
```
python lib/scheduler.py
```

## **Usage**

**Run Scraper:**
- Automatically extracts data and stores it in MongoDB.

**Schedule Tasks:**
- Periodically scrape data using the scheduler.

**Download Files:**
- Enable optional PDF downloads when prompted.
