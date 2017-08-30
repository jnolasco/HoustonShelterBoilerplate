import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import httplib2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Follow instructions here to create a service account. This code uses the p12 key format, not json.
https://developers.google.com/api-client-library/php/auth/service-accounts
"""
def analytics_service():
    scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # REPLACE THESE PLACEHOLDER VALUES
    key_file_location = os.path.join(BASE_DIR, 'your-service-account.p12')
    service_account_email = 'service-account-name-000@project-name.iam.gserviceaccount.com'

    return get_service('sheets', 'v4', scope, key_file_location, service_account_email)

def get_service(api_name, api_version, scope, key_file_location, service_account_email):
    """
    Get a service that communicates to a Google API.

    Args:
      api_name: The name of the api to connect to.
      api_version: The api version to connect to.
      scope: A list auth scopes to authorize for the application.
      key_file_location: The path to a valid service account p12 key file.
      service_account_email: The service account email address.

    Returns:
      A service that is connected to the specified API.
    """
    f = open(key_file_location, 'rb')
    key = f.read()
    f.close()

    credentials = SignedJwtAssertionCredentials(service_account_email, key, scope=scope)

    http = credentials.authorize(httplib2.Http())

    # Build the service object.
    service = build(api_name, api_version, http=http)

    return service

"""
Instant boilerplate code for dumping the contents of the Houston Shelter Map spreadsheet.
1) You must generate your own p12 key for production purposes.
https://developers.google.com/api-client-library/php/auth/service-accounts
 
2) pip install -r requirements.txt
Make sure that you install all the necessary libraries. Optional: use a virtualenv.

3) python runserver and go to the index page. Should dump the spreadsheet.
"""
def index(request):
    # get the service using the included key.
    # if google caps the one in the repo, generate your own.
    service = analytics_service()

    # get the full contents of the spreadsheet here:
    # https://docs.google.com/spreadsheets/d/14GHRHQ_7cqVrj0B7HCTVE5EbfpNFMbSI9Gi8azQyn-k/edit#gid=0
    spreadsheetId = '14GHRHQ_7cqVrj0B7HCTVE5EbfpNFMbSI9Gi8azQyn-k'
    rangeName = 'Shelters!A2:P'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    ctx = { }
    ctx['values'] = values

    # populate the template however you like
    response = render_to_response('index.html', RequestContext(request, ctx))

    return response
