My cruising blog (svcrazylove.com) is a static website hosted in an s3 bucket.

# Install & Configure

```bash
cd ~/Documents
git clone git@github.com:davidkrisch/svcrazylove.com.git
cd svcrazylove.com
pip install virtualenv
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
# Install s3cmd and set up keys
brew install s3cmd
s3cmd --configure  # Retrieve credientials from AWS console
```

# Generate html

```bash
cd ~/Documents/svcrazylove.com
benjen
```

# Generate images

```bash
cd ~/Documents/website-images
cp ../svcrazylove.com/small.py .
python small.py
```

# Deploy to S3

```bash
cd ~/Documents/svcrazylove.com/output
s3cmd sync . s3://svcrazylove.com
```
