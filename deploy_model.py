import sagemaker
from sagemaker.pytorch import PyTorchModel

# Specify the IAM role with SageMaker permissions!!!!
sagemaker_role = '<your-sagemaker-role>'

# definning model
pytorch_model = PyTorchModel(model_data='s3://path-to-trained-model/model.tar.gz',
                             role=sagemaker_role,
                             framework_version='1.8.0',
                             entry_point='inference.py')

# deply model
predictor = pytorch_model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.xlarge',
    endpoint_name='chatbot-endpoint'
)
