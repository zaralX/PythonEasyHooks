# PythonEasyHooks
This code will allow you to create discord webhooks very easily. You only need to enter data in the config.

FOR SPAWN WEBHOOKS RUN webhook.py

What in webhookconfig.py:

# specify here the variables to run
loadhooks = ['example']

# variable webhook. you must add more
example = {
  # place here webhook or webhooks to send in channels
	'hooks': ['WEB HOOK'],                
  # WebHook User Name
	'name': 'A config test name',          
  # Default message
	'content': 'A config content message', 
  # True - send Embeds False - not send Embeds
	'embedrule': True,                    
	# here embeds for send. if you selected EMBEDRULE:FALSE you can leave it as it is or erase it to the brackets of the list
  'embed': [{                            
  # place here Embed Image
		'image': 'https://cdn.discordapp.com/attachments/702071656729935933/881273560033816637/1630182315220.jpg',            
  # place here text above embed
		'author_name': 'example author',   
  # icon above embed
		'author_icon': 'https://cdn.discordapp.com/attachments/702071656729935933/911596518295875624/images_25.jpeg',                      
  # if user click on AuthorName running this command
		'author_url': 'https://github.com/zaralX',                                                                                         
  # icon top right in embed
		'thumbnail': 'https://cdn.discordapp.com/attachments/702071656729935933/855853580203065375/2eea5d6b72eac426a40657249d52c7a1.png',    
  # under embed text
		'footer_name': 'example footer',                                                                                                     
  # under text embed icon
		'footer_icon': 'https://cdn.discordapp.com/attachments/702071656729935933/727903114564337734/Screenshot_20200623-005546_Camera.jpg', 
  # Embed name under of author and above of description
		'name': 'A config test embed name',                          
  # Embded descriprion (under of EmbedName)
		'description': 'A config test embed description',            
  # line color in HEX
		'color': '03b2f8',                                          
  # True - add send time to footer (For each user's timezone and language will be changed) False - not add this
		'timestamp': True,                                           
  # add table? True - YES False - NO (you can leave it as it is or erase it to the brackets of the list)
		'fieldsrule': True,                                          
  # Table (he under of description)
		'fields': [{                                        
  # String Name
			'name': 'example field 1',                        
  # String Description
			'value': 'example field value 1'     
  # add more strings ( ,{'name':'','value':''} )
		}, - last string
		{
			'name': 'example field 2',
			'value': 'example field value 2'
		}
    ] - list end
  # add more embeds in message, copy all in {} and add ,
	}, - end last embed
	{
		'image': '',
		'author_name': 'example author',
		'author_icon': 'https://cdn.discordapp.com/attachments/702071656729935933/911596518295875624/images_25.jpeg',
		'author_url': 'https://github.com/zaralX',
		'thumbnail': '',
		'footer_name': 'example footer',
		'footer_icon': 'https://cdn.discordapp.com/attachments/702071656729935933/727903114564337734/Screenshot_20200623-005546_Camera.jpg',
		'name': 'A config test embed name 2',
		'description': 'A config test embed description 2',
		'color': '03fff8',
		'timestamp': False,
		'fieldsrule': True,
		'fields': [{
			'name': 'example field 1',
			'value': 'example field value 1'
		},
		{
			'name': 'example field 2',
			'value': 'example field value 2'
		}]
	}] - }-embed end ]-embeds end
} - variable end
