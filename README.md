# Github Classrooms `main.cpp` Autograding Template

 - A classroom demo (hello world).
 - Autograding
 - Self-hosted
 - Python-based `main.cpp` autograding.

> Source code: [https://github.com/inha-zjcao/github-classrooms-cpp-helloworld-autograding-template](https://github.com/inha-zjcao/github-classrooms-cpp-helloworld-autograding-template)

## 1. Week-01 quiz-01 helloWorld.

### 1.1. Requirement.

- You must complete the code in C++. 

- Note that the inputs and outputs must match the following example.

### 1.2. Example.

> Week01 quiz01 _Hello World_ demo

**Example 1:**

Input: `frank`

Output: `Hello frank!`

**Example 2:**

Input: `world`

Output: `Hello world!`

### 1.3. Others.

None.


## 2. Autograding of `main.cpp` with `python.py`.

### 2.1. Python-based autograding code.

```python
"""
Python-based `main.cpp` Autograding 
Code: czjing
Data: 2024.03.28
"""

# week01_quiz01_score01.py
import subprocess
import argparse

def run_jobs(cmd, cmd_inputs=None):
    if cmd_inputs is not None:
    	# create process
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    	# send cmd_input
        p.stdin.write(cmd_inputs.encode('utf-8'))

        # get results.
        output, error = p.communicate()

        return output.decode('utf-8'), error.decode('utf-8')
    else:
    	# create process.
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # get results.
        stdout, stderr = process.communicate()

        return stdout.decode('utf-8'), stderr.decode('utf-8')


def runing(args):
    # ------------
    # g++
    gcc_output, gcc_error = run_jobs(cmd="g++ "+args.cpp_path)
    assert gcc_error == "", "### compile error (g++ main.cpp)."
    # ------------
  
    # ------------
    ## demo: sum
    # input
    # cmd_input = "1\n1\n"

    # # get return.
    # output, error = run_jobs(cmd="./a.out", cmd_inputs=cmd_input)
    # assert gcc_error == "", "### output error (./a.out)."

    # # match.
    # # assert output == b'2\n'
    # assert output == "2\n", "### output error (./a.out)."
    # ------------

    # ------------
    # define input & get return.
    output, error = run_jobs(cmd="./a.out", cmd_inputs=args.cmd_input)

    assert gcc_error == "", "### output error (./a.out)."

    # match.
    assert output == args.cmd_output, "### output error (./a.out)."
    # ------------


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cpp_path', type=str, default= "main.cpp", help='main.cpp path.')
    parser.add_argument('--cmd_input', type=str, 
        default= "Frank\n", 
        help='test input.'
    )
    parser.add_argument('--cmd_output', type=str, 
        default= "Hello Frank!\n", 
        help='test output.'
    )
    args = parser.parse_args()

    # print(args)
    runing(args)
```


### 2.2. Upload to self-hosted server.

```bash
(torch) ➜  week01 pwd
/home/zjcao/actions-runner/_work/eval_py/week01
(torch) ➜  week01
(torch) ➜  week01 ll
total 8.0K
-rw-rw-r-- 1 zjcao zjcao 2.1K Mar 28 16:26 week01_quiz01_score01.py
-rw-rw-r-- 1 zjcao zjcao 2.1K Mar 28 16:26 week01_quiz01_score02.py
```

### 2.3. Create `.github/workflows/classroom.yml` in template repository. 

- Do not use the GitHub Classroom Assignment UI to set Autograding. 
- You need to define `.github/workflows/classroom.yml` workflow file in the template repo.
- ref: https://github.com/orgs/community/discussions/68249

```yml
# .github/workflows/classroom.yml
name: Autograding Tests
'on':
- push
- workflow_dispatch
- repository_dispatch
permissions:
  checks: write
  actions: read
  contents: read
jobs:
  run-autograding-tests:
    # runs-on: ubuntu-latest
    runs-on: self-hosted
    if: github.actor != 'github-classroom[bot]'
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    - name: week01_quiz01_score01
      id: week01_quiz01_score01
      uses: education/autograding-command-grader@v1
      with:
        test-name: week01_quiz01_score01
        setup-command: ''
        command: python /home/zjcao/actions-runner/_work/eval_py/week01/week01_quiz01_score01.py
          main.cpp
        timeout: 10
        max-score: 5
    - name: week01_quiz01-score02
      id: week01_quiz01-score02
      uses: education/autograding-command-grader@v1
      with:
        test-name: week01_quiz01-score02
        setup-command: ''
        command: python /home/zjcao/actions-runner/_work/eval_py/week01/week01_quiz01_score02.py
          main.cpp
        timeout: 10
        max-score: 5
    - name: Autograding Reporter
      uses: education/autograding-grading-reporter@v1
      env:
        WEEK01_QUIZ01_SCORE01_RESULTS: "${{steps.week01_quiz01_score01.outputs.result}}"
        WEEK01_QUIZ01-SCORE02_RESULTS: "${{steps.week01_quiz01-score02.outputs.result}}"
      with:
        runners: week01_quiz01_score01,week01_quiz01-score02
```

### 3. Upload `mian.cpp` to repository.

```cpp
// mian.cpp
#include <iostream>

using namespace std;

int main(){
    string name;
    cin >> name;

    cout << "Hello " << name << "!" << endl;

    return 0;
}
```


### 4. Check results.

![score.png](https://raw.githubusercontent.com/inha-zjcao/cpp-hello-world-workflow-template/main/.imgs/score.png "score.png")


## 5. Ref.

Ref-1: https://github.com/orgs/community/discussions/68249 \
Ref-2: https://mti-lab.github.io/blog/2021/12/15/autograding.html


> Autor: czjing \
[![Updated Badge](https://badges.pufler.dev/updated/inha-zjcao/github-classrooms-cpp-helloworld-autograding-template)](https://badges.pufler.dev) [![Visits Badge](https://badges.pufler.dev/visits/inha-zjcao/github-classrooms-cpp-helloworld-autograding-template)](https://badges.pufler.dev)



