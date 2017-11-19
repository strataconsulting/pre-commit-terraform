# pre-commit-terraform hook

Collection of [pre-commit](http://pre-commit.com/) hooks for Terraform files.

An example `.pre-commit-config.yaml`:

```yaml
-   repo: git://github.com/strataconsulting/pre-commit-terraform
    sha: v1.2.0-st1
    hooks:
      -   id: terraform_fmt
      -   id: tflint
      -   id: terralint

```
