import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
        'project_name': 'AwesomeProject',
        'author_name': 'AwesomeName',
        'description': 'A very awesome project.',
        'open_source_license': 'BSD-3-Clause',
        'python_interpreter': 'python',
        'version': '0.1.0'
        }

def system_check(basename):
    platform = sys.platform
    if 'linux' in platform:
        basename = basename.lower()
    return basename

@pytest.fixture(scope='class', params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir
    )

    project_name = pytest.param.get('project_name') or 'project_name'
    
    # project name gets converted to lower case on Linux but not Mac
    project_name = system_check(project_name)

    project_path = out_dir/project_name
    request.cls.project_path = project_path
    yield 

    # cleanup after
    shutil.rmtree(out_dir)
    