# data_science
Archiving my learnings on machine learning and data science related stuff.

Python 3.5
##############
sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)



Module Dependencies 
####################
(venv) C:\BITS\dm_asg\code>python -m pip freeze
et-xmlfile==1.0.1
jdcal==1.4
numpy==1.14.3
openpyxl==2.5.3
pandas==0.22.0
python-dateutil==2.7.2
pytz==2018.4
scikit-learn==0.19.1
scipy==1.0.1
six==1.11.0
sklearn-extensions==0.0.2
xlrd==1.1.0
XlsxWriter==1.0.4




How to Run?
#############
1. Modify the data directory path in main.py
2. Adjust the Test Percent (Percentage of dataset used for test) value - default is 0.3
2. Execute the main.py




What you should see post execution?
#####################################
1. Each algorithm is run on each file, the program will take few minutes to complete
2. output folder created with data equivalent *.xlsx files and a consolidated_results.xlsx file




Meaning of different sheets
##############################
input - raw data
input_normalized - removed unwanted fields like name, version etc and bug data normalized to 0 and 1
output_<algorithm> - test data listed with actual and predicted output post execution of algorithm
output_<algorithm>_result - computed performance metrics evaluation for the algorithm 

