from optparse import OptionParser

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
