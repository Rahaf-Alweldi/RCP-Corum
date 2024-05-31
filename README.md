# Web Scraping Corum Website

This project is designed to extract information about watches from the Corum website. The extracted data includes various details about each watch, such as reference number, price, case material, and other specifications. Then came the data cleaning and saved into a CSV file for further analysis. Additionally, a cron job is set up to run the scraper at regular intervals and log its progress.

## Agenda

1. [Features](#features)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [Project Architecture](#project-architecture)
5. [Usage](#usage)
6. [Setting Up Cron Job](#setting-up-cron-job)
7. [AWS EC2 Deployment](#aws-ec2-deployment)
8. [Code Explanation](#code-explanation)
9. [Notes](#notes)


## Project Architecture

![image](https://github.com/Rahaf-Alweldi/RCP-Corum/assets/163084070/5332dafd-542c-47e3-8a3f-e0713bda7f6c)







## Features

- Scrapes data from multiple collections of watches on the Corum website.
- Extracts detailed information for each watch, including:

| Field Label | Description of Field |
|----------|----------|
| reference_number | This is the most unique identifier of a watch. |
| watch_URL | The link to the watch. |
| type | This is Men’s Watches, Women’s Watches, Unisex Watches, or Pocket Watches. If it says it on the individual watch page, it can be scraped. If not, leave it blank in the scrape. |
| brand | The name of the watch brand. |
| year_introduced | The year the watch was introduced. Most of the time this isn’t listed on the brand’s websites, so it can be left blank, but sometimes it is. |
| parent_model | This is the collection or family of the watch. |
| specific_model | An individual watch within the parent model category. |
| nickname | An informal or colloquial name given to a specific watch model. |
| marketing_name | Most watches won’t have these, but some will. It’s a special title like “2024 Olympics” or “Red Bull Edition” that’s unique to a limited edition watch, OR a name given to a watch by collectors. |
| style | The style will be listed on the watch pages or you'll be able to sort by the style in the collection pages. Potential values are: Dive, Chronograph, Military / Field, GMT, Dress, Atomic Radio Controlled, GPS, Smartwatch, Pilot, Skeleton, Racing / Driving, Sport, Digital |
| currency | standardization of money in USD |
| price | Should not contain any commas or currency symbols. Decimals are ok. For example, if the site says $4,800.50 then put the scraped value as 4800.50 - you do not need to include trailing zeros (so if the price is $5,000.00 then you can just populate 5000) |
| image_URL | A direct link to the image file of the watch. Make sure we get a high-resolution, front-facing image of the watch, even if it’s not the main product photo. Sometimes it is further down the page. |
| made_in | Find out where the brand’s watches are made and make that the automatic value for that brand. If they are made in different places, see if the product page says it for that watch. If you can't tell, leave it blank. |
| case_shape | The case shape (examples: Round, Rectangular, Tonneau, Oval, Irregular...) |
| case_material | This is almost always available. Include the entire field and we will clean and normalize the data later.  |
| case_finish | This might be listed as its own field, or it might be part of the case material or nickname data, in which case you'd scrape the entire field where it appears. Possible values are: Brushed, Polished, Sandblasted, Satin, Microblasted, Matte, Frosted |
| caseback | More often than not this will be its own field where it says “Open Caseback: Yes” or will be included in the case field when it says something like “Sapphire caseback” in which case you’d scrape that whole field and we’ll clean it up later. It could also be listed as open caseback, exhibition caseback, solid caseback, closed caseback. |
| diameter | This is almost always available. Make sure it’s the whole case diameter (usually 25 - 50 mm) and not the diameter of the movement which would be much smaller. Format as ## mm (including the space), or if there are two measurements (sometimes for oval or rectangular cases) format as ## x ## mm |
| between_lugs | Will sometimes be included. This is often called strap width or bracelet with - it’s the distance between two lugs on the same side of the watch where the strap hooks in. Usually will be 12 - 22 mm. Format as ## mm (including the space) |
| lug_to_lug | Will occasionally be included. This will be the biggest number if it is included (can be 50+ mm). It’s the distance from the tip of one lug to the tip of a lug on the other side of the watch. Careful not to mix this up with between_lugs |
| case_thickness | This is how thick a watch case is if you look at it from the side. It’ll usually be between 7 and 14mm if it’s there |
| bezel_material | This is the ring around the watch dial. The bezel material is not often listed by itself on a website, but sometimes it is listed as part of the entire “Bezel” description, in which case, scrape the whole field and it'll be cleaned later |
| bezel_color | This is the ring around the watch dial. The bezel material is not often listed by itself on a website, but sometimes it is listed as part of the entire “Bezel” description, in which case, scrape the whole field and it'll be cleaned later |
| crystal | Will usually be listed as Crystal or Glass on the site. This is the piece in front of the watch dial that protects it. Usually it will be Sapphire for high end brands, but can be things like Mineral Glass, Fiberglass, etc. |
| water_resistance | Will usually be listed as water resistance and will be labeled as meters, M, ATM, or Bar. Make sure you scrape the label as well so we can convert it to ATM during cleanup. |
| weight | Will usually be listed as weight if included. Make sure it’s the case weight and NOT just the weight of the movement mechanism, which is sometimes listed in the movement or caliber area. We want it in grams (labeled as g) |
| dial_color | Will usually be listed as a whole dial description if included. Scrape the whole dial field and we’ll clean it up |
| numerals | Occasionally numerals are listed, but more often it’s part of the dial description if it’s included at all. Might be something like Arabic numerals, Roman numerals, baton indexes, stick / dot, diamond indexes, gem-set indexes, etc. |
| bracelet_material | Sometimes called bracelet, strap material, etc. - we want the whole field, for example Alligator leather, Calfskin, stainless steel, etc. |
| bracelet_color | Might be included as part of the bracelet field or description. Scrape the entire field and it will be cleaned to extract the color |
| clasp_type | Sometimes called clasp, buckle, or closure. We're looking for a value like Folding clasp, Pin buckle, NATO strap, velcro, non-closure, etc. |
| movement | We want the type of movement here, not the caliber. Be careful when assigning website fields to make sure you’re mapping the right thing, because sometimes sites will have a field called Movement and list the caliber. If the field includes both, you can scrape the whole thing and it’ll be cleaned up. Movement examples are Automatic, self-winding, mechanical, manual winding, quartz, battery, etc. |
| caliber | Will usually be listed as caliber, calibre, movement, or mechanism. It’ll be a series of letters and numbers. |
| power_reserve | Will usually be listed as power reserve or energy. Quartz watches might not have this. |
| frequency | Will usually be listed as frequency and will be listed in units of Hz or vph. It's how quickly a watch ticks. Quartz watches will not have this. Be sure to include the unit, whatever it is |
| jewels | Will only ever be called jewels - not gemstones, parts, or components. Jewels are rubies or other jewels inside a watch's movement that help it move more smoothly. Quartz watches might not have this. |
| features | Might be called features, functions, or complications. We're looking for a complete list of functions or features that a watch has. If multiple fields contain features, scrape them all and make them comma-separated. |
| description | Will be the paragraph or two main product description. |


- Data cleaning to ensure the integrity and usability of the extracted data.
- Cron job setup to automate the scraping process at regular intervals.
- Implementation on AWS EC2 for reliable and scalable execution.

## Requirements

- Python 3.x
- `requests`
- `BeautifulSoup4`
- `pandas`

