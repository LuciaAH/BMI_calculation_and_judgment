height = float (input ('您的身高是? (m)'))
weight = float (input ('您的體重是? (kg)'))
bmi = weight / height / height
if bmi < 18.5:
	print ('您的bmi是', bmi, '，為過輕。')
elif bmi >=18.5 and bmi <24:
	print ('您的bmi是', bmi, '，為正常。')
elif bmi >=24 and bmi <27:
	print ('您的bmi是', bmi, '，為過重。')
elif bmi >=27 and bmi <30:
	print ('您的bmi是', bmi, '，為輕度肥胖。')
elif bmi >=30 and bmi <35:
	print ('您的bmi是', bmi, '，為中度肥胖。')
else:
	print ('您的bmi是', bmi, '，為過度肥胖。')