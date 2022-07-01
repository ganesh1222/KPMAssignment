import urllib.request as urlreq
instanceid = urlreq.urlopen('http://ip/latest/meta-data/instance-id').read()
instancetype = urlreq.urlopen('http://ip/latest/meta-data/instance-type').read()
#all the instance metadata can be fetched using below link
#https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instancedata-data-categories.html
print(instanceid,instancetype)

# We can also fetch data of ec2 resource using boto3 module as well.s