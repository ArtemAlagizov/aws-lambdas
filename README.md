# aws-lambdas

How to use the repo:
* for creating and updating aws lambda functions in python ([aws_docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)):
    * install python3
    * install zip (or 7-zip)
    * install aws cli
        ```
        https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows
        ```
    * create function in a directory
    * install needed packages:
      ```
      py -m pip install --target ./package GitPython boto3
      ```
    * package function and packages into a zip archive
      ```
      cd package
      zip -r9 <path>\async-workers-lambda-scripts\lambdas\function.zip .
      cd ..
      zip -g function.zip generate_flights.py
      ```
    * upload the archive to aws:
      ```
      aws lambda update-function-code --function-name generate_flights --zip-file fileb://function.zip --profile sub-zero
      ```
