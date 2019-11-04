# Problem : Convert given API(json) format to Human Readable format

# Please consider following steps to solve this problem

Step 1: In order to work with APIs in Python we need "requests library".
        Install requests by using below command

        pip install requests

Step 2: Name of script is   apiparser.py

Step 3: import requests

Step 4: Write a Python script which  takes API link as input and convert to human readable file.
        Input : api_link
        i.e for this problem link : https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences

Step 5: Run Python file - apiparser.py
        get the output

      Output :  prints the output as
        List of upcoming paid technical conferences
        List of upcoming Free technical conferences, according to format shown below

        format : 'conference Name','conference Start Date','city','state','country','entry type','conference Register Url'

      for example
        1.'Beyond Tellerrand Berlin', 04 Nov, 2019, Berlin, ,  Germany, Paid, https://beyondtellerrand.com/events/berlin-2019
        2.'Indo Data Week 2019', 04 Nov, 2019, Hyderabad,  Telangana,  India, Paid, https://www.indodataweek.com/conference/indo-data-week
        3.'Devopsdays Montreal 2019', 05 Nov, 2019, Montreal,  QC,  Canada, Paid, https://devopsdays.org/events/2019-montreal/welcome/
        4.'FutureCon San Antonio Cyber Security Conference', 06 Nov, 2019, San Antonio, Texas, United States, Paid,
            https://futureconevents.com/events/san-antonio/c
        .
        .
        .
         so on

      output also prints if any duplicate list found
      else
      No duplicates found!!!
