# Generate master token to be used in keep_import.py for authentication.

import gpsoauth

email = 'your@google.email.here' # insert your Google username (email) here
android_id = '000000cc99ffaa44' # put a fake Andoid ID
token = 'oauth2_4/your-oauth-token-from-cookie-here' # insert the oauth_token here

master_response = gpsoauth.exchange_token(email, token, android_id)
print(master_response)

master_token = master_response['Token']  # if there's no token check the response for more details with print(master_response)
print(master_token)
