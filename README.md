# surf_dashboard
Dashboard for serfers
This project involves scraping surf forecast data from a webpage, cleaning the extracted data using Python, and visualizing it using flexdashboard in R. It provides a complete workflow for analyzing surf conditions, making it useful for surfers, meteorologists, or enthusiasts interested in weather and surf trends.

surf_dashboard/
|
├── surf_scrap/
│   ├── __init__.py
│   └── meteo_surf_scrap.py       # Python script for data extraction
│
├── run_surf_scrap_library.py      # Script to execute data extraction
├── output.csv             # Extracted and cleaned data
├── README.md              # Project documentation
└── surf-dashboard.Rmd      # R script for flexdashboard visualization
