# niko-exercises
Exercises and lessons for Niko.

## Prerequisites

1. Make sure you have Python 3.
```bash
python3 --version
```

2. Install Python 3 if you don't have it.
```bash
brew install python
```

3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/).

```bash
pip install virtualenv
```

4. Create a virtualenv for this project. This will allow you to keep all your dependencies up to date and consistent with what is expected. It will also allow you to pip install packages without `sudo`.
```bash
virtualenv -p python3.6 ~/virtualenvs/niko-exercises
```

5. Activate the virtualenv.
```bash
source ~/virtualenvs/niko-exercises/bin/activate
```

6. Install the requirements for this project. You should do this perioidically to make sure you are up to date.
```bash
pip install -r requirements.txt
```

7. Install [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download). The IDE has tools that are going to make your life a lot easier and help you catch mistakes before committing to git.

8. Point PyCharm at the correct virtualenv. Go to Settings > Project Settings > Project Interpreter. Click the gear icon next to the dropdown and select Add Local. Navigate to the location of the virtualenv you created in step 4. Select the `bin/python` executable in that directory.

## Exercises

1. [PEP-8](exercises/pep8) - best practices for conventional code styling