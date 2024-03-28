"""
test main.cpp
"""

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
        default= "Czjing\n", 
        help='test input.'
    )
    parser.add_argument('--cmd_output', type=str, 
        default= "Hello Czjing!\n", 
        help='test output.'
    )
    args = parser.parse_args()

    # print(args)
    runing(args)

