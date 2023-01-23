#to calculate age
p_age=int(input('Enter your current age\n'))
print('your age after 5 years\n')
f_age=p_age+5
print(f_age)
print('your age 10 years earlier is\n ')
past_age=p_age-10
print(past_age)

#To calculate height
feet=0.3048#in
inch=0.0254#cm
meter=100
height_1=int(input('Enter your height in feet'))
height_2=int(input('Enter your height in inches'))
conv=float(height_1*feet)
conv_2=conv+height_2
print('your height in meters is :')
print (format((conv_2),'.2f'))#conv_2
print('height in cm is')
conv_3=conv_2*meter
print (format((conv_3),'.2f'))