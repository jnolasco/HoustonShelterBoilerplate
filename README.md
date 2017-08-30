# HoustonShelterBoilerplate

Python/Django code to dump the contents of the Houston Shelter Map spreadsheet to a web page. The various bits of sample code floating around on the internet for Python are a mix of broken and wrong and wonky.

This is a bare bones project for dumping the contents of the public Google Sheets document located here to screen:
https://docs.google.com/spreadsheets/d/14GHRHQ_7cqVrj0B7HCTVE5EbfpNFMbSI9Gi8azQyn-k/edit#gid=0

From there, you can cache it (highly recommended) or transform the data internally. 

1) Clone this repo.
2) pip install -r requirements.txt
3) Create a service account .p12 key with these instructions.
https://developers.google.com/api-client-library/php/auth/service-accounts
4) Start your Python/Django server and go the to the index page. It should dump the spreadsheet. This same code should work for any public spreadsheet but you'll have to modify the range you're pulling.

*Do NOT write to this document using this library.*
*Do NOT remove the read only flag.*

Do all your transforms locally.

Happy hacking.
