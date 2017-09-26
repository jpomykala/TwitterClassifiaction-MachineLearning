import twitterService
import dataFacade
from textBlobProcessing import train_classifier
import os
import pprint
import random
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# user_id = twitterService.get_user_by_tweet_id(909364401047617537)
# print(user_id)

# twitterService.get_user_tweets(user_id)


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "start")
worksheet.write(1, 0, "test 10")
worksheet.write(0, 1, "test 01")
workbook.close()

dataFacade.update_data()
cl = train_classifier()
cl.show_informative_features(5)	

sick_post_ids = dataFacade.getSickPostIds()

# get meta info
# save creation date 
# get more posts (after detected sickness)
# decide if next post is heal
# if heal get date 
# calculate days between sick/heal
# write to xlsx
# next
