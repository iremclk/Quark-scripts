# Quark-scripts
Detect vulnerabilities in binaries via automated Quark scripts
(https://github.com/quark-engine)

## Usage of Scripts
Quark Script requires Python 3.8 or above.
1.	First, install Quark Engine by running:
```
pip3 install quark-engine
```
2. Add the apk file in same directory with the scripts. 
![image](https://user-images.githubusercontent.com/15799224/221565551-5a80b361-4b54-452f-abcd-8cf1c631989a.png)

3.	Edit apk name in the globVariable.py file:

applicationName = "exampleApp.apk"

4.	Run with the following command:
```
./main.sh > Quark-Report.txt
```
