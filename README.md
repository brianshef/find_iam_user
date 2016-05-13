# find_iam_user
Python script to find an AWS IAM user by AWS ACCESS KEY ID

## Requirements

This sample project depends on *boto*, the AWS SDK for Python, and requires
Python 2.6.5+ or 2.7. You can install *boto* using `pip`:

    pip install boto

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys.

## Usage
`python find_iam_user.py <SOME-ACCESS-KEY-ID-STRING>`
