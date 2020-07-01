import argparse
import os
import pkg_resources


def update_req_version(fname):

    output_str = ''
    if os.path.isfile(fname):
        with open(fname) as f:
            content = f.readlines()
            for line in content:
                module = line.rstrip().split('==')[0]
                local_version = pkg_resources.get_distribution(module).version
                output_str += '{}=={}\n'.format(module, local_version)
    else:
        raise AttributeError('No \'{}\' file.'.format(fname))

    with open(fname, 'w') as outfile:
        outfile.write(output_str)


def main():

    req_file = 'pipreqs.txt'
    path_folder = os.getcwd()

    # use pipreqs to generate requirements.txt
    os.system('pipreqs --force --savepath {} {}'.format(req_file, path_folder))

    update_req_version(req_file)


if __name__ == "__main__":
    main()
