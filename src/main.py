import enum
import src.graph_reader as gr
import src.algo_and_tools as at


GRAPH = "..\input\graph.txt"
TEST_GRAPH = '..\input/test.txt'
TEST_GRAPH_2 = '..\input/test_2.txt'


if __name__ == '__main__':
    graph = gr.graph_builder(TEST_GRAPH_2)
    message, res = at.top_sort_(graph)
    if message:
        print(res)
    else:
        print('Cycle was found!!!')