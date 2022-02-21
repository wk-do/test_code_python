
import sys
from termcolor import cprint

# 현재 실행 중인 함수명 알아내기/출력하기...
def ilaya1():
    current_func_name = sys._getframe().f_code.co_name
    print("The current running function name : {}".format(current_func_name))
    aa = 5
    print("{}/{}".format(current_func_name, aa))
    print("The current running function name :", ilaya1.__name__)


def dbg(self, *args, sep=' ', end='\n', file=None):
    print(self, *args, sep=' ', end='\n', file=None)


# 라인넘버와 함수명 출력하기...
def line_info(return_type=None):
    import inspect

    ### line number
    '''
      여기를 호출한 곳의 라인위치(라인번호)를 리턴한다.
    '''
    cf = inspect.currentframe()
    linenumber = cf.f_back.f_lineno

    ### Call to Function name
    '''
      여기를 호출한 곳의 함수이름(function name(def))를 리턴한다.
    '''
    func_name = cf.f_back.f_code.co_name

    ### file name
    '''
      여기를 호출한 파일 이름을 리턴한다.
    '''
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    get_filename = filename.split('/')[-1]

    if return_type == 'filename':
        result_info = f'{get_filename}'
    elif return_type == 'function' or return_type == 'func_name' or return_type == 'f_name':
        result_info = f'{func_name}'
    elif return_type == 'lineinfo' or return_type == 'linenum' or return_type == 'lineno':
        result_info = f'{linenumber}'
    elif return_type == 'info_all' or return_type is None:
        # result_info = f'{get_filename}({func_name}.{linenumber})'
        result_info = f'({func_name}.{linenumber})'
    else:
        result_info = f'{get_filename}({func_name}.{linenumber})'
    return result_info


# 색깔이 추가되어 print된다.....
def get_line_info_all():
    cprint(f'get_line_info_all : {line_info(return_type="info_all")}', 'green')
def get_line_number():
    cprint(f'get_line_number : {line_info(return_type="lineno")}', 'yellow')
def get_filename():
    cprint(f'get_filename : {line_info(return_type="filename")}', 'blue')
def get_function_name():
    cprint(f'get_function_name : {line_info(return_type="f_name")}', 'red')
def get_arg_null():
    cprint(f'get_arg_null : {line_info()}')

if __name__ == '__main__':
    ilaya1()
    dbg('__print__ test')
    print(line_info())
    print(line_info('filename'))

    print('======================')
    a = 18
    print(f'{line_info()} This is test code a={a}')



### 화면 출력을 위한 함수 호출
get_line_info_all()
get_line_number()
get_filename()
get_function_name()
get_arg_null()