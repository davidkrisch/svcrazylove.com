Installation 

Before doing pip install -r requirements.txt, install libjpeg from:

http://ethan.tira-thompson.com/Mac_OS_X_Ports.html

Install s3cmd and set up keys

Generating the Site and Pushing it to S3

To generate the site:
    benjen

To generate the sites images:
    python small.py 
In ~/Documents/website-images

To upload the generated site to S3:
    cd ~/Documents/svcrazylove.com/output
    s3cmd sync . s3://svcrazylove.com
