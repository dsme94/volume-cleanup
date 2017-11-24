# volume-cleanup
Python script which will check for volumes in an available state and remove them. Testing with moto.

I have included the script which can be deployed straight to lambda, see lambda/ebs.py. Note that if no region is supplied in lambda environments variables then the region will be defaulted to the region in which the function is deployed.

# Moto
Moto is a library that allows your tests to easily mock out AWS Services.
https://github.com/spulec/moto

# Using this script
Testing can be achieved by executing ebs_test.py (python ebs_test.py). 
To run the script you can execute (python ebs.py). 

# Requirements
boto3 
moto
python 2.7.11

```
$ pip install moto
$ pip install boto3
```
