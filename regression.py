import argparse
import numpy


def train(polynomial_degree, path_to_csv):
    print('train ', polynomial_degree, path_to_csv)


def evaluate(x):
    print('evaluate ', x)


COMMAND_FUNCTIONS = {'evaluate': evaluate,
                     'train': train}


def plot():
    import matplotlib.pyplot as mpl
    data = numpy.genfromtxt('./ai-task-samples.csv', delimiter=',')
    mpl.plot(data[:, 0], data[:, 1], ls='none', marker='.')
    mpl.show()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_train = subparsers.add_parser('train', help='Train the model')
    parser_train.add_argument(
        'polynomial_degree', help='Degree of the polynomial which shall be approximated')
    parser_train.add_argument(
        'path_to_csv', default='./ai-task-samples.csv', help='Patch to csv file used for training')

    parser_evaluate = subparsers.add_parser('evaluate', help='Evaluate the approximated function at the given point')
    parser_evaluate.add_argument(
        'x', help='Point X at which the approximated function shall be evaluated')

    kwargs = vars(parser.parse_args())
    if kwargs.get('command') is None:
        print('Required arguments were not provided')
        parser.print_usage()
        exit()
    command = kwargs.pop('command')

    return COMMAND_FUNCTIONS[command], kwargs


if __name__ == '__main__':
    command, kwargs = parse_arguments()
    command(**kwargs)
    # plot()
