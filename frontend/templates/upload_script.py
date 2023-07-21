# import os
# fi = form['filename']
# if fi.filename:
# 	# This code will strip the leading absolute path from your file-name
# 	fil = os.path.basename(fi.filename)
# 	# open for reading & writing the file into the server
# 	open(fn, 'wb').write(fi.file.read())




# #2- $ pip install requests
# import requests
# dfile = open("datafile.txt", "rb")
# url = "http://httpbin.org/post"
# test_res = requests.post(url, files = {"form_field_name": dfile})
# if test_res.ok:
#     print(" File uploaded successfully ! ")
#     print(test_res.text)
# else:
#     print(" Please Upload again ! ")

# #3-Using Filestack API
# pip install filestack-python

# from filestack import Client
# c = Client("API's Key")
# filelnk = c.upload(filepath = '/path/of/file.png')
# print(filelnk.url)

# # this is trying to connect index.html button to untitled2 py code 