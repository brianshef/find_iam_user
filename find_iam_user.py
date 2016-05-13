#!/usr/bin/env python
# Find the IAM username belonging to AWS_ACCESS_KEY_ID
# Useful for finding IAM user corresponding to a compromised AWS credential
# Usage:
#     find_iam_user AWS_ACCESS_KEY_ID
# Requirements:
#
# Environmental variables:
#     AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
#     or
#     AWS_PROFILE
# python:
#   boto

import boto.iam
import sys

if len(sys.argv) == 1:
  print 'Usage: \n find_iam_user AWS_ACCESS_KEY_ID'
  exit(1)

TARGET_ACCESS_KEY = sys.argv[1]

iam = boto.connect_iam()

marker = None
is_truncated = 'true'
users = []

while is_truncated == 'true':
  all_users = iam.get_all_users('/',marker=marker)
  users += all_users['list_users_response']['list_users_result']['users']
  is_truncated = all_users['list_users_response']['list_users_result']['is_truncated']
  if is_truncated == 'true':
    marker = all_users['list_users_response']['list_users_result']['marker']

print "Found " + str(len(users)) + " users, searching..."

def find_key():
  for user in users:
    for key_result in iam.get_all_access_keys(user['user_name'])['list_access_keys_response']['list_access_keys_result']['access_key_metadata']:
      aws_access_key = key_result['access_key_id']
      if aws_access_key == TARGET_ACCESS_KEY:
        print 'Target key belongs to user: ' + user['user_name']
        return True
  return False

if not find_key():
  print 'Did not find access key (' + TARGET_ACCESS_KEY + ') in ' + str(len(users)) + ' IAM users.'
