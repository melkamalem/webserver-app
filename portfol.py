from flask import Flask, render_template, request, redirect
import csv, sys, sysconfig

Webapp = Flask(__name__)
print(__name__)

@Webapp.route('/')
def welcome():
 	return render_template('index.html')

@Webapp.route('/<string:page_name>')
def html_page(page_name):
 	return render_template(page_name)

# def write_to_file(data):
#  	with open('database.txt', newline='', mode='a') as database:
# 			name = data["name"]
# 			email = data["email"]
# 			message = data["message"]
# 			file = database.write(f'\n{name},{email},{message}')
# 			database.write = ([name,email,message])
		
def write_to_csv(data):
 	with open('database.csv', newline='', mode='a') as database2:
			name = data["name"]
			email = data["email"]
			message = data["message"]
			csv_writer = csv.writer(database2, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([name,email,message])

@Webapp.route('/send_message', methods=['POST', 'GET'])
def send_message():
	if request.method == 'POST':
		data = request.form.to_dict()
		#write_to_file(data)
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong. Please make sure your email is correct and try again.'
	
    
# @Webapp.route('/')
# def welcome():
# 	return render_template('index.html')

# @Webapp.route('/home')
# def welcome2():
# 	return render_template('index.html')

# @Webapp.route('/My Background')
# def my_background():
# 	return render_template('elements.html')

# @Webapp.route('/VOLUNTEERISM AND LEADERSHIP')
# def volunteerism():
# 	return render_template('elements.html')

# @Webapp.route('/Career_experience')
# def Career_Experience():
# 	return render_template('elements.html')

# @Webapp.route('/GET IN TOUCH')
# def get_in_touch():
# 	return render_template('index.html')

