from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
    core
)


class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="my-first-cdk-project-2022-10-14",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
            
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
        )
        
        _iam.Group(
            self,
            "gid"
        )




        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first CDK Bucket",
            export_name="myBucketOutput1"
        )