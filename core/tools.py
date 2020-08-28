from optparse import OptionParser
import sys
from config.env import get_env


def _confirm_phase():
    phase = get_env('common')
    service_name = get_env['common'].get('SERVICE_NAME', '(none)')
    print('Your current environment values are below')
    print('-' * 80)
    print('\tSERVICE_NAME        : %s' % service_name)
    print('\tPHASE               : %s' % phase)
    if 'template' in get_env:
        print('\tTEMPLATE            : %s' % get_env['template']['NAME'])
    if 'elasticbeanstalk' in get_env:
        eb = get_env['elasticbeanstalk']
        for eb_env in eb['ENVIRONMENTS']:
            aws_default_region = get_env['aws']['AWS_DEFAULT_REGION'] \
                if 'AWS_DEFAULT_REGION' not in eb_env \
                else eb_env['AWS_DEFAULT_REGION']
            print('\tCNAME of %-10s : %-20s (%s)' % (eb_env['NAME'], eb_env['CNAME'], aws_default_region))
    print('-' * 80)

    answer = input('Please type in the name of phase \'%s\' to confirm: ' % phase)
    if answer != phase:
        print('The execution is canceled.')
        sys.exit(0)


def parse_args(require_arg=False):
    if require_arg:
        usage = 'usage: %prog [options] arg'
    else:
        usage = 'usage: %prog [options]'

    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--force", action="store_true", help='skip the phase confirm')
    (options, args) = parser.parse_args(sys.argv)

    if not options.force:
        _confirm_phase()

    return args


def print_message(message):
    print('*' * 80)
    print(message + '\n')
