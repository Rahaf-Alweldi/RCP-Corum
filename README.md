# Web Scraping Corum Website

This project is designed to extract information about watches from the Corum website. The extracted data includes various details about each watch, such as reference number, price, case material, and other specifications. Then came the data cleaning and saved into a CSV file for further analysis. Additionally, a cron job is set up to run the scraper at regular intervals and log its progress.

## Agenda

1. [Features](#features)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [Project Architecture](#project-architecture)
5. [AWS EC2 Deployment](#aws-ec2-deployment)
6. [Code Explanation](#code-explanation)
7. [Setting Up Cron Job](#setting-up-cron-job)
8. [Data Analysis](#data-analysis)

---
<br></br>
## Features

- Scraping target <a href="https://www.corum-watches.com/" target="_blank">Corum</a> website.
- Scrapes data from multiple collections of watches on the Corum website.
- Data cleaning to ensure the integrity and usability of the extracted data.
- Cron job setup to automate the scraping process at regular intervals.
- Extracts detailed information for each watch, including:

| Field Label | Description of Field |
|----------|----------|
| reference_number | This is the most unique identifier of a watch. |
| watch_URL | The link to the watch. |
| type | This can be Men’s Watches, Women’s Watches, Unisex Watches, or Pocket Watches. |
| brand | The name of the watch brand. |
| year_introduced | The year the watch was introduced. |
| parent_model | This is the collection or family of the watch. |
| specific_model | An individual watch within the parent model category. |
| nickname | An informal or colloquial name given to a specific watch model. |
| marketing_name | Most watches won’t have these, but some will. It’s a special title like “2024 Olympics” or “Red Bull Edition” that’s unique to a limited edition watch, OR a name given to a watch by collectors. |
| style | Potential values are: Dive, Chronograph, Military / Field, GMT, Dress, Atomic Radio Controlled, GPS, Smartwatch, Pilot, Skeleton, Racing / Driving, Sport, Digital. |
| currency | Standardization of money in USD. |
| price | Price of the watch in Dollars. |
| image_URL | A direct link to the image file of the watch. |
| made_in | Where the brand’s watches are made. |
| case_shape | Examples: Round, Rectangular, Tonneau, Oval, Irregular...etc. |
| case_material | Materials used for watch cases. |
| case_finish | The way the surfaces are polished. Possible values are: Brushed, Polished, Sandblasted, Satin, Microblasted, Matte, Frosted. |
| caseback | It could also be listed as open caseback, exhibition caseback, solid caseback, closed caseback. |
| diameter | Round cases are sized by measuring the diameter across the case. |
| between_lugs | This is often called strap width or bracelet with - it’s the distance between two lugs on the same side of the watch where the strap hooks in. |
| lug_to_lug | It’s the distance from the tip of one lug to the tip of a lug on the other side of the watch. |
| case_thickness | This is how thick a watch case is if you look at it from the side. |
| bezel_material | This is the ring around the watch dial. |
| bezel_color | Color of the outer ring around the watch. |
| crystal | This is the piece in front of the watch dial that protects it. |
| water_resistance | A measure of how well a watch can handle being exposed to water. Will be labeled as meters, M, ATM, or Bar. |
| weight | Weight of the watch. The material used will affect how heavy a watch feels. (labeled as g). |
| dial_color | The color of the face or background of the watch where the time is displayed. |
| numerals | Might be something like Arabic numerals, Roman numerals, baton indexes, stick / dot, diamond indexes, gem-set indexes, etc. |
| bracelet_material | The material used to construct the wristband or strap of the watch. For example Alligator leather, Calfskin, stainless steel, etc. |
| bracelet_color | The color of the wristband or strap that holds the timepiece. |
| clasp_type | Sometimes called clasp, buckle, or closure. We're looking for a value like Folding clasp, Pin buckle, NATO strap, velcro, non-closure, etc. |
| movement | Refers to the internal mechanism that drives the watch and powers its timekeeping functions. |
| caliber | The specific design or model of its movement, which is the internal mechanism responsible for keeping time and driving the watch's functions. |
| power_reserve | This is a measure of the energy stored in the watch's mainspring, which drives the movement of the watch. |
| frequency | It's how quickly a watch ticks. |
| jewels | Jewels are rubies or other jewels inside a watch's movement that help it move more smoothly. |
| features | Might be called features, functions, or complications. We're looking for a complete list of functions or features that a watch has. |
| description | Will be the paragraph or two main product description. |

---
<br></br>
## Requirements

- Python 3
- `requests`
- `BeautifulSoup4`
- `pandas`

---
<br></br>
## Project Structure

- :file_folder: data:
  - `Corum_timestamp.csv`: The initial data collected directly from the Corum website.
  - `Cleaned_data.csv`: Contains the data after it has been cleaned and processed.
- :file_folder: src:
  - `scrape.py`: Script for scraping data from the Corum website.
  - `processing.py`: Script for cleaning the scraped data.
  - `Cron_job.py`: Script to retrieves the current timestamp, and appends it into a log file `Cron_job.log` to track the progress of the cronjob.
  - `run.py`: Script to list the required python files to be executed.
- :file_folder: venv: A virtual environment to store our libraries.
- `init.sh`: Automate the setup process to create a virtual environment in the `venv` directory, activate it, and install all necessary dependencies listed in `requirements.txt`.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

---
<br></br>
## Project Architecture

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/5332dafd-542c-47e3-8a3f-e0713bda7f6c)

1. Data Collection
  - Collects URLs of individual watches from the Corum collections pages.
  - Scrapes detailed information for each watch.
  - Saves the raw data into a CSV file.
2. Data Cleaning
  - Drop the empty columns.
  - Change currency from CHF to USD.
  - Clean the description column from any extra HTML tags.
3. Task Automation
4. Data Analysis

---
<br></br>
## AWS EC2 Deployment

1. Launch an EC2 instance on Amazon Web Services (AWS).
2. Connecting VSCode to EC2 Instance.
3. Install dependencies on EC2 by running `init.sh` in the terminal.

---
<br></br>
## Code Explanation

1. **Collect URLs:** Scrapes the URLs of individual watches from the collections pages.
2. **Scrape Data:** For each watch URL, scrape various details about the watch.
3. **Save Data:** Converts the data dictionary into a pandas DataFrame and saves it to a CSV file.
4. **Data Cleaning:** The `processing.py` script processes the raw data to ensure consistency and correctness.
5. **Cronjob:** Script to create a log file used in tracking cronjob progress.
6. **Data Analysis:** External notebook performed the data analysis.

---
<br></br>
## Setting Up Cron Job

1. Make the scripts executable.
```
chmod +x scrape.py
```
```
chmod +x processing.py
```
```
chmod +x Cron_job.py
```
```
chmod +x run.py
```
2. Edit the crontab.
```
crontab -e
```
3. Add the following line to schedule the scraper to run every 5 minutes.
```
*/5 * * * * python3 /home/ubuntu/RCP-Corum/src/run.py
```

---
<br></br>
## Data Analysis

1. Total number of watches by collection

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/c471ec95-5034-4f42-8c50-cd9d204b2488)

2. Average price by collection

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/8674f55b-3482-4707-b0ef-30d9f769e5c8)

3. Most expensive watches

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/933c9d34-7b03-4087-b548-05cc3f038b29)

4. Watch color segmentation

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/b0e84a51-dd2d-40ab-bbe6-13cd5b875dbf)
