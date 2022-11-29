## Serverless Machine Learning Applications with Hugging Face Gradio and AWS Lambda

### Getting started

You must have an **AWS account** configured and ready to use; furthermore, you need **npm**.
**Python >= 3.6** is required.
1. Create a virtual environment
   ```shell
   python -mvenv .venv
   . .venv/bin/activate
   ```

2. Install the requirements
    ```shell
   pip install -r requirements.txt
   ```
3. Install [cdk](https://aws.amazon.com/it/cdk/)
   ```shell
   npm install -g aws-cdk
   ```

4. Deploy
   ```shell
   cdk bootstrap
   cdk deploy
   ```

### Run locally

You can also run the model locally:

```shell
python download_model.py
python app.py
```

The model will run locally at http://127.0.0.1:8080/
