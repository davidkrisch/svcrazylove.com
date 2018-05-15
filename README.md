My cruising blog ([svcrazylove.com](https://svcrazylove.com)) is a static
website hosted in an s3 bucket with CloudFront acting as CDN and https
termination point.

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
# So we can invalidate the CloudFront cache...
brew install awscli
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

# Clear CloudFront cache

The site uses AWS CloudFront for https and CDN.  When the site is updated we
have to manually clear the CloudFront cache or wait until the TTL expires.
That could be as much as a day, so I've added another step to the deploy
process.

```bash
./create_invalidation.sh
```
