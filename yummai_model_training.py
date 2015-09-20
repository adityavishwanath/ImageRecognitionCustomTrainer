"""
Uses the Clarafai API to learn a custom model.
Here: We train the module to understand the difference between Coca-Cola and Pepsi. 
The module returns a high confidence value for Coca-Cola and a low confidence value for Pepsi.
"""

#author Aditya Vishwanath
#created for HackMIT 2015

# """
# THE FOLLOWING COMMENT IS REDUNDANT.
# Concepts:
# 1. Grains.
# 2. Vegetables.
# 3. Fruits.
# 4. Milk.
# 5. Meat and Beans.
# """

from clarifai_basic import ClarifaiCustomModel

testConcept = ClarifaiCustomModel()
TEST_TAG = 'cocacola'
def conceptTrainer():
	# grainsConcept = ClarifaiCustomModel()
	# vegetablesConcept = ClarifaiCustomModel()
	# fruitsConcept = ClarifaiCustomModel()
	# milkConcept = ClarifaiCustomModel()
	# meatandbeansConcept = ClarifaiCustomModel()

	#TEST: To learn the coca-cola tag, and differentiate between Coca-Cola and Pepsi.

	#Should be optimized to pull data from an Image Search API and run multiple positive and negative tests.

	#Positives
	testConcept.positive('http://www.coca-cola.com/global/images/coke_disc.png', TEST_TAG)
	testConcept.positive('http://img3.wikia.nocookie.net/__cb20150801090518/logopedia/images/5/59/Coca-Cola_logo_2007.jpg', TEST_TAG)
	#testConcept.positive('https://upload.wikimedia.org/wikipedia/commons/c/ce/Coca-Cola_logo.svg', TEST_TAG)
	testConcept.positive('http://d1ynl4hb5mx7r8.cloudfront.net/wp-content/uploads/2014/11/coca-cola.jpg', TEST_TAG)
	testConcept.positive('https://pbs.twimg.com/profile_images/493592781575557120/H7R37Fc8_400x400.jpeg', TEST_TAG)
	testConcept.positive('http://www.impomag.com/sites/impomag.com/files/CocaCola_7.jpg', TEST_TAG)
	testConcept.positive('http://cdn.simplymeasured.com/wp-content/uploads/2014/05/Coke.jpg', TEST_TAG)
	testConcept.positive('http://www.rio2016.com/sites/default/files/imagecache/460x346_rounded_corners//sites/default/files/0_rodape_logosgrandes_v2_0000s_0020_coca-cola_0.png', TEST_TAG)
	testConcept.positive('http://dixiedelightsonline.com/wp-content/uploads/2015/05/coca_cola_bubbles-e1351441498523.jpg', TEST_TAG)
	testConcept.positive('http://www.relocatesitges.com/wp-content/uploads/2015/02/coca-cola-sitges.jpg', TEST_TAG)
	#testConcept.positive('http://nebula.wsimg.com/1bfc08e252c58f25711f63e0aab3ce21?ATEST_TAGessKeyId=4E4A2E83194F32D2E69F&disposition=0&alloworigin=1', TEST_TAG)
	testConcept.positive('http://abduzeedo.com/files/originals/c/coke1_1.jpg', TEST_TAG)
	testConcept.positive('http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2013/7/24/1374663182669/Coca-Cola-logo--008.jpg', TEST_TAG)
	testConcept.positive('http://www.coca-cola.com/global/images/coke_disc.png', TEST_TAG)
	#testConcept.positive('http://t2.gstatic.com/images?q=tbn:ANd9GcTGhIleSSts9txdNj5ji-D2MYhrVHmcHLssmkUZvMkuRlNkPHu5', TEST_TAG)

	#Negatives
	testConcept.negative('http://wallstcheatsheet.com/wp-content/uploads/2012/05/pepsi-logo.jpg', TEST_TAG)
	#testConcept.negative('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Pepsi_logo_2014.svg/2000px-Pepsi_logo_2014.svg.png', TEST_TAG)
	testConcept.negative('http://img3.wikia.nocookie.net/__cb20120813003900/bttf/images/8/84/Pepsi-logo-2012-1024x398.jpg', TEST_TAG)
	#testConcept.negative('https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Pepsi_logo.svg/1280px-Pepsi_logo.svg.png', TEST_TAG)
	testConcept.negative('http://www.aquaterracorp.ca/SupplyImages/WF00007/96040.VP_355ml_Pepsi.jpg', TEST_TAG)
	testConcept.negative('https://d17b1stq82ojj.cloudfront.net/wp-content/uploads/2015/06/pepsi-scholarships.png', TEST_TAG)
	testConcept.negative('http://www.marcczerwiec.com/vid/m_pepsi_versionTypo_FulllDEF_0636.jpg', TEST_TAG)
	testConcept.negative('http://topclassactionscom.c.presscdn.com/wp-content/uploads/2015/06/pepsi.png', TEST_TAG)
	testConcept.negative('http://www.dairyqueen.com/PageFiles/4957/dq-drinks-soft-pepsi.png', TEST_TAG)
	testConcept.negative('http://jamaicatakeout.com/wp-content/uploads/2015/02/Pepsi-HD-Wallpapers0.jpg', TEST_TAG)
	testConcept.negative('http://3219a2.medialib.glogster.com/rsscarr/media/f3/f33332a2a4d5b5f9b0828f556b971071985bcdca/pepsi-logo.png', TEST_TAG)
	testConcept.negative('http://dg6qn11ynnp6a.cloudfront.net/wp-content/uploads/2015/06/ziiqQdOt.jpg', TEST_TAG)
	#testConcept.negative('http://vignette3.wikia.nocookie.net/logosfake/images/5/50/Pepsi_2003.png/revision/latest?cb=20140327111847', TEST_TAG)
	#testConcept.negative('http://www.cartonwheels.com/image/cache/data/aerateddrinks/Pepsi%201L-500x500.jpg', TEST_TAG)
	testConcept.negative('http://www.simondanaher.com/mobile/wp2/wp-content/uploads/sites/2/2013/03/ret-Pepsi-Wet-wide-FLT-1920x1280.jpg', TEST_TAG)
	testConcept.negative('https://absolutelymindboggling.files.wordpress.com/2012/04/pepsi-bottle.jpg', TEST_TAG)
	testConcept.negative('http://static.caloriecount.about.com/images/medium/pepsi-diet-183174.jpg', TEST_TAG)
	testConcept.negative('http://couponing4you.net/wp-content/uploads/2015/07/pepsi.jpg', TEST_TAG)
	testConcept.negative('https://stephanieolivieri.files.wordpress.com/2014/02/pepsi-cola_1940s.png', TEST_TAG)

	testConcept.train(TEST_TAG)


if __name__ == "__main__":
	conceptTrainer() #Run the custom concept trainer.
	done = False
	while not done:
		result = None
		inputURL = raw_input("Enter an image URL to test: ")
		if inputURL != None:
			result = testConcept.predict(inputURL, TEST_TAG)
			if result['status']['message'] == 'Success':
				confidenceScore = result['urls'][0]['score']
				print "Your confidence score is = " + str(confidenceScore) + "  Hope this makes sense!"
			else: 
				print "We encountered some weird error!"
		else:
			print "ERROR IN URL!@#$%^"
		doneVal = raw_input("Are we done here? (y/n): ")
	 	if doneVal == 'y' or doneVal == 'Y' or doneVal == 'Yes' or doneVal == 'yes':
	 		done = True
	 	elif doneVal == 'n' or doneVal == 'N' or doneVal == 'No' or doneVal == 'no':
	 		print "All right then, let's go again!"
	 	else:
	 		print "That's not a valid input, so I'm just going to do this all over again."




