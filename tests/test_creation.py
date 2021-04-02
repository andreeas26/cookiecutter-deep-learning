import os
import pytest
import re 

from subprocess import check_output

from conftest import system_check


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was Jinja able to render everything?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.project_path
        if pytest.param.get('project_name'):
            name = system_check('AwesomeProject')
            assert project.name == name
        else:
            assert project.name == 'project_name'
    
    def test_dockerfile(self):
        dockerfile_path = self.project_path/'docker/Dockerfile'
        assert dockerfile_path.exists()
        assert no_curlies(dockerfile_path)

    def test_dockerfile_maintainer_is_author_name(self):
        docker_file = self.project_path/'docker/Dockerfile'
        pattern = '"maintainer"="(.*)"'

        default_author = 'Your name (or your organization/company/team)'
        exp_author_name = pytest.param.get('author_name', default_author)

        maintainer = None
        with open(docker_file, 'r') as fp:
            lines = "\n".join(fp.readlines())
            maintainer = re.findall(pattern, lines) 
            maintainer = maintainer[0] if maintainer else maintainer

        assert maintainer == exp_author_name

    def test_dockerfile_version(self):
        docker_file = self.project_path/'docker/Dockerfile'
        
        default_version = "Project version"
        exp_version = pytest.param.get('version', default_version)

        pattern = '"version"="(.*)"'
        version = None
        with open(docker_file, 'r') as fp:
            lines = "\n".join(fp.readlines())
            version = re.findall(pattern, lines) 
            version = version[0] if version else version

        assert version == exp_version
    def test_dockerfile_description(self):
        docker_file = self.project_path/'docker/Dockerfile'
        
        default_description = "A short description of the project."
        exp_description = pytest.param.get('description', default_description)

        pattern = '"description"="(.*)"'
        description = None
        with open(docker_file, 'r') as fp:
            lines = "\n".join(fp.readlines())
            description = re.findall(pattern, lines) 
            description = description[0] if description else description
        assert description == exp_description
    def test_dockerfile_license_type(self):
        docker_file = self.project_path/'docker/Dockerfile'
        
        default_license_types = ["MIT", "BSD-3-Clause", "No license file"]
        exp_license_types = pytest.param.get('open_source_license', default_license_types)

        pattern = '"license"="(.*)"'
        license_type = None
        with open(docker_file, 'r') as fp:
            lines = "\n".join(fp.readlines())
            license_type = re.findall(pattern, lines) 
            license_type = license_type[0] if license_type else license_type

        assert license_type in default_license_types
    def test_readme(self):
        readme_path = self.project_path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert 'AwesomeProject' == next(fin).strip()

    def test_license(self):
        license_path = self.project_path / 'LICENSE'
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_requirements(self):
        reqs_path = self.project_path/'requirements.txt'
        assert reqs_path.exists()
        assert no_curlies(reqs_path)
    def test_folders(self):
        expected_dirs = [
            'configs',
            'configs/logging',
            'data',
            'docker',
            'docs',
            'experiments',
            'experiments/experiment_name',
            'experiments/experiment_name/train',
            'experiments/experiment_name/evaluation',
            'notebooks',
            'reports',
            'reports/figures',
            'tests',
            self.project_path.name,
            f'{self.project_path.name}/data',
            f'{self.project_path.name}/models',
            f'{self.project_path.name}/visualization',
        ]

        ignored_dirs = [
            str(self.project_path)
        ]

        abs_expected_dirs = [str(self.project_path/d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.project_path)))

        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0
