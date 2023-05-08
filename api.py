import tweepy

def twitterPost(textTwitter):
  #textTwitter = ''#'This is a test :p'
  print(textTwitter)

  API_key= 'Ku6y6yvhvRs1hymaMFEmf7XGu'
  API_secret= '0wHz79bNzANyP2DAkbaaj2vnFY7RMxfuCFFRFsNgV6x4GFZA3H'
  bearer_token='AAAAAAAAAAAAAAAAAAAAAC5OnAEAAAAAZpJ%2FkQEOCECiyGkqENcX9b4QFBk%3DrFwfPMPBsrS8pTwgarFnOq8nYAlpMrNNVIOUuD5Ladkulfofkz'
  access_token= '1651336519146442752-6quQKZt1YjWAbuUzl0nHqUhpPt0zxZ'
  access_token_secret= 'qfWXbdQgwJz4KakUMKdpPqEAnID3JOpFs2v9F4ER64yC1'

  client = tweepy.Client(bearer_token,API_key, API_secret,access_token, access_token_secret)
  auth = tweepy.OAuth1UserHandler(bearer_token,API_key, API_secret,access_token, access_token_secret)
  response = client.create_tweet(text = textTwitter)
  print (response)
  return

  
  def postTweet(passedString,bearer_token,API_key, API_secret,access_token, access_token_secret):
    textTwitter = passedString
    
    client = tweepy.Client(bearer_token,API_key, API_secret,access_token, access_token_secret)
    
    auth = tweepy.OAuth1UserHandler(bearer_token,API_key, API_secret,access_token, access_token_secret)
  
    response = client.create_tweet(text = textTwitter)
    print(response)
  
  postTweet(bearer_token,API_key, API_secret,access_token, access_token_secret)

