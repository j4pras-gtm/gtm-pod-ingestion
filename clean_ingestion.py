name: Clean & Anonymize GTM Data
on:
  push:
    paths:
      - 'raw_input.csv'
  workflow_dispatch:

jobs:
  clean
