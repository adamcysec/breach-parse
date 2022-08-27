import argparse
import textwrap
import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count
import glob
import os.path
from contextlib import ExitStack

def get_args():
    parser = argparse.ArgumentParser(
        description="Search BreachCompiliation data and save output to file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Examples:
        py breach-parse.py @yahoo.com yahoo
        py breach-parse.py @yahoo.com yahoo --userfile
        py breach-parse.py @yahoo.com yahoo --passwordfile
        py breach-parse.py @yahoo,com yahoo -u -p
        ''')
    )

    parser.add_argument('term', action='store', type=str, help="the string to search on")
    parser.add_argument('output', action='store', type=str, help="output file name")
    parser.add_argument('-d', '--datafile', action='store', type=str, default=r"/media/adam/BreachCompilation/data", required=False, help="BreachCompilation data dir")
    parser.add_argument('-u', '--userfile', action='store_true', help="output list of user names")
    parser.add_argument('-p', '--passwordfile', action='store_true', help="output list of passwords")

    args = parser.parse_args() # parse arguments

    args_dict = vars(args)

    return args_dict

def get_breach_files(file_path):
    """get all BreachCompilation txt files

    Parameters:
    -----------
    file_path : str
        BreachCompilation data directory path
    
    Returns:
    --------
    breach_files : list
        BreachCompilation txt files
    """

    files = [os.path.join(dirpath, filename) for (dirpath, dirs, files) in os.walk(file_path) for filename in (dirs + files)]
    breach_files = [file for file in files if os.path.isfile(file)]

    return breach_files

def format_data(files, term):
    """format the data to work with the multiprocessing Pool()

    groups the files paths into batches of 5
    
    Parameters:
    -----------
    files : list
        contains 1981 files paths
    term : str
        user supplied search term

    Returns:
        data : list
    """

    data = []
    five_files = []
    count = 0
    for file in files:
        if count == 5:
            data.append([five_files, term])
            five_files = []
            count = 0
        else:
            five_files.append(file)
            count += 1

    return data

def search_file(files, search_term):
    """enumerate all files line by line and 
    return lines that contain the search term

    Parameters:
    -----------
    files : list
        five file paths
    search_term : str
        user supplied search term
    
    Returns:
    --------
    results : list
        contains results for each file enumerated
    """
    
    results = []
    
    with ExitStack() as stack:
        working_files = [stack.enter_context(open(x, "rb")) for x in files]
        for lines in working_files:
            for line in lines:
                #if insensitive:
                #    if search_term.lower() in line.lower():
                #        results.append(line)
                #else:
                if search_term in line:
                    results.append(line)
    
    return results

def out_file(results, out_filename):
    """save the search data to file

    Parameters:
    -----------
    results : list
        postive matches from the search term
    out_filename : str
        file name
    """
    
    with open(out_filename, 'w') as f:
        for row in results:
            for item in row:
                data = item.decode('utf-8')
                f.writelines(data)
    
    print(f"file saved: {out_filename}")

def out_user_file(results, out_filename):
    """save user names from search data to file

    Parameters:
    -----------
    results : list
        postive matches from the search term
    out_filename : str
        file name
    """

    with open(out_filename, 'w') as f:
        for row in results:
            for item in row:
                try:
                    data = item.decode('utf-8')
                    x = data.split(':', 1)
                    
                    # some entries use ';' as a delimiter
                    if len(x) < 2:
                        x = data.split(';', 1)

                    f.writelines(f"{x[0]}\n")
                    
                except UnicodeDecodeError as err:
                    print(f"ERROR saving user file: {err}")
    
    print(f"file saved: {out_filename}")

def out_password_file(results, out_filename): 
    """save passwords from search data to file

    Parameters:
    -----------
    results : list
        postive matches from the search term
    out_filename : str
        file name
    """

    with open(out_filename, 'w') as f:
        for row in results:
            for item in row:
                try:
                    data = item.decode('utf-8')
                    
                    x = data.split(':', 1)
                    # some entries use ';' as a delimiter
                    if len(x) < 2:
                        x = data.split(';', 1) 
                    
                    f.writelines(x[1])
                
                except UnicodeDecodeError as err:
                    print(f"ERROR saving password file: {err}")
                    
    print(f"file saved: {out_filename}")

def main():
    start = timer()

    # read args
    args = get_args()
    out_filename = args['output']
    term = args['term']
    b_term = str.encode(term)
    userfile = args['userfile']
    passwordfile = args['passwordfile']

    print(f"starting search on {cpu_count()} cores")

    # prep search
    breach_fpath = args['datafile']
    breach_data_files = get_breach_files(breach_fpath) # get all txt breach files
    queue = format_data(breach_data_files, b_term) # prep data for the pool
    
    # start multi threaded search
    with Pool() as pool:
        res = pool.starmap(search_file, queue)
    
    print("search complete!")
    print("saving results")
    
    # output results
    out_file(res, out_filename)

    if userfile:
        #py_logger.info("saving results to user file")
        out_user_file(res, f"{out_filename}_users.txt")
    if passwordfile:
        #py_logger.info("saving results to password file")
        out_password_file(res, f"{out_filename}_passwords.txt")
    
    end = timer()
    print(f"elpased time: {end - start}")

if __name__ == '__main__':
    main()