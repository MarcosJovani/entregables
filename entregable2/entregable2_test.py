import time

from entregable2 import *


def check_solution(stack: List[bool], solution: List[int]) -> bool:
    for t in solution:
        if t < 0:
            raise Exception("A step can not be a negative number: {t}")
        if t > len(stack):
            raise Exception("A step can not be larger than len(stack): {t} > {len(stack)}")
        stack2 = stack[:t]
        for i in range(t):
            stack[i] = not stack2[t-1-i]
    return all(stack)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Use:')
        print(f'    python3 {sys.argv[0]} <instance_file_name>')
        sys.exit(1)

    # Parsing the instace filename to get the steps -------------
    try:
        steps = int(sys.argv[1].split('.')[0].split('_')[-1])
    except Exception as e:
        print(f"Exception parsing <instance_file_name> ({sys.argv[1]}):", e)
        sys.exit(1)

    # Reading the instance --------------------------------------
    line = ''
    stack = []
    stack_copy = []
    print('- Reading the instance...', end='')
    try:
        with open(sys.argv[1]) as f:
            line = f.readline().strip()
        stack = [e == 'o' for e in line]
        stack_copy = stack[:]
        print('Ok!')
    except Exception as e:
        print("Exception reading <instance_file_name> ({sys.argv[1]}):", e)
        sys.exit(1)

    # Getting the solution --------------------------------------
    print('- Getting the solution (process)...', end='')
    sys.stdout.flush()
    t = -1
    try:
        t1 = time.process_time()
        solution = process(stack)
        t2 = time.process_time()
        t = t2 - t1  # tiempo de proceso utilizado en process
        print('Ok!')
    except Exception as e:
        print("Exception running 'process':", e)
        sys.exit(1)

    # Checking the solution --------------------------------------
    print('- Checking the solution...', end='')
    sys.stdout.flush()
    is_valid = False
    try:
        is_valid = check_solution(stack_copy, solution)
    except Exception as e:
        print("\nException running 'check_solution':", e)
        sys.exit(1)
    print('Ok!')

    # Ouput results ----------------------------------------------
    sol_msg = 'ERROR'
    if is_valid:
        sol_msg = 'OK' if steps == len(solution) else 'NOT OPTIMAL'
    time_msg = 'OK' if t <= 1 else 'ERROR'
    print (f"SOLUTION {sol_msg} - TIME {time_msg} ({t:.3f})")
