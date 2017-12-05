import terraform_validate
import unittest
import os
import sys

class TestAWSResources(unittest.TestCase):

    # This list contains the resource types where rules should be applied
    # It's a subset of main identities related to most common services.
    # See https://www.terraform.io/docs/providers/aws
    AWS_RESOURCES = [
       "aws_ami",
       "aws_autoscaling_group",
       "aws_cloudformation_stack",
       "aws_cloudfront_distribution",
       "aws_cloudwatch_dashboard",
       "aws_config_config_rule",
       "aws_db_instance",
       "aws_db_snapshot",
       "aws_ebs_snapshot",
       "aws_ebs_volume",
       "aws_ecr_cluster",
       "aws_ecs_cluster",
       "aws_efs_file_system",
       "aws_eip",
       "aws_elastic_beanstalk_application",
       "aws_elasticache_cluster",
       "aws_elasticsearch_domain",
       "aws_emr_cluster",
       "aws_iam_access_key",
       "aws_iam_group",
       "aws_iam_policy",
       "aws_iam_role",
       "aws_iam_role_policy",
       "aws_iam_user",
       "aws_instance",
       "aws_key_pair",
       "aws_kms_key",
       "aws_lambda_function",
       "aws_launch_configuration",
       "aws_lb",
       "aws_rds_cluster",
       "aws_route53_zone",
       "aws_s3_bucket",
       "aws_security_group",
       "aws_sns_topic",
       "aws_subnet",
       "aws_vpc"
    ]

    # This is the list of required tags
    REQUIRED_TAGS = [
        "Name",
        "Description",
        "Owner",
        "Provisioner"
    ]

    def setUp(self):
        # tfrules.sh provides the directory of the terraform files as argument
        terraform_directory = sys.argv[1]

        # Tell the module where to find your terraform configuration folder
        self.path = terraform_directory
        self.v = terraform_validate.Validator(self.path)

    def test_tags(self):
        # Assert that all resources of these types have the required tags
        self.v.resources(self.AWS_RESOURCES).property('tags').should_have_properties(self.REQUIRED_TAGS)

    def test_naming(self):
        # Assert that all resources of these types doesnt include/repeat the resource type on the resource name
        # We check agains a list of names not including the "aws_" preffix used by Terraform. Therefore, instead
        # of just check if "aws_iam_group" is part of the name, we check against the use of "iam_group"
        check_list = []
        for aws_resource in self.AWS_RESOURCES:
            check_resource = aws_resource.replace("aws_", "")
            check_list.append(check_resource)
        self.v.resources(self.AWS_RESOURCES).property('name').list_should_not_contain(check_list)
        # NOTE: The above checking is just for the "name" property of the resource.
        #       For the actual resource name the function "name_should_match_regex" could be used.

if __name__ == '__main__':
    # Execute tests and return success to shell (for pre-commit)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAWSResources)
    ret = not unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful()
    sys.exit(ret)
