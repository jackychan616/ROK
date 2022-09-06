from discord_webhook import DiscordWebhook, DiscordEmbed

url = ["https://discord.com/api/webhooks/1015241597388070962/wXSejycDR0fhbJdc3Z8JRQrkhf_gEObrYPCV-h3irtBaXVUTiLpCD0NMjpgsP0C8ZhMo","https://discord.com/api/webhooks/1015232903560577115/i38-FAKXlHlFEyZb4Pq5N0Vkc08ybwaIeCflBR_4ydXFzjKoqQEyMbW3ZmJG-Bqw5kmK"]

webhook = DiscordWebhook(url=url,username="epic",avatar_url="",content="idk https://images.pexels.com/photos/267569/pexels-photo-267569.jpeg") 

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
# add embed object to webhook

response = webhook.execute()