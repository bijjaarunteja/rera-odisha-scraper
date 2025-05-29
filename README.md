
 RERA Odisha Project Scraper

📌 Overview

This project is a Python-based web scraper that uses **Selenium** to extract details of the **first 6 projects** listed under the “Projects Registered” section on the [RERA Odisha portal](https://rera.odisha.gov.in/projects/project-list).

🔍 Extracted Fields per Project:

✅ RERA Registration Number
 🏢 Project Name
 👨‍💼 Promoter Name (from *Promoter Details*)
 📍 Promoter Address (Registered Office Address)
 🧾 GST Number *(manually verified)*


 Technologies Used

* `Selenium` – for dynamic content interaction and scraping
* `csv` – for saving results
* `time` – for scroll delays
* `unused/gst_numbers.py` – contains hardcoded GST values for each project (due to inconsistent visibility on site)

 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/bijjaarunteja/rera-odisha-scraper.git
cd rera-odisha-scraper
```

2. **Install Required Packages**

```bash
pip install -r requirements.txt
```

3. **Update Chromedriver Path**
   Edit the line in `scraper.py`:

```python
Service(executable_path=r"path_to_your_chromedriver")
```

Replace it with your actual path.

---

## 🚀 Running the Script

```bash
python scraper.py
```

Upon execution, the script will:

* Open the website using Chrome
* Scroll to load projects
* Scrape required fields from the first 6 projects
* Save the data into `rera_projects.csv`

---

##  Project Structure

```
rera-odisha-scraper/
│
├── scraper.py              # Main scraper script
├── unused/
│   └── gst_numbers.py      # Hardcoded GST numbers for fallback use
├── rera_projects.csv       # Output CSV file
└── requirements.txt        # Required pip dependencies


 📌 Notes

* The RERA portal uses dynamic content loading, hence **Selenium** is used instead of `requests` or `BeautifulSoup` alone.
* GST numbers were **not consistently available** or scrappable from the site. A static list of verified GST numbers is used to ensure data completeness.
* If they fix the GST visibility on the website in the future, the code can be adapted to scrape them live.

---

Requirements (`requirements.txt`)

selenium
```

You also need to download the appropriate [ChromeDriver](https://chromedriver.chromium.org/downloads) and ensure it matches your browser version.

---

 Assignment Reference

> Write a Python program to scrape the first 6 projects listed under the “Projects Registered” section on the RERA Odisha site. Extract:
>
> * Rera Regd. No
> * Project Name
> * Promoter Name
> * Address of the Promoter
> * GST No

